from __future__ import annotations # To allow self-referential type hinting pre python 3.10
from typing import List


class BaseField:
    def get_name(self) -> str:
        return ""

    def get_fields(self) -> List[BaseField]:
        return list()
