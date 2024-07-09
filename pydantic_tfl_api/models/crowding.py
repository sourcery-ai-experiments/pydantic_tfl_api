from pydantic import BaseModel, Field
from typing import List

from .passenger_flow import PassengerFlow
from .train_loading import TrainLoading


class Crowding(BaseModel):
    passenger_flows: List[PassengerFlow] = Field(alias='passengerFlow')
    train_loadings: List[TrainLoading] = Field(alias='trainLoadings')

    class Config:
        allow_population_by_field_name = True