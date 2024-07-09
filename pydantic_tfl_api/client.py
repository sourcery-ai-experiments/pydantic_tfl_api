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

from .config import endpoints
from .api_token import ApiToken
from .rest_client import RestClient
from importlib import import_module
from requests import Response
import pkgutil
from pydantic import BaseModel
from . import models


class Client:
    """Client

    :param ApiToken api_token: API token to access TfL unified API
    """

    def __init__(self, api_token):
        self.client = RestClient(api_token)
        self.models = self._load_models()

    def _load_models(self):
        models_dict = {}
        for importer, modname, ispkg in pkgutil.iter_modules(models.__path__):
            module = import_module(f".models.{modname}", __package__)
            for model_name in dir(module):
                attr = getattr(module, model_name)
                if isinstance(attr, type) and issubclass(attr, BaseModel):
                    models_dict[model_name] = attr
        print(models_dict)
        return models_dict

    def _deserialize(self, model_name, response):
        Model = self.models.get(model_name)
        if Model is None:
            raise ValueError(f"No model found with name {model_name}")
        return Model(**response.json())

    def _deserialize_error(self, response: Response):
        # if content is json, deserialize it, otherwise manually create an ApiError object
        if response.headers.get("content-type") == "application/json":
            return self._deserialize("ApiError", response)
        return models.ApiError(
            timestampUtc=response.headers.get("date"),
            exceptionType="Unknown",
            httpStatusCode=response.status_code,
            httpStatus=response.reason,
            relativeUri=response.url,
            message=response.text,
        )

    def get_stop_points_by_line_id(self, line_id):
        response = self.client.send_request(
            endpoints["stopPointsByLineId"].format(line_id)
        )
        if response.status_code is not 200:
            return self._deserialize_error(response)
        return self._deserialize("StopPoint", response)

    def get_line_meta_modes(self):
        response = self.client.send_request(endpoints["lineMetaModes"])
        if response.status_code is not 200:
            return self._deserialize_error(response)
        return self._deserialize("Mode", response)

    def get_lines(self, line_id=None, mode=None):
        if line_id is None and mode is None:
            raise Exception(
                "Either the --line_id argument or the --mode argument needs to be specified."
            )
        if line_id is not None:
            endpoint = endpoints["linesByLineId"].format(line_id)
        else:
            endpoint = endpoints["linesByMode"].format(mode)
        response = self.client.send_request(endpoint)
        if response.status_code is not 200:
            return self._deserialize_error(response)
        return self._deserialize("Line", response)

    def get_line_status(self, line, include_details=None):
        response = self.client.send_request(
            endpoints["lineStatus"].format(line), {"detail": include_details is True}
        )
        if response.status_code is not 200:
            return self._deserialize_error(response)
        return self._deserialize("Line", response)

    def get_line_status_severity(self, severity):
        response = self.client.send_request(
            endpoints["lineStatusBySeverity"].format(severity)
        )
        if response.status_code is not 200:
            return self._deserialize_error(response)
        return self._deserialize("Line", response)

    def get_route_by_line_id(self, line_id):
        response = self.client.send_request(endpoints["routeByLineId"].format(line_id))
        if response.status_code is not 200:
            return self._deserialize_error(response)
        return self._deserialize("Line", response)

    def get_route_by_mode(self, mode):
        response = self.client.send_request(endpoints["routeByMode"].format(mode))
        if response.status_code is not 200:
            return self._deserialize_error(response)
        return self._deserialize("Line", response)

    def get_line_disruptions_by_line_id(self, line_id):
        response = self.client.send_request(
            endpoints["lineDisruptionsByLineId"].format(line_id)
        )
        if response.status_code is not 200:
            return self._deserialize_error(response)
        return self._deserialize("Disruption", response)

    def get_line_disruptions_by_mode(self, mode):
        response = self.client.send_request(
            endpoints["lineDisruptionsByMode"].format(mode)
        )
        if response.status_code is not 200:
            return self._deserialize_error(response)
        return self._deserialize("Disruption", response)

    def get_stop_points_by_id(self, id):
        response = self.client.send_request(endpoints["stopPointById"].format(id))
        if response.status_code is not 200:
            return self._deserialize_error(response)
        return self._deserialize("StopPoint", response)

    def get_stop_points_by_mode(self, mode):
        response = self.client.send_request(endpoints["stopPointByMode"].format(mode))
        if response.status_code is not 200:
            return self._deserialize_error(response)
        return self._deserialize("StopPointsResponse", response)

    def get_stop_point_meta_modes(self):
        response = self.client.send_request(endpoints["stopPointMetaModes"])
        if response.status_code is not 200:
            return self._deserialize_error(response)
        return self._deserialize("Mode", response)

    def get_arrivals_by_line_id(self, line_id):
        response = self.client.send_request(
            endpoints["arrivalsByLineId"].format(line_id)
        )
        if response.status_code is not 200:
            return self._deserialize_error(response)
        return self._deserialize("Prediction", response)
