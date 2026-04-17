from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, profile, memory
from app.core.config import settings
from app.core.database import engine, Base
from app.models import user # Ensure models are registered with Base.metadata

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
        import traceback
        print(f"⚠️ Database connection failed: {e}")
        traceback.print_exc()
        print("💡 Server will start, but database-related features will fail.")

# Include routers
app.include_router(auth.router, tags=["Authentication"])
app.include_router(profile.router, tags=["Profile"])
app.include_router(memory.router, tags=["Memory"])

@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.PROJECT_NAME} API"}

@app.get("/health")
async def health_check():
    from sqlalchemy import text
    from app.core.database import async_session
    
    health_status = {"status": "ok", "database": "unknown"}
    try:
        async with async_session() as session:
            await session.execute(text("SELECT 1"))
        health_status["database"] = "connected"
    except Exception as e:
        health_status["database"] = "failed"
        health_status["error"] = str(e)
    return health_status
