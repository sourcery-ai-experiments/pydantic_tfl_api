from pydantic import BaseModel, Field

class ServiceType(BaseModel):
    name: str = Field(alias='name')
    uri: str = Field(alias='uri')

    class Config:
        allow_population_by_field_name = True
