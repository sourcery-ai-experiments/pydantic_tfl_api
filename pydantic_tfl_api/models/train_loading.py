from pydantic import BaseModel, Field

class TrainLoading(BaseModel):
    line: str = Field(alias='line')
    line_direction: str = Field(alias='lineDirection')
    platform_direction: str = Field(alias='platformDirection')
    direction: str = Field(alias='direction')
    naptan_to: str = Field(alias='naptanTo')
    time_slice: str = Field(alias='timeSlice')
    value: int = Field(alias='value')

    class Config:
        allow_population_by_field_name = True
