from pydantic import BaseModel, Field
from datetime import datetime
from typing import List

from .validity_period import ValidityPeriod
from .disruption import Disruption

class LineStatus(BaseModel):
    id: int = Field(alias='id')
    line_id: str = Field(alias='lineId')
    status_severity: int = Field(alias='statusSeverity')
    status_severity_description: str = Field(alias='statusSeverityDescription')
    reason: str = Field(alias='reason')
    created: datetime = Field(alias='created')
    last_update: datetime = Field(alias='lastUpdate')
    validity_periods: List[ValidityPeriod] = Field(alias='validityPeriods')
    disruption: List[Disruption] = Field(alias='disruption')

    class Config:
        allow_population_by_field_name = True