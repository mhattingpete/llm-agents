import uuid

from fastapi import APIRouter

from src.api_dataclasses import AnswerInput
from src.setup_agent import AgentRunner

executor = AgentRunner()


router = APIRouter(
    prefix="/answer",
    tags=["answer"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
def get_answer(
    user_input: AnswerInput,
):
    question = user_input.question
    session_id = user_input.session_id
    if not session_id:
        session_id = str(uuid.uuid4())
    response = executor.get_answer(
        question,
        session_id,
    )
    return {
        "answer": str(response["output"]).replace("<|end_of_turn|>", ""),
        "session_id": session_id,
    }
