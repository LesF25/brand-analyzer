from pathlib import Path
from typing import Literal

from pydantic import BaseModel, field_validator


class File(BaseModel):
    file_name: str

    @field_validator('file_name', mode='after')
    @classmethod
    def validate_file_type(
        cls,
        file_name: str,
    ) -> str:
        if Path(file_name).suffix != '.csv':
            raise ValueError(
                'The command only supports working with CSV files.'
            )

        return file_name


class CommandArguments(BaseModel):
    files: list[File]
    report: Literal['average-rating']

    @field_validator('files', mode='before')
    @classmethod
    def _validate_files(cls, files: list[str]) -> list[File]:
        return [
            File(file_name=file_name)
            for file_name in files
        ]


class AverageData(BaseModel):
    count: int = 0
    rating: float = 0.0
