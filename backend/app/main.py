from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, profile, memory
from app.core.config import settings
from app.core.database import engine, Base

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    print("🚀 Starting up... Connecting to database")
    try:
        # Create tables on startup (use migrations like Alembic for production)
        async with engine.begin() as conn:
            print("📦 Database connection established. Creating tables...")
            await conn.run_sync(Base.metadata.create_all)
        print("✅ Database tables verified/created.")
    except Exception as e:
        print(f"❌ Database startup error: {e}")
        raise e

# Include routers
app.include_router(auth.router, tags=["Authentication"])
app.include_router(profile.router, tags=["Profile"])
app.include_router(memory.router, tags=["Memory"])

@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.PROJECT_NAME} API"}
