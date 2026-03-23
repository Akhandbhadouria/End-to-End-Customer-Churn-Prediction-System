# schema.py
from pydantic import BaseModel

class ChurnInput(BaseModel):
    CreditScore: int
    Geography: str
    Gender: str
    Age: int
    Tenure: int
    Balance: float
    NumOfProducts: int
    HasCrCard: int
    IsActiveMember: int
    EstimatedSalary: float

class ChurnPrediction(BaseModel):
    churn_probability: float
    prediction: int