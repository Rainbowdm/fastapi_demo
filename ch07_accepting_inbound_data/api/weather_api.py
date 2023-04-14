from typing import Optional, List

import fastapi
from fastapi import Depends
from models.location import Location
from models.validation_error import ValidationError
from services import openweather_service, report_service

from models.reports import Report

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
    except Exception as ex:
        return fastapi.Response(content=str(ex), status_code=500)


@router.get('/api/reports', name='all_reports')
async def reports_get() -> List[Report]:
    # report_service.add_report("A", Location(city="Portland"))
    # report_service.add_report("B", Location(city="NYC"))
    return await report_service.get_reports()
