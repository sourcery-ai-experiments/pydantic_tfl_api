from pydantic import BaseModel, Field
from datetime import datetime

class ValidityPeriod(BaseModel):
    from_date: datetime = Field(alias='fromDate')
    to_date: datetime = Field(alias='toDate')
    is_now: bool = Field(alias='isNow')

    class Config:
        allow_population_by_field_name = True
