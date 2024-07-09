from pydantic import BaseModel, Field

class PassengerFlow(BaseModel):
    time_slice: str = Field(alias='timeSlice')
    value: int = Field(alias='value')

    model_config = {'populate_by_name': True}