

class Request:
    """
    Initializes the request with the given title slug (e.g. "two-sum")
    """
    def __init__(self, title_slug, fields):
        self.title_slug = title_slug
        self.fields = fields

    def serialize(self) -> str:
        nl = '\\n'
        output = '{'
        output += '"operationName":"questionData",'
        output += f'"variables":{{"titleSlug":"{self.title_slug}"}},'
        query = f"query questionData($titleSlug: String\u0021) {{{nl}"
        query += f"  question(titleSlug: $titleSlug) {{{nl}"
        for field in self.fields:
            query += f"    {field.get_name()}"
            sub_fields = field.get_fields()
            if len(sub_fields) > 0:
                query += f" {{{nl}"
                for sub_field in sub_fields:
                    query += f"      {sub_field.get_name()}{nl}"
                query += f"    }}{nl}"
            query += nl
        query += f"}}{nl}}}{nl}"
        output += f'"query":"{query}"'
        output += '}'
        return output
