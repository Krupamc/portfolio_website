from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from pathlib import Path
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exception_handlers import http_exception_handler
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Start server: uvicorn main:app --reload

app = FastAPI(title="SBB Mesonet Notification System")#, lifespan=lifespan)

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

@app.get("/services", response_class=HTMLResponse)
def contact(request: Request):
    return templates.TemplateResponse(request, "services.html", {"request": request, "active_page": "services"})

@app.get("/homelab", response_class=HTMLResponse)
def homelab(request: Request):
    return templates.TemplateResponse(request, "homelab.html", {"request": request, "active_page": "homelab"})

@app.get("/contact", response_class=HTMLResponse)
def contact(request: Request):
    return templates.TemplateResponse(request, "contact.html", {"request": request, "active_page": "contact"})