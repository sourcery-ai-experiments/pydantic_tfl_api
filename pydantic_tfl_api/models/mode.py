from pydantic import BaseModel, Field

class Mode(BaseModel):
    is_tfl_service: bool = Field(alias='isTflService')
    is_fare_paying: bool = Field(alias='isFarePaying')
    is_scheduled_service: bool = Field(alias='isScheduledService')
    mode_name: str = Field(alias='modeName')

    class Config:
        allow_population_by_field_name = True