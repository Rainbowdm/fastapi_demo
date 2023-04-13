from typing import Optional

import fastapi
from fastapi import Depends
from models.location import Location
from services import openweather_service

router = fastapi.APIRouter()


@router.get('/api/weather/{city}')
async def weather(location: Location = Depends(), units: Optional[str] = 'metric'):
    report = await openweather_service.get_report_async(location.city, location.state, location.country, units)
    print(type(report), report)
    return report
