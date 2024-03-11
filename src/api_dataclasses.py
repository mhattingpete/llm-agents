from pydantic import BaseModel


class AnswerInput(BaseModel):
    question: str
    session_id: str = None


class AnswerOutput(BaseModel):
    answer: str
    session_id: str
