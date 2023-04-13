from typing import Optional
import requests
import httpx

api_key: Optional[str] = None


async def get_report_async(city, state: Optional[str], country: str, units: str) -> dict:
    if state:
        q = f'{city},{state},{country}'
    else:
        q = f'{city},{country}'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}&units={units}'
    print(url)

    async with httpx.AsyncClient() as client:
        # response = requests.get(url)
        response = await client.get(url)
        response.raise_for_status()

    data = response.json()
    forecast = data['main']
    print(data)
    return forecast
