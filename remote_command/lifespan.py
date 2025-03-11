from contextlib import asynccontextmanager

from fastapi import FastAPI
from loguru import logger
from tortoise import Tortoise

# from claude_auditlimit_python.configs import DATA_DIR
# from claude_auditlimit_python.periodic_checks.limit_sheduler import \
#     LimitScheduler
# from claude_auditlimit_python.sqlite_manager import SQLiteManager
# from claude_auditlimit_python.utils.time_zone_utils import set_cn_time_zone


async def on_startup():
    pass
    # logger.info("Starting up")
    # set_cn_time_zone()
    #
    # # Initialize SQLite database
    # logger.info("Initializing SQLite database")
    # sqlite_manager = SQLiteManager()
    # await sqlite_manager.initialize()
    # logger.info("SQLite database initialized")
    #
    # logger.info("Clients loaded")
    # await LimitScheduler.start()
    # logger.info("Scheduler started")


async def on_shutdown():
    pass
    # logger.info("Shutting down")
    # await LimitScheduler.shutdown()
    # logger.info("Scheduler stopped")
    #
    # # Close SQLite connections
    # logger.info("Closing SQLite connections")
    # await Tortoise.close_connections()
    # logger.info("SQLite connections closed")


@asynccontextmanager
async def lifespan(app: FastAPI):
    await on_startup()
    yield
    await on_shutdown()
