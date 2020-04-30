import os

from flask import Flask, render_template, make_response
from flask import redirect, request, jsonify, url_for
from gevent import monkey

# monkey.patch_all()
# from gevent.pywsgi import WSGIServer
from project import create_app

# from project.settings import GEOCODING_API_KEY

# import project.utils.data_config as data_config

app = create_app('flask_prod.cfg')


@app.route("/")
def rendering_main_page():
    return render_template("main-page.html")


@app.route('/getall', methods=['GET'])
def get_all():
    try:

        request.args.get('key', '')

        return jsonify({'test': 'testy'})
    except Exception as e:
        return (str(e))


@app.route('/getsentiment', methods=['GET'])
def get_sentiment():
    try:
        headline = request.args.get('headline', '')

        if headline:
            compoundScore = app.engine.get_scores_headline(headline)
            return jsonify({'result': compoundScore})
        return jsonify({'result': '0.'})
    except Exception as e:
        return (str(e))


@app.route('/getsentiments', methods=['GET'])
def get_sentiments():
    try:
        headlines = request.args.get('headlines', '')

        if headlines:
            compoundScores = [app.engine.get_scores_headline(headline) for headline in headlines.split('|')]
            return jsonify({'result': compoundScores})
        return jsonify({'result': '0.'})
    except Exception as e:
        return (str(e))


@app.route('/get-sentiment-article', methods=['GET'])
def get_sentinment_article():
    try:
        url = "https://www.mirror.co.uk/news/world-news/victims-fury-brit-paedophile-makes-15256215"
        if url:
            page = app.service.get_article_page(url)
            content = app.service.get_article_content(page)

            score = app.engine.get_scores_headline(content)
            return jsonify({'result': score})
        return jsonify({'result': '0.'})
    except Exception as e:
        return (str(e))


@app.route('/get-bitcoin-latest', methods=['GET'])
def get_bitcoin_latest():
    try:
        url = "https://newsapi.org/v2/everything?q=bitcoin&from=2019-11-03&sortBy=publishedAt&apiKey=338d2068147b4dff8d3d030fcb59e4af"
        if url:

            everythingResults = app.service.get_article_page(url)
            articleUrlDescs = app.service.get_articles_from_everything(everythingResults)
            articleUrlScore = {}

            for url, desc in articleUrlDescs:
                page = app.service.get_article_page(url)
                content = app.service.get_article_content(page)
                score = app.engine.get_scores_headline(content)

                articleUrlScore[url] = score

            avgScore = sum(articleUrlScore.values()) / len(articleUrlScore)
            return jsonify({'result':
                                {'scores': articleUrlScore,
                                 'average': avgScore,
                                 }})
        return jsonify({'result': '0.'})
    except Exception as e:
        return (str(e))


# server = WSGIServer(('0.0.0.0', 5001), app)
# app.debug = True
# app.run(host = '192.168.1.67',port=5001)
# app.run(host='0.0.0.0', port=5001)

# server = WSGIServer(('0.0.0.0', 5001), app)
# server.serve_forever()
# android:style/TextAppearance.Material.


if __name__ == '__main__':
    app.run()
