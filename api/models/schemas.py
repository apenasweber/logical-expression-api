from typing import Any, List, Optional

from pydantic import BaseModel


class ExpressionIn(BaseModel):
    expression: str


class ExpressionOut(BaseModel):
    id = int
    expression: str
    result: Optional[Any]


class ExpressionCreate(BaseModel):
    id = int


class ExpressionListOut(BaseModel):
    expressions: List[ExpressionOut]
