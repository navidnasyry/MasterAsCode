import json
from pathlib import Path

p = Path(r"f:/University/IUT_Master/Project/MasterAsCode/MasterAsCode/Implementation/jupyter-notebook/main_lstm_1.ipynb")
nb = json.loads(p.read_text(encoding="utf-8"))

# describe output from cell 12
# heatmap cell 17
# train_df.head cell 22
# lstm preprocessing prints in cell 24

def dump_outputs(cell_idx, max_chars=8000):
    c = nb["cells"][cell_idx]
    texts = []
    for o in c.get("outputs", []):
        if o.get("output_type") == "stream":
            texts.append("".join(o.get("text", [])))
        elif o.get("output_type") in ("execute_result", "display_data"):
            data = o.get("data", {})
            if "text/plain" in data:
                t = data["text/plain"]
                texts.append("".join(t) if isinstance(t, list) else t)
    blob = "\n---\n".join(texts)
    return blob[:max_chars]

parts = []
for i in [9, 12, 16, 22, 24, 43, 44]:
    parts.append("=" * 70)
    parts.append(f"OUTPUT CELL {i}")
    parts.append("=" * 70)
    parts.append(dump_outputs(i, 12000))
    parts.append("")

Path("_eda_outputs.txt").write_text("\n".join(parts), encoding="utf-8")
print("ok")
