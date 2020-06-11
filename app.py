import json
import contextlib
from urllib.parse import urljoin
import re

import requests as r
from flask import Flask, request, jsonify, abort, make_response
from pymongo import MongoClient

import config

app = Flask(__name__)


def load_movies(filename):
    with contextlib.suppress(FileNotFoundError):
        with open(filename, encoding='utf-8') as f:
            return json.loads(f.read())


def search_from_db(name):
    pat = re.compile(re.escape(name), re.I)
    with MongoClient(config.MONGO_URL) as client:
        db = client.pytest
        return list(db.movies.find({'title': {'$regex': re.compile(re.escape(name), re.I)}}))


def search_online(local_result):
    for res in local_result:
        url = urljoin(config.URL_BASE, res['id'])
        with r.get(url) as resp:
            js = resp.json()
            js['russian_title'] = res['russian_title']
            yield js


@app.route('/')
def home():
    return {'app_name': 'filmify'}


@app.route('/api/movies', methods=['GET'])
def get_movie():
    return _get_movie()


def _get_movie():
    name = request.args.get('movie', '').lower().strip()
    if len(name) == 0:
        abort(404)
    online_results = search_from_db(name)
    online_results = [s for s in search_online(online_results)]
    return {'results': online_results, 'keyword': name}


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
