from pydantic import BaseModel, Field
from datetime import datetime

class RouteSection(BaseModel):
    route_code: str = Field(alias='routeCode')
    name: str = Field(alias='name')
    direction: str = Field(alias='direction')
    origination_name: str = Field(alias='originationName')
    destination_name: str = Field(alias='destinationName')
    originator: str = Field(alias='originator')
    destination: str = Field(alias='destination')
    service_type: str = Field(alias='serviceType')
    valid_to: datetime = Field(alias='validTo')
    valid_from: datetime = Field(alias='validFrom')

    class Config:
        allow_population_by_field_name = True
