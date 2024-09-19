from fastapi import APIRouter

from operations import TaskOperation
from schemas import STaskAdd

tasks = []

router = APIRouter(
    prefix="/tasks",
)


@router.post("")
async def add_task(
        task: STaskAdd
):
    task_id = await TaskOperation.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks():
    tasks = await TaskOperation.find_all()
    return {"data": tasks}

