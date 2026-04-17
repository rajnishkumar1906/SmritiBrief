import uvicorn
import asyncio
import sys

if __name__ == "__main__":
    # Fix for Windows asyncio loop policy with asyncpg
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        print("🔧 Applied Windows asyncio loop policy.")
    
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=False,
        workers=1
    )
