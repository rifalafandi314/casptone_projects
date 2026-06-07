from typing import Dict, Any, Annotated
from pydantic import BaseModel, Field

# =========================
# COMMON TYPE
# =========================

Score = Annotated[int, Field(ge=0, le=4)]

# =========================
# REQUEST
# =========================

class PredictRequest(BaseModel):

    # Demografi
    Age: str
    Gender: str
    University: str
    Department: str
    Academic_Year: str
    CGPA: str
    Scholarship: str

    # Stress
    Q1: Score
    Q2: Score
    Q3: Score
    Q4: Score
    Q5: Score
    Q6: Score
    Q7: Score
    Q8: Score
    Q9: Score
    Q10: Score

    # Anxiety
    AQ1: Score
    AQ2: Score
    AQ3: Score
    AQ4: Score
    AQ5: Score
    AQ6: Score
    AQ7: Score

    # Depression
    DQ1: Score
    DQ2: Score
    DQ3: Score
    DQ4: Score
    DQ5: Score
    DQ6: Score
    DQ7: Score
    DQ8: Score
    DQ9: Score

    # NLP Text
    text: str

# =========================
# QUESTIONNAIRE RESPONSE
# =========================

class ConditionResult(BaseModel):
    prediction: str

class QuestionnaireResult(BaseModel):
    stress: ConditionResult
    anxiety: ConditionResult
    depression: ConditionResult

# =========================
# NLP RESPONSE
# =========================

class NLPResult(BaseModel):
    prediction: str
    confidence: float
    top2: list[Dict[str, Any]]

# =========================
# FINAL RESPONSE
# =========================

class FinalResponse(BaseModel):
    questionnaire: QuestionnaireResult
    text: NLPResult
    final_assessment: str