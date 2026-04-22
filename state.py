from typing import TypedDict, List

class CareerState(TypedDict):
    question: str
    messages: List[str]
    route: str
    retrieved: str
    sources: List[str]
    tool_result: str
    answer: str
    faithfulness: float
    eval_retries: int
    user_name: str
    user_skills: List[str]