from fastapi import APIRouter, Query
from typing import Optional, List
from app.services.engine_service import (
    get_engine_data,
    get_all_final_states,
    set_engine_states,
    set_all_engine_states
)

router = APIRouter(prefix="/engines", tags=["Engines"])


# =========================================================
# Get engine data
# =========================================================
# ▶ Example:
# curl -X GET "http://localhost:8001/engines/data/1"
# curl -X GET "http://localhost:8001/engines/data/1?clock=50"
@router.get("/{engine_number}")
def get_engine(engine_number: int, until_clock: Optional[int] = Query(None)):
    """
    Get all data for a specific engine.
    Optionally provide `until_clock` to get data up to that time step.
    """
    data = get_engine_data(engine_number, until_clock)
    return {"engine_number": engine_number, "records": data}


# =========================================================
#  Turn ON/OFF a list of engines
# =========================================================
# ▶ Example:
# curl -X POST "http://localhost:8001/engines/states/set?state=OFF" \
#      -H "Content-Type: application/json" \
#      -d "[1, 3, 5]"
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



# =========================================================
# Turn ON/OFF all engines
# =========================================================
# ▶ Example:
# curl -X POST "http://localhost:8001/engines/states/set_all?state=OFF"
# curl -X POST "http://localhost:8001/engines/states/set_all?state=ON"
@router.post("/states/set_all")
def set_all_states(state: str):
    """
    Turn all engines ON or OFF.
    Example:
      POST /engines/states/set_all?state=OFF
    """
    try:
        updated_states = set_all_engine_states(state)
        return {"updated_states": updated_states}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))