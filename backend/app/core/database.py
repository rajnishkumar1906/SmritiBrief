from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from .config import settings

# Strip query parameters from URL for asyncpg compatibility
db_url = settings.DATABASE_URL
if "?" in db_url:
    db_url = db_url.split("?")[0]

# Debug print (hiding password)
from urllib.parse import urlparse
parsed = urlparse(db_url)
print(f"🔗 Connecting to database at: {parsed.scheme}://{parsed.hostname}{parsed.path}")

engine = create_async_engine(
    db_url, 
    connect_args={
        "ssl": "require",
        "statement_cache_size": 0,
    },
    pool_pre_ping=True,
    echo=True
)
async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

class Base(DeclarativeBase):
    pass

async def get_db():
    async with async_session() as session:
        yield session
