from pathlib import Path

file_path = Path(__file__).resolve().parents[2] / "DEMO" / "records.txt"

with open(file_path, "r") as f:
    print(f.read())
