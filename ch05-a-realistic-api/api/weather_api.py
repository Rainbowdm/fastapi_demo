from typing import Optional

import fastapi
from fastapi import Depends
from models.location import Location
from services import openweather_service

router = fastapi.APIRouter()


@router.get('/api/weather/{city}')
def weather(location: Location = Depends(), units: Optional[str] = 'metric'):
    report = openweather_service.get_report(location.city, location.state, location.country, units)
    return report
