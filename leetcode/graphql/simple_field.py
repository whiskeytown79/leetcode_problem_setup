from enum import Enum

from leetcode.graphql.base_field import BaseField


class SimpleField(BaseField, Enum):
    def get_name(self) -> str:
        return self._name_
