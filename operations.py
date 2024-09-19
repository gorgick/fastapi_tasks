from sqlalchemy import select

import tables
from database import async_session
from schemas import STaskAdd

from tables import TaskOrm


class TaskOperation:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with async_session() as session:
            task_dict = data.model_dump()
            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls):
        async with async_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            return task_models

