import pandas as pd
import numpy as np
from app.core.config import TEST_DATA_PATH
from app.models.engine_state import engine_states

# Cache dataset globally to avoid reloading
_df_cache: pd.DataFrame | None = None


def load_cmapss_test_data() -> pd.DataFrame:
    """Load CMAPSS test dataset once and cache it."""
    global _df_cache
    if _df_cache is not None:
        return _df_cache

    columns = [
        "unit_number", "time_in_cycles",
        "op_setting_1", "op_setting_2", "op_setting_3"
    ] + [f"sensor_{i}" for i in range(1, 22)]

    df = pd.read_csv(TEST_DATA_PATH, sep=r"\s+", header=None, names=columns)
    _df_cache = df
    return df


def initialize_engine_states():
    """Initialize all engines to ON by default."""
    df = load_cmapss_test_data()
    engine_numbers = df["unit_number"].unique()

    for eng in engine_numbers:
        eng_id = int(eng)  # convert numpy.int64 → int
        if eng_id not in engine_states:
            engine_states[eng_id] = "ON"


def get_engine_data(engine_number: int, until_clock: int | None = None):
    """Return engine data, optionally up to a given clock."""
    df = load_cmapss_test_data()
    engine_df = df[df["unit_number"] == engine_number]

    if until_clock is not None:
        engine_df = engine_df[engine_df["time_in_cycles"] <= until_clock]

    # Convert to native Python types for FastAPI
    data = engine_df.replace({np.nan: None}).to_dict(orient="records")
    for row in data:
        for key, value in row.items():
            if isinstance(value, (np.integer, np.floating)):
                row[key] = value.item()  # Convert to Python scalar
    return data


def get_all_final_states():
    """Return all engines and their ON/OFF state (JSON-safe)."""
    result = [
        {"engine_number": int(eng), "state": str(state)}
        for eng, state in engine_states.items()
    ]
    return result


def set_engine_states(engine_list: list[int], state: str):
    """Turn ON or OFF a list of engines."""
    for eng in engine_list:
        eng_id = int(eng)
        engine_states[eng_id] = state.upper()

    return get_all_final_states()

    
def set_all_engine_states(state: str):
    """Turn all engines ON or OFF."""
    state = state.upper()
    if state not in ["ON", "OFF"]:
        raise ValueError("Invalid state. Must be 'ON' or 'OFF'.")
    
    for eng in list(engine_states.keys()):
        engine_states[int(eng)] = state
    return get_all_final_states()