from pydantic import BaseModel, Field
from typing import List

class LineGroup(BaseModel):
    naptan_id_reference: str = Field(alias='naptanIdReference')
    station_atco_code: str = Field(alias='stationActoCode')
    line_identifier: List[str] = Field(alias='lineIdentifier')

    model_config = {'populate_by_name': True}