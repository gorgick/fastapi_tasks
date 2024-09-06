from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class STask(STaskAdd):
    id: int


tasks = []


@app.post("/index")
async def add_task(task: STaskAdd):
    tasks.append(task)
    return {'tasks': True}

# @app.get("/index")
# def get_tasks():
#     task = STask(name='Do it!')
#     return {'tasks': task}
