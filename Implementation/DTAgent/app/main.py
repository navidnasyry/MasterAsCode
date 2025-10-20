from fastapi import FastAPI
from app.api import routes_engine
from app.services.engine_service import initialize_engine_states

app = FastAPI(
    title="CMAPSS Engine Control API",
    description="API to manage engine states and retrieve test data from CMAPSS dataset.",
    version="1.0.0"
)

# Include routers
app.include_router(routes_engine.router)


@app.on_event("startup")
def startup_event():
    """Initialize engine states when the app starts."""
    initialize_engine_states()
    print("✅ All engines initialized to ON.")


@app.get("/")
def root():
    return {"message": "Engine Control API is running 🚀"}
