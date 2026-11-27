from dotenv import load_dotenv, find_dotenv
import config as cfg
# Developer mode (allows env variables in desktop)
if cfg.develop == True:
    load_dotenv(find_dotenv(), override=False)

from pathlib import Path
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse, Response, PlainTextResponse, JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exception_handlers import http_exception_handler
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from datetime import datetime, time, timedelta
from time import monotonic
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

# Immich Cache
_gallery_cache = {
    "expires": 0,
    "asset_ids": []
}

# Uptimerobot cache
_uptime_cache = {
    "expires": 0,
    "services": None
}

# For any http error, send them to a specific error page
@app.exception_handler(StarletteHTTPException)
async def not_found(request: Request, exc: StarletteHTTPException):
    # HTTP Errors
    if exc.status_code == 404:
        return templates.TemplateResponse(request, "404.html", {"request": request, "title": "404", "detail": exc.detail}, exc.status_code)
    
    return await http_exception_handler(request, exc)

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    today = today_summary(request)
    week = week_summary(request)
    all = total_code_time(request)
    uptime = get_uptime_status()
    return templates.TemplateResponse(request, "home.html", {"request": request, "today": today["data"], "week": week["data"], "all": all["data"], "uptime": uptime})

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

Disallow: /api/
Disallow: /hackatime/

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
def services(request: Request):
    return templates.TemplateResponse(request, "services.html", {"request": request, "active_page": "services"})

@app.get("/homelab", response_class=HTMLResponse)
def homelab(request: Request):
    return templates.TemplateResponse(request, "homelab.html", {"request": request, "active_page": "homelab"})

@app.get("/specs", response_class=HTMLResponse)
def specs(request: Request):
    return templates.TemplateResponse(request, "specs.html", {"request": request, "active_page": "specs"})

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

# ---Immich Background---
# Get asset ids
def get_gallery_asset_ids():
    if monotonic() < _gallery_cache["expires"]:
        return _gallery_cache["asset_ids"]

    try:
        response = requests.post(
            f"{cfg.immich_url}/api/search/metadata",
            headers={"x-api-key": cfg.immich_api_key.strip(),},
            json={
                "albumIds": [cfg.immich_album_id],
                "type": "IMAGE",
                #"size": 100,
                "withExif": False,
                "withPeople": False,
            },
            timeout=10,
        )

        response.raise_for_status()
        data = response.json()

        assets = data["assets"]["items"]
        if not isinstance(assets, list):
            raise ValueError("Unexpected asset list.")

        asset_ids = [
            asset["id"]
            for asset in assets
            if asset.get("type") == "IMAGE"
        ]

        _gallery_cache["asset_ids"] = asset_ids
        _gallery_cache["expires"] = monotonic() + 86400 # 24hrs

        return asset_ids

    except requests.HTTPError as exc:
        raise HTTPException(status_code=503, detail=(f"Immich photo search failed: HTTP {exc.response.status_code}"))

    except requests.RequestException:
        raise HTTPException(status_code=503, detail="Could not connect to Immich.")

    except (ValueError, KeyError, TypeError):
        raise HTTPException(status_code=503, detail="Immich returned an unexpected photo-search response.")

@app.get("/api/gallery", include_in_schema=False)
def gallery_photos():
    return {
        "photos": [
            {"url": f"/api/gallery/{asset_id}/images"}
            for asset_id in get_gallery_asset_ids()
        ]
    }

# Do not public requiest images
@app.get("/api/gallery/{asset_id}/images", include_in_schema=False)
def gallery_image(asset_id: str):
    if asset_id not in get_gallery_asset_ids():
        raise HTTPException(status_code=404, detail="Photo not Found.")

    try:
        response = requests.get(
            f"{cfg.immich_url}/api/assets/{asset_id}/thumbnail",
            headers={
                "x-api-key": cfg.immich_api_key,
            },
            timeout=15,
        )
        response.raise_for_status()

        content_type = response.headers.get("Content-Type", "").split(";")[0].lower()
        if not content_type.startswith("image/"):
            raise ValueError("Unexpected image response.")

        return Response(content=response.content, media_type=content_type, headers={"Cache-Controls": "public, max-age=86400"})

    except (requests.RequestException, ValueError, KeyError):
        raise HTTPException(status_code=503, detail="Photo is currently unavailable.")

# Homelab status api

# Count the statuses in the monitors
def count_statuses(monitors):
    names = {
        "UP": "up",
        "LOOKS_DOWN": "looks_down",
        "DOWN": "down",
        "PAUSED": "paused",
        "STARTED": "pending"
    }
    counts = {"up": 0, "looks_down": 0, "down": 0, "paused": 0, "pending": 0, "unknown": 0}

    for monitor in monitors:
        key = names.get(str(monitor.get("status", "")).upper(), "unknown")
        counts[key] +=1

    return counts

def get_uptime_status():
    if monotonic() < _uptime_cache["expires"]:
        if monotonic() < _uptime_cache["expires"]:
            return _uptime_cache["services"]

    # Back off after a failure (cuz rate limit)
    _uptime_cache["expires"] = monotonic() + 60

    try:
        response = requests.get("https://api.uptimerobot.com/v3/monitors", headers={"Authorization": f"Bearer {cfg.uptimerobot_api_key}"}, params={"limit": 100}, timeout=5)
        response.raise_for_status()
        
        monitors = response.json()["data"]
        
    except (requests.RequestException, ValueError, KeyError):
        return _uptime_cache["services"]  # last good result, or None

    counts = count_statuses(monitors)
    checked = counts["up"] + counts["looks_down"] + counts["down"]

    result = {
        "total": len(monitors),
        **counts,
        "percent_down": round(counts["down"] / checked * 100, 1) if checked else None,
    }

    _uptime_cache["services"] = result
    _uptime_cache["expires"] = monotonic() + 60 # 1m

    print(result)
    return result

# docs version
@app.get("/api/homelab/status", include_in_schema=False)
def homelab_status_api():
    status = get_uptime_status()
    if status is None:
        return JSONResponse({"detail": "Status temporarily unavailable"}, status_code=503)
    return status

# Github Rest API
@app.get("/api/github/latest")
def get_latest_github_event(request: Request):
    response = requests.get(f"https://api.github.com/users/{cfg.github_user}/events/public", timeout=5)
    response.raise_for_status()
    
    record = 
    return(response.json())

# def calc_stats(request: Request):
#     today = week_summary(request)

# calc_stats(Request)
