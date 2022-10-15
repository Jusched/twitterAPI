from fastapi import HTTPException, status
import json

def load_data(type, mode):
    with open(f"db/{type}.json", f"{mode}", encoding="utf-8") as f:
        results = json.load(f)
        return results,

def save_data(results, f):
    f.seek(0)
    json.dump(results, f, default=str, indent=4)


def http_404(exception):
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"{exception}"
    )