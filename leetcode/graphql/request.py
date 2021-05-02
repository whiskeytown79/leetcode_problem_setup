

class Request:
    """
    Initializes the request with the given title slug (e.g. "two-sum")
    """
    def __init__(self, title_slug, fields):
        self.title_slug = title_slug
        self.fields = fields

    # curl 'https://leetcode.com/graphql' \
    #   -H 'authority: leetcode.com' \
    #   -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"' \
    #   -H 'x-newrelic-id: UAQDVFVRGwEAXVlbBAg=' \
    #   -H 'dnt: 1' \
    #   -H 'sec-ch-ua-mobile: ?0' \
    #   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36' \
    #   -H 'content-type: application/json' \
    #   -H 'accept: */*' \
    #   -H 'x-csrftoken: H4pZGMTbCgJOlFHO7mkbR36eHFSVrmDN0kwNNaX9ROGG4TXuZ6PcRkXYtvKStYeO' \
    #   -H 'origin: https://leetcode.com' \
    #   -H 'sec-fetch-site: same-origin' \
    #   -H 'sec-fetch-mode: cors' \
    #   -H 'sec-fetch-dest: empty' \
    #   -H 'referer: https://leetcode.com/problems/two-sum/' \
    #   -H 'accept-language: en-US,en;q=0.9' \
    #   -H 'cookie: _ga=GA1.2.1024576238.1613190828; csrftoken=H4pZGMTbCgJOlFHO7mkbR36eHFSVrmDN0kwNNaX9ROGG4TXuZ6PcRkXYtvKStYeO; messages="06aae3d2f7e5831ffd6e4870f06174b2b08ca9b0$[[\"__json_message\"\0540\05420\054\"Confirmation e-mail sent to cohen.jacob@gmail.com.\"]\054[\"__json_message\"\0540\05425\054\"Successfully signed in as whiskeytown79.\"]\054[\"__json_message\"\0540\05425\054\"You have confirmed cohen.jacob@gmail.com.\"]]"; __stripe_mid=82e985d1-ae32-47e0-aef8-d63c18b21c83199ca0; __atuvc=3%7C10%2C2%7C11%2C9%7C12%2C0%7C13%2C4%7C14; __cfduid=d0e8c371cb7169694a154dad1e01a804d1618384658; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X3ZlcmlmaWVkX2VtYWlsIjpudWxsLCJhY2NvdW50X3VzZXIiOiIyY25yOSIsIl9hdXRoX3VzZXJfaWQiOiIzOTQ5ODkzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiYWxsYXV0aC5hY2NvdW50LmF1dGhfYmFja2VuZHMuQXV0aGVudGljYXRpb25CYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzg0MWJiZWZkZTBiOGYxNjE2ZGM2Zjk4NDY1ODE1ZTU3MGQ3MDU4ZSIsImlkIjozOTQ5ODkzLCJlbWFpbCI6ImNvaGVuLmphY29iQGdtYWlsLmNvbSIsInVzZXJuYW1lIjoid2hpc2tleXRvd243OSIsInVzZXJfc2x1ZyI6IndoaXNrZXl0b3duNzkiLCJhdmF0YXIiOiJodHRwczovL3d3dy5ncmF2YXRhci5jb20vYXZhdGFyL2UxZjVjN2FlYmE4ZmEyMTUzNGMyZDgxOWY4ZDM4MzQyLnBuZz9zPTIwMCIsInJlZnJlc2hlZF9hdCI6MTYxOTc0MzY3OSwiaXAiOiIyNjAwOjM4Nzo0OjgwMzo6NzYiLCJpZGVudGl0eSI6Ijg0ZWRhOGM5Y2YyMTNmYWJmNjQ2ZGI1Y2VkMGIyNjAxIiwic2Vzc2lvbl9pZCI6NjcyNzg5NX0.pHAxqx5C-OPPfzpqtEDCTxXcgDek3SZ-qqzD1M95Gsk; _gid=GA1.2.547093520.1619743680; __cf_bm=cb30f0f8c79ea387d6b35a594c25777eeca2b957-1619746303-1800-Afa+ClqhAmhx64f3I+JQ4yvuf4WcoWnDHYNmrfqxOsjTqhGvvVd72L8CQ6hse+TDGKvYlFzvaIea9kGnJMKXclc=; _gat=1; c_a_u="d2hpc2tleXRvd243OQ==:1lcI0Y:TipfOvBw9g62RkC2gytbZlj64QQ"' \
    #   --data-raw $'{"operationName":"questionData","variables":{"titleSlug":"two-sum"},"query":"query questionData($titleSlug: String\u0021) {\\n  question(titleSlug: $titleSlug) {\\n    questionId\\n    questionFrontendId\\n    boundTopicId\\n    title\\n    titleSlug\\n    content\\n    translatedTitle\\n    translatedContent\\n    isPaidOnly\\n    difficulty\\n    likes\\n    dislikes\\n    isLiked\\n    similarQuestions\\n    exampleTestcases\\n    contributors {\\n      username\\n      profileUrl\\n      avatarUrl\\n      __typename\\n    }\\n    topicTags {\\n      name\\n      slug\\n      translatedName\\n      __typename\\n    }\\n    companyTagStats\\n    codeSnippets {\\n      lang\\n      langSlug\\n      code\\n      __typename\\n    }\\n    stats\\n    hints\\n    solution {\\n      id\\n      canSeeDetail\\n      paidOnly\\n      hasVideoSolution\\n      paidOnlyVideo\\n      __typename\\n    }\\n    status\\n    sampleTestCase\\n    metaData\\n    judgerAvailable\\n    judgeType\\n    mysqlSchemas\\n    enableRunCode\\n    enableTestMode\\n    enableDebugger\\n    envInfo\\n    libraryUrl\\n    adminUrl\\n    __typename\\n  }\\n}\\n"}' \
    #   --compressed

    def serialize(self):
        nl = '\\n'
        output = '{'
        output += '"operationName":"questionData",'
        output += f'"variables":{{"titleSlug":"{self.title_slug}"}},'
        query = f"query questionData($titleSlug: String\u0021) {{{nl}"
        query += f"  question(titleSlug: $titleSlug) {{{nl}"
        for field in self.fields:
            query += f"    {field.get_name()}"
            sub_fields = field.get_fields()
            if sub_fields is not None:
                query += f" {{{nl}"
                for sub_field in sub_fields:
                    query += f"      {sub_field.get_name()}{nl}"
                query += f"    }}{nl}"
            query += nl
        query += f"}}{nl}}}{nl}"
        output += f'"query":"{query}"'
        output += '}'
        return output
