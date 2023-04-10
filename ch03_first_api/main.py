import fastapi
import uvicorn

api = fastapi.FastAPI()


@api.get('/api/calculate')
def calculate(x: int, y: int, z: int = 10):
    value = (x + y) * z
    return {
        'value': value
    }


# Write in browser - http://127.0.0.1:8000/api/calculate?x=2&y=3&z=10

uvicorn.run(api, port=8000, host="127.0.0.1")
