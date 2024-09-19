from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

DATABASE_URL = "sqlite+aiosqlite:///tasks.db"

engine = create_async_engine(DATABASE_URL, echo=True)               # echo дает видеть sql-запрос к дб

async_session = async_sessionmaker(engine, expire_on_commit=False)