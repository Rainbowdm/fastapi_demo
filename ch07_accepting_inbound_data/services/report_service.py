from datetime import datetime
from typing import List
from models.location import Location

from models.reports import Report

reports: List[Report] = []


async def get_reports() -> List:
    # Would be an async call here.
    return list(reports)


async def add_report(description: str, location: Location) -> Report:
    now = datetime.now()
    report = Report(location=location, description=description, created_date=now)
    # Simulate saving to DB.
    # Would be an async call here.
    reports.append(report)
    reports.sort(key=lambda r: r.created_date, reverse=True)
    return report
