from pydantic import BaseModel, Field
from typing import List, Optional

from .stop_point import StopPoint

class StopPointsResponse(BaseModel):
    stop_points: Optional[List[StopPoint]] = Field(None, alias='stopPoints')
    page_size: int = Field(alias='pageSize')
    total: int = Field(alias='total')
    page: int = Field(alias='page')

    class Config:
        allow_population_by_field_name = True
