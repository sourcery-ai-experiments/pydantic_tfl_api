from pydantic import BaseModel, Field

class PassengerFlow(BaseModel):
    time_slice: str = Field(alias='timeSlice')
    value: int = Field(alias='value')

    class Config:
        allow_population_by_field_name = True