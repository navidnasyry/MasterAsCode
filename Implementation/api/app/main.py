from fastapi import FastAPI
from app.api import routes_prediction, routes_health
# import nest_asyncio
import uvicorn

app = FastAPI(
    title="LSTM RUL Prediction API",
    description="API for Remaining Useful Life prediction using LSTM.",
    version="1.0.0"
)

# Include routers
app.include_router(routes_health.router, prefix="/api")
app.include_router(routes_prediction.router, prefix="/api/predict", tags=["Prediction"])

# Allow running in notebooks
# nest_asyncio.apply()

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
