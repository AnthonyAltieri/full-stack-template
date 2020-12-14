import json

import flask_restful
from flask import make_response

from json_encoder import JSONEncoderWithDateLikeSupport


def output_json_with_custom_encoder(data, code, headers=None):
    response = make_response(json.dumps(data, cls=JSONEncoderWithDateLikeSupport), code)
    response.headers.extend(headers or {})
    return response


class API(flask_restful.Api):
    def __init__(self, *args, **kwargs):
        super(API, self).__init__(*args, **kwargs)
        self.representations["application/json"] = output_json_with_custom_encoder
