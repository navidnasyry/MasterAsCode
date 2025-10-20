from typing import Dict

# Simple in-memory store (could be replaced with Redis or DB later)
engine_states: Dict[int, str] = {}  # {engine_number: "ON" or "OFF"}
