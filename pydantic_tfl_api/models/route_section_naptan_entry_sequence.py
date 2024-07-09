from pydantic import BaseModel, Field

from .stop_point import StopPoint

class RouteSectionNaptanEntrySequence(BaseModel):
    ordinal: int = Field(alias='ordinal')
    stop_point: StopPoint = Field(alias='stopPoint')

    class Config:
        allow_population_by_field_name = True
