from leetcode.graphql.base_field import BaseField
from leetcode.graphql.simple_field import SimpleField
from typing import List


class CompoundField(BaseField):
    """
    A compound field, which has a name as well as sub-fields.

    This can result in GraphQL field structures like so:
        codeSnippets {
            lang
            langSlug
            code
        }

    Each specific subtype of CompoundField will need to define its own list of
    fields that are relevant to it.
    """
    def __init__(self, name: str, fields: List[SimpleField] = None):
        """
        Initializes the compound field with a name and an optional set of sub-fields.

        :param name: the name of the field (required)
        :param fields: the list of sub-fields (optional)
        """
        self.name = name
        if fields is None:
            fields = list()
        self.fields = fields

    def get_name(self) -> str:
        """
        Gets the name of the compound field, set upon initialization.

        :return: the name of the field
        """
        return self.name

    def get_fields(self) -> List[BaseField]:
        """
        Gets the list of fields defined as sub-fields of this compound field.

        :return: a list of fields
        """
        return self.fields
