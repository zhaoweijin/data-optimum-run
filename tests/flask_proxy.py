# -*- coding: utf-8 -*-

from flask import Flask
from flask import Response
from flask import stream_with_context

import requests

app = Flask(__name__)
app.debug = True

uri = 'http://app.appgame.com'

@app.route('/<path:url>')
def home(url):
    print url
    # if url.find(uri)==-1:
    #     url = uri + '/' + url

    req = requests.get(url, stream = True)
    return Response(stream_with_context(req.iter_content()), content_type = req.headers['content-type'])

if __name__ == '__main__':
    app.run(host='0.0.0.0')