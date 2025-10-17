from pydantic import BaseModel


class CommandArguments(BaseModel):
    files: list[str]
    report: str
