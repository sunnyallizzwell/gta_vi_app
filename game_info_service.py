# game_info_service.py
# Requires: pip install fastapi uvicorn pydantic

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="GTA 6 Game Info Service", version="1.0.0")

# --- Models ---
class Feature(BaseModel):
    id: int
    title: str
    description: str
    category: str

# --- Mock Database ---
# In production, this would be swapped out for a connection to a database
MOCK_DB = [
    Feature(id=1, title="Vice City Returns", description="Set in the sprawling state of Leonida.", category="World"),
    Feature(id=2, title="Dual Protagonists", description="Play as Jason and Lucia.", category="Characters"),
]

# --- Endpoints ---
@app.get("/api/v1/info/features", response_model=List[Feature])
async def get_all_features(category: Optional[str] = None):
    """Retrieve game features, optionally filtered by category."""
    if category:
        filtered = [f for f in MOCK_DB if f.category.lower() == category.lower()]
        if not filtered:
            raise HTTPException(status_code=404, detail="No features found for this category.")
        return filtered
    return MOCK_DB

@app.get("/api/v1/info/features/{feature_id}", response_model=Feature)
async def get_feature_by_id(feature_id: int):
    """Retrieve a specific feature by its ID."""
    for feature in MOCK_DB:
        if feature.id == feature_id:
            return feature
    raise HTTPException(status_code=404, detail="Feature not found.")

if __name__ == "__main__":
    import uvicorn
    # Running on port 8001 to keep it separate from other microservices
    uvicorn.run(app, host="0.0.0.0", port=8001)