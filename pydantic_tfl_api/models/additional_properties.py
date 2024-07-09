from pydantic import BaseModel, Field
from datetime import datetime

class AdditionalProperties(BaseModel):
    category: str = Field(alias='category')
    key: str = Field(alias='key')
    source_system_key: str = Field(alias='sourceSystemKey')
    value: str = Field(alias='value')
    modified: datetime = Field(alias='modified')

    model_config = {'populate_by_name': True}
