from enum import Enum

from leetcode.graphql.base_field import BaseField


class SimpleField(BaseField, Enum):
    """
    A simple field that has no sub-fields, just a name.
    """
    def get_name(self) -> str:
        """
        Gets the name of the simple field, taken from the enum member name.

        :return: the name of the field
        """
        return self._name_
