from dotenv import load_dotenv, find_dotenv
import config as cfg
# Developer mode (allows env variables in desktop)
if cfg.develop == True:
    load_dotenv(find_dotenv(), override=False)

from pathlib import Path
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse, PlainTextResponse, JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exception_handlers import http_exception_handler
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from datetime import datetime, time, timedelta
from zoneinfo import ZoneInfo
import requests, os

from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession

# Start server: uvicorn main:app --reload

app = FastAPI(title="Krupam's Portfolio")#, lifespan=lifespan)

# Open Parent dir
BASE_DIR = Path(__file__).resolve().parent

STATIC_DIR = BASE_DIR / "static"
TEMPLATES_DIR = BASE_DIR / "templates"
FONTS_DIR = STATIC_DIR / "fonts"

# Static and Templates
templates = Jinja2Templates(directory=TEMPLATES_DIR)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# For any http error, send them to a specific error page
@app.exception_handler(StarletteHTTPException)
async def not_found(request: Request, exc: StarletteHTTPException):
    # HTTP Errors
    if exc.status_code == 404:
        return templates.TemplateResponse(request, "404.html", {"request": request, "title": "404", "detail": exc.detail})
    elif exc.status_code == 403:
        return templates.TemplateResponse(request, "403.html", {"request": request, "title": "403", "detail": exc.detail})
    elif exc.status_code == 401:
        return templates.TemplateResponse(request, "401.html", {"request": request, "title": "401", "detail": exc.detail})
    elif exc.status_code == 400:
        return templates.TemplateResponse(request, "400.html", {"request": request, "title": "400", "detail": exc.detail})
    elif exc.status_code == 500:
        return templates.TemplateResponse(request, "500.html", {"request": request, "title": "500", "detail": exc.detail})
    
    return await http_exception_handler(request, exc)

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    today = today_summary(request)
    week = week_summary(request)
    all = total_code_time(request)
    return templates.TemplateResponse(request, "home.html", {"request": request, "today": today["data"], "week": week["data"], "all": all["data"]})

@app.get("/robots.txt", response_class=PlainTextResponse, include_in_schema=False)
def robots_txt():
    return """\
User-agent: *

Allow: /
Allow: /mates
Allow: /gis
Allow: /field
Allow: /extracurriculars
Allow: /services
Allow: /homelab
Allow: /website
Allow: /work
Allow: /volunteer
Allow: /research
Allow: /band
Allow: /theater
Allow: /contact
"""

@app.get("/mates", response_class=HTMLResponse)
def mates(request: Request):
    return templates.TemplateResponse(request, "mates.html", {"request": request, "active_page": "mates"})

@app.get("/gis", response_class=HTMLResponse)
def gis(request: Request):
    return templates.TemplateResponse(request, "gis.html", {"request": request, "active_page": "gis"})

@app.get("/field", response_class=HTMLResponse)
def field(request: Request):
    return templates.TemplateResponse(request, "field.html", {"request": request, "active_page": "field"})

@app.get("/extracurriculars", response_class=HTMLResponse)
def extracurriculars(request: Request):
    return templates.TemplateResponse(request, "clubs.html", {"request": request, "active_page": "clubs"})

@app.get("/services", response_class=HTMLResponse)
def contact(request: Request):
    return templates.TemplateResponse(request, "services.html", {"request": request, "active_page": "services"})

@app.get("/homelab", response_class=HTMLResponse)
def homelab(request: Request):
    return templates.TemplateResponse(request, "homelab.html", {"request": request, "active_page": "homelab"})

@app.get("/website", response_class=HTMLResponse)
def website(request: Request):
    return templates.TemplateResponse(request, "website.html", {"request": request, "active_page": "website"})

@app.get("/work", response_class=HTMLResponse)
def work(request: Request):
    return templates.TemplateResponse(request, "work.html", {"request": request, "active_page": "work"})

@app.get("/hackclub", response_class=HTMLResponse)
def hackclub(request: Request):
    return templates.TemplateResponse(request, "hackclub.html", {"request": request, "active_page": "hackclub"})

@app.get("/volunteer", response_class=HTMLResponse)
def volunteer(request: Request):
    return templates.TemplateResponse(request, "volunteer.html", {"request": request, "active_page": "volunteer"})

@app.get("/research", response_class=HTMLResponse)
def research(request: Request):
    return templates.TemplateResponse(request, "research.html", {"request": request, "active_page": "research"})

@app.get("/band", response_class=HTMLResponse)
def band(request: Request):
    return templates.TemplateResponse(request, "band.html", {"request": request, "active_page": "band"})

@app.get("/theater", response_class=HTMLResponse)
def theater(request: Request):
    return templates.TemplateResponse(request, "theater.html", {"request": request, "active_page": "theater"})

@app.get("/reflection", response_class=HTMLResponse)
def reflection(request: Request):
    return templates.TemplateResponse(request, "reflection.html", {"request": request, "active_page": "reflection"})

@app.get("/contact", response_class=HTMLResponse)
def contact(request: Request):
    return templates.TemplateResponse(request, "contact.html", {"request": request, "active_page": "contact"})

# --- Hackatime --- 

# @app.get("/hackatime/id")
# def get_id(request: Request):
#     headers = {"Accept": "application/json", "Authorization": f"Bearer {cfg.hackatime_token.strip()}"}
#     response = requests.get(f"https://{cfg.hackatime_host}/api/hackatime/v1/users/{cfg.hackatime_email}", headers=headers)
#     response.raise_for_status()
#     id = response.json()
#     return id

@app.get("/hackatime/today")
def today_summary(request: Request):
    headers = {"Accept": "application/json", "Authorization": f"Bearer {cfg.hackatime_token.strip()}"}
    response = requests.get(f"https://{cfg.hackatime_host}/api/hackatime/v1/users/{cfg.hackatime_id}/statusbar/today", headers=headers)
    response.raise_for_status()
    return response.json()

@app.get("/hackatime/week")
def week_summary(request: Request):
    headers = {"Accept": "application/json", "Authorization": f"Bearer {cfg.hackatime_token.strip()}"}
    response = requests.get(f"https://{cfg.hackatime_host}/api/hackatime/v1/users/current/stats/last_7_days", headers=headers)
    response.raise_for_status()
    return response.json()

@app.get("/hackatime/stats")
def total_code_time(request: Request):
    headers = {"Accept": "application/json", "Authorization": f"Bearer {cfg.hackatime_token.strip()}"}
    response = requests.get(f"https://{cfg.hackatime_host}/api/v1/users/{cfg.hackatime_id}/stats", headers=headers)
    response.raise_for_status()
    return response.json()

# --- Google API for calender ---
@app.get("/api/calendar-status", include_in_schema=False)
def calendar_status():
    headers = {"Cache-Control": "no-store"}

    try:
        calendar_id = cfg.google_calendar_id
        timezone = ZoneInfo(cfg.calendar_timezone)

        today = datetime.now(timezone).date()
        start = datetime.combine(today, time.min, tzinfo=timezone)
        end = datetime.combine(today + timedelta(days=1), time.min, tzinfo=timezone)

        credentials = (service_account.Credentials.from_service_account_file( BASE_DIR / "google-calendar.json", scopes=["https://www.googleapis.com/auth/calendar.events.freebusy"]))

        with AuthorizedSession(credentials) as session:
            response = session.post(
                "https://www.googleapis.com/calendar/v3/freeBusy",
                json={
                    "timeMin": start.isoformat(),
                    "timeMax": end.isoformat(),
                    "timeZone": str(timezone),
                    "items": [{"id": calendar_id}]
                },
                timeout=10,
            )
            response.raise_for_status()
            result = response.json()

        calendar = result.get("calendars", {}).get(calendar_id)

        if (not isinstance(calendar, dict) or calendar.get("errors") or not isinstance(calendar.get("busy"), list)):
            print("calendar availablity cannot be read")
            return JSONResponse({"has_plans": None}, status_code=503, headers=headers)
            

        return JSONResponse(
            {
                "date": today.isoformat(),
                "has_plans": bool(calendar["busy"]),
                
            },
            headers=headers
        )

    except Exception:
        print("Calendar status lookup failed.")
        return JSONResponse(
            {"has_plans": None},
            status_code=503,
            headers=headers
        )

def calc_stats(request: Request):
    today = week_summary(request)

calc_stats(Request)
