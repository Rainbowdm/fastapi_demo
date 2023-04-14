import datetime

from pydantic import BaseModel
from typing import Optional

from models.location import Location


class Report(BaseModel):
    descripion: str
    location: Location
    created_date: Optional[datetime]
