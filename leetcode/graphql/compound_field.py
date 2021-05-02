from leetcode.graphql.base_field import BaseField
from leetcode.graphql.simple_field import SimpleField
from typing import List


class CompoundField(BaseField):
    def __init__(self, name: str, fields: List[SimpleField] = None):
        self.name = name
        if fields is None:
            fields = list()
        self.fields = fields

    def get_name(self) -> str:
        return self.name

    def get_fields(self) -> List[BaseField]:
        return self.fields
