import datetime
import uuid
from typing import List

from models.location import Location
from models.reports import Report

reports: List[Report] = []


async def get_reports() -> List[Report]:
    # Would be an async call here.
    return list(reports)


async def add_report(description: str, location: Location) -> Report:
    now = datetime.datetime.now()
    report = Report(
        id=str(uuid.uuid4()),
        location=location,
        description=description,
        created_date=now)
    # Simulate saving to the DB.
    # Would be an async call here.
    reports.append(report)
    reports.sort(key=lambda r: r.created_date, reverse=True)
    return report
