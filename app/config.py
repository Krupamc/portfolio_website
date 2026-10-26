import os
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

if not hackatime_token:
    raise RuntimeError("Hackatime Token Missing")