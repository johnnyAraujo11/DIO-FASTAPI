from fastapi import FastAPI
from workout_api.routers import api_router

app = FastAPI(title="Workout API")
app.include_router(api_router)

# Pode deixar direto no makefile a execução
"""
    if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="localhost", port=8000, log_level="info", reload=True)
"""
