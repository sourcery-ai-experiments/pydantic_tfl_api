from pydantic import BaseModel, Field
from typing import List

class LineGroup(BaseModel):
    naptan_id_reference: str = Field(alias='naptanIdReference')
    station_atco_code: str = Field(alias='stationActoCode')
    line_identifier: List[str] = Field(alias='lineIdentifier')

    class Config:
        allow_population_by_field_name = True