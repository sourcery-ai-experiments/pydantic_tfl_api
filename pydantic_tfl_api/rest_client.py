# from https://github.com/dhilmathy/TfL-python-api
# MIT License

# Copyright (c) 2018 Mathivanan Palanisamy

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import requests
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode
from .config import base_url
from .api_token import ApiToken

class RestClient():
    """RestClient.

    :param ApiToken api_token: API token to access TfL unified API
    """

    def __init__(self, api_token: ApiToken = None):
        self.api_token = {"app_key": api_token.app_key} if api_token else None

    def send_request(self, location, params=None):
        return requests.get(base_url + location + "?" + self._get_query_strings(params))

    def _get_query_strings(self, params):
        if params is None:
            params = {}
        if self.api_token is not None:
            params.update(self.api_token)
        return urlencode(params)