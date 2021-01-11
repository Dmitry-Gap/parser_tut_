import os
from datetime import datetime

DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64)"
    "AppleWebKit/537.36 (KHTML, like Gecko)"
    "Chrome/87.0.4280.88 Safari/537.36"
)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
HOST = "https://news.tut.by/"
PREVIEW_URL = "{}archive/{}"
DATE = datetime.strftime(datetime.now(), "%d.%m.%Y")
