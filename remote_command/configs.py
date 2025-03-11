import os
from pathlib import Path

from httpx import Timeout

REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = int(os.environ.get("REDIS_PORT", 6379))
REDIS_DB = 2


DOCS_USERNAME = "claude-backend"
DOCS_PASSWORD = "20Wd!!!!"


# 三小时
CLAUDE_OFFICIAL_EXPIRE_TIME = 3 * 60 * 60
RATE_LIMIT = (
    180 * 10000
)  # 6w tokens for 3 hours # token limit for the 3 hours  # Configure this value as needed

USAGE_RECORD_RATE_LIMIT = 45
DEFAULT_TOKENIZER = "cl100k_base"


# limits check的函数
CLAUDE_CLIENT_LIMIT_CHECKS_INTERVAL_MINUTES = 60


# IP访问的限制
IP_REQUEST_LIMIT_PER_MINUTE = 40  # 一分钟40次

# ROOT path
ROOT = Path(__file__).parent.parent

DATA_DIR = ROOT / "data"

LOGS_PATH = ROOT / "logs"

SQLITE_DB_PATH = DATA_DIR / "sqlite_db"
SQLITE_DB_PATH.mkdir(exist_ok=True, parents=True)
DB_PATH = SQLITE_DB_PATH / "db.sqlite3"
DB_URL = f"sqlite://{DB_PATH}"

MAX_DEVICES = 3

LOGS_PATH.mkdir(exist_ok=True)

if __name__ == "__main__":
    print(ROOT)
