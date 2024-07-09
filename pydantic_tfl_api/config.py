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

base_url = "https://api.tfl.gov.uk/"

endpoints = {
    'stopPointsByLineId': 'Line/{0}/StopPoints',
    'lineMetaModes': 'Line/Meta/Modes',
    'linesByLineId': 'Line/{0}',
    'linesByMode': 'Line/Mode/{0}',
    'lineStatus': 'Line/{0}/Status',
    'lineStatusBySeverity': 'Line/Status/{0}',
    'lineStatusByMode': 'Line/Mode/{0}/Status',
    'routeByLineId': 'Line/{0}/Route',
    'routeByMode': 'Line/Mode/{0}/Route',
    'lineDisruptionsByLineId': 'Line/{0}/Disruption',
    'lineDisruptionsByMode': 'Line/Mode/{0}/Disruption',
    
    'stopPointMetaModes': 'StopPoint/Meta/Modes',
    'stopPointById': 'StopPoint/{0}',
    'stopPointByMode': 'StopPoint/Mode/{0}',

    'arrivalsByLineId': 'Line/{0}/Arrivals'
}