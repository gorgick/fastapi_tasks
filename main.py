from contextlib import asynccontextmanager

from fastapi import FastAPI

from tables import delete_tables, create_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # await delete_tables()
    print('clear')
    await create_tables()
    print('ready')
    yield
    print('out')


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
