from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import routes_prediction, routes_health
import uvicorn

app = FastAPI(
    title="LSTM RUL Prediction API",
    description="API for Remaining Useful Life prediction using LSTM.",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development only - restrict in production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(routes_health.router, prefix="/api")
app.include_router(routes_prediction.router, prefix="/api/predict", tags=["Prediction"])

# Allow running in notebooks
# nest_asyncio.apply()

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
