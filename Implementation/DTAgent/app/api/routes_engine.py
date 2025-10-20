from fastapi import APIRouter, Query
from typing import Optional, List
from app.services.engine_service import (
    get_engine_data,
    get_all_final_states,
    set_engine_states
)

router = APIRouter(prefix="/engines", tags=["Engines"])

@router.get("/{engine_number}")
def get_engine(engine_number: int, until_clock: Optional[int] = Query(None)):
    """
    Get all data for a specific engine.
    Optionally provide `until_clock` to get data up to that time step.
    """
    data = get_engine_data(engine_number, until_clock)
    return {"engine_number": engine_number, "records": data}

@router.get("/states/all")
def get_final_states():
    """Get the ON/OFF state of all engines"""
    return {"states": get_all_final_states()}

@router.post("/states/set")
def set_states(engine_list: List[int], state: str):
    """
    Turn ON/OFF a list of engines.
    Example:
      POST /engines/states/set?state=OFF
      Body: [1, 3, 5]
    """
    if state.upper() not in ["ON", "OFF"]:
        return {"error": "Invalid state. Must be 'ON' or 'OFF'."}
    updated_states = set_engine_states(engine_list, state)
    return {"updated_states": updated_states}
