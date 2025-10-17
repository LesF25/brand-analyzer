from pydantic import BaseModel


class AverageData(BaseModel):
    count: int = 0
    rating: float = 0.0
