from pydantic import BaseModel, Field
from typing import List

class LineModeGroup(BaseModel):
    mode_name: str = Field(alias='modeName')
    line_identifier: List[str] = Field(alias='lineIdentifier')

    class Config:
        allow_population_by_field_name = True