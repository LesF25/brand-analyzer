from typing import Annotated, Union

from pydantic import Field

from .csv_adapter import CsvReader


AdapterUnion = Annotated[
    Union[
        CsvReader,
    ],
    Field(discriminator='type')
]
