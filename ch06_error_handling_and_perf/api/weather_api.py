from typing import Optional

import fastapi
from fastapi import Depends
from models.location import Location
from models.validation_error import ValidationError
from services import openweather_service

router = fastapi.APIRouter()


@router.get('/api/weather/{city}')
async def weather(location: Location = Depends(), units: Optional[str] = 'metric'):
    # report = await openweather_service.get_report_async(location.city, location.state, location.country, units)
    # print(type(report), report)
    # return report
    try:
        return await openweather_service.get_report_async(location.city, location.state, location.country, units)
    except ValidationError as ve:
        return fastapi.Response(content=ve.error_msg, status_code=ve.status_code)
    except Exception as x:
        return fastapi.Response(content=str(x), status_code=500)
