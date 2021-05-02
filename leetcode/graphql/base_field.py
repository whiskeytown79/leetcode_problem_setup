from __future__ import annotations # To allow self-referential type hinting pre python 3.10
from typing import List


class BaseField:
    """
    The base type for all fields to be used in assembling GraphQL queries.
    """
    def get_name(self) -> str:
        """
        Gets the name of this field. Overridden in subtypes, the base implementation returns an empty string.

        :return: an empty string
        """
        return ""

    def get_fields(self) -> List[BaseField]:
        """
        Gets the list of sub-fields of this field. Subtypes may override this to provide a non-empty list.

        :return: an empty list
        """
        return list()
