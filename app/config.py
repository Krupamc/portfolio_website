import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(usecwd=True), override=False)

# Get functions
def get_bool(name: str, default: bool = False) -> bool:
    value = os.getenv(name)

    if value is None:
        return default

    return value.strip().lower() in {"1", "true", "yes", "on"}

develop = get_bool("DEVELOP")

hackatime_token = os.getenv("HACKATIME_TOKEN", "")
hackatime_host = os.getenv("HACKATIME_HOST", "hackatime.hackclub.com")
hackatime_email=os.getenv("HACKATIME_EMAIL")
hackatime_id=os.getenv("HACKATIME_ID", 35839)
hackatime_username=os.getenv("HACKATIME_USERNAME")

google_calendar_id = os.getenv("GOOGLE_CALENDAR_ID", "")
#google_service_account_file = os.getenv("GOOGLE_SERVICE")
calendar_timezone = os.getenv("CALENDAR_TIMEZONE", "")

immich_url = os.getenv("IMMICH_URL", "")
immich_api_key = os.getenv("IMMICH_API_KEY", "")
immich_album_id = os.getenv("IMMICH_ALBUM_ID", "")

uptimerobot_api_key = os.getenv("UPTIMEROBOT_API_KEY", "")

github_user = os.getenv("GITHUB_USER", "")

if not hackatime_token:
    raise RuntimeError("Hackatime Token Missing")