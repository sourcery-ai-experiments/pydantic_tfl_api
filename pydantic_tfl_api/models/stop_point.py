from pydantic import BaseModel, Field
from typing import List, Optional


from .line_group import LineGroup
from .line_mode_group import LineModeGroup
from .additional_properties import AdditionalProperties

class StopPoint(BaseModel):
    naptan_id: str = Field(alias='naptanId')
    platform_name: str = Field(alias='platformName')
    indicator: str = Field(alias='indicator')
    stop_letter: str = Field(alias='stopLetter')
    modes: List[str] = Field(alias='modes')
    ics_code: str = Field(alias='icsCode')
    sms_code: str = Field(alias='smsCode')
    stop_type: str = Field(alias='stopType')
    station_naptan: str = Field(alias='stationNaptan')
    accessibility_summary: str = Field(alias='accessibilitySummary')
    hub_naptan_code: str = Field(alias='hubNaptanCode')
    lines: List['Line'] = Field(alias='lines')
    line_group: List[LineGroup] = Field(alias='lineGroup')
    line_mode_groups: List[LineModeGroup] = Field(alias='lineModeGroups')
    full_name: str = Field(alias='fullName')
    naptan_mode: str = Field(alias='naptanMode')
    status: bool = Field(alias='status')
    id: str = Field(alias='id')
    url: str = Field(alias='url')
    common_name: str = Field(alias='commonName')
    distance: int = Field(alias='distance')
    place_type: str = Field(alias='placeType')
    additional_properties: List[AdditionalProperties] = Field(alias='additionalProperties')
    children: Optional[List['StopPoint']] = Field(None, alias='children')
    children_urls: List[str] = Field(alias='childrenUrls')
    lat: int = Field(alias='lat')
    lon: int = Field(alias='lon')

    class Config:
        allow_population_by_field_name = True

from .line import Line
StopPoint.model_rebuild()
