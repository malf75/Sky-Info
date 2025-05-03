import datetime
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from datetime import date
from pydantic import BaseModel
from typing import Optional
from geopy.geocoders import Nominatim
from starlette import status
from astral import LocationInfo
from timezonefinder import TimezoneFinder
from astral.moon import moonset, moonrise, phase
from astral.sun import sunrise, sunset, noon
from moon_phases import moon_phase

app = FastAPI()

class InfoRequest(BaseModel):
    date: Optional[date]
    city: str

geolocator = Nominatim(user_agent="Sky-Info")
tz_finder = TimezoneFinder()

@app.get("/")
async def redirect_index():
    return RedirectResponse("/docs")

@app.post("/moon")
async def moon_info(request: InfoRequest):
    try:
        location = geolocator.geocode(request.city)
        if not request.date:
            request.date = datetime.date.today()
        if location:
            timezone_str = tz_finder.timezone_at(lat=location.latitude, lng=location.longitude)
            country = location.raw.get('display_name', '').split(',')[-1].strip()
            city = LocationInfo(request.city, country, timezone_str, location.latitude, location.longitude)
            return {
                "date":request.date,
                "city":request.city,
                "location":{
                    "latitude": location.latitude,
                    "longitude": location.longitude,
                },
                "moon_phase":moon_phase(phase(request.date)),
                "moon_rise":moonrise(city.observer, request.date, timezone_str).strftime('%Y-%m-%d %H:%M:%S'),
                "moon_set":moonset(city.observer, request.date, timezone_str).strftime('%Y-%m-%d %H:%M:%S')
            }
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="City not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)

@app.post("/sun")
async def sun_info(request: InfoRequest):
    try:
        location = geolocator.geocode(request.city)
        if not request.date:
            request.date = datetime.date.today()
        if location:
            timezone_str = tz_finder.timezone_at(lat=location.latitude, lng=location.longitude)
            country = location.raw.get('display_name', '').split(',')[-1].strip()
            city = LocationInfo(request.city, country, timezone_str, location.latitude, location.longitude)
            return {
                "date":request.date,
                "city":request.city,
                "location":{
                    "latitude": location.latitude,
                    "longitude": location.longitude,
                },
                "sun_rise":sunrise(city.observer, request.date, timezone_str).strftime('%Y-%m-%d %H:%M:%S'),
                "sun_noon":noon(city.observer, request.date, timezone_str).strftime('%Y-%m-%d %H:%M:%S'),
                "sun_set":sunset(city.observer, request.date, timezone_str).strftime('%Y-%m-%d %H:%M:%S')
            }
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="City not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)