from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse, PlainTextResponse
from pathlib import Path
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exception_handlers import http_exception_handler
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

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
    return templates.TemplateResponse(request, "home.html", {"request": request})

@app.get("/robots.txt", response_class=PlainTextResponse, include_in_schema=False)
def robots_txt():
    return """\
User-agent: *
Disallow: /users/

Allow: /
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

@app.get("/services", response_class=HTMLResponse)
def contact(request: Request):
    return templates.TemplateResponse(request, "services.html", {"request": request, "active_page": "services"})

@app.get("/homelab", response_class=HTMLResponse)
def homelab(request: Request):
    return templates.TemplateResponse(request, "homelab.html", {"request": request, "active_page": "homelab"})

@app.get("/research", response_class=HTMLResponse)
def research(request: Request):
    return templates.TemplateResponse(request, "research.html", {"request": request, "active_page": "research"})

@app.get("/band", response_class=HTMLResponse)
def band(request: Request):
    return templates.TemplateResponse(request, "band.html", {"request": request, "active_page": "band"})

@app.get("/contact", response_class=HTMLResponse)
def contact(request: Request):
    return templates.TemplateResponse(request, "contact.html", {"request": request, "active_page": "contact"})