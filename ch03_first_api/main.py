from typing import Optional

import fastapi
import uvicorn

api = fastapi.FastAPI()


@api.get('/api/calculate')
def calculate(x: int, y: int, z: Optional[int] = None):
    if z == 0:
        return fastapi.Response(content='{"error": ERROR: Z cannot be zero.}',
                                media_type="application/json",
                                status_code=400)
    value = (x + y) / z
    if z is not None:
        value /= z
    return {
        'x': x,
        'y': y,
        'z': z,
        'value': value
    }


# Write in browser - http://127.0.0.1:8000/api/calculate?x=2&y=3&z=10

uvicorn.run(api, port=8000, host="127.0.0.1")
