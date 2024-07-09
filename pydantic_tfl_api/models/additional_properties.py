from pydantic import BaseModel, Field
from datetime import datetime

class AdditionalProperties(BaseModel):
    category: str = Field(alias='category')
    key: str = Field(alias='key')
    source_system_key: str = Field(alias='sourceSystemKey')
    value: str = Field(alias='value')
    modified: datetime = Field(alias='modified')

    class Config:
        allow_population_by_field_name = True
