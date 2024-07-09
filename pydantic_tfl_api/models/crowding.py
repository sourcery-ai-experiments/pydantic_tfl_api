from pydantic import BaseModel, Field
from typing import List, Optional

from .passenger_flow import PassengerFlow
from .train_loading import TrainLoading


class Crowding(BaseModel):
    passenger_flows: Optional[List[PassengerFlow]] = Field(None, alias='passengerFlow')
    train_loadings: Optional[List[TrainLoading]] = Field(None, alias='trainLoadings')

    class Config:
        allow_population_by_field_name = True