from leetcode.graphql.field import Field, CodeSnippets
from leetcode.graphql.request import Request
import json
import requests

title_slug = "two-sum"

graphql_request = Request(title_slug, fields=[
            Field.questionId,
            Field.questionFrontendId,
            Field.title,
            Field.boundTopicId,
            Field.titleSlug,
            Field.content,
            CodeSnippets(fields=[
                CodeSnippets.Field.lang,
                CodeSnippets.Field.langSlug,
                CodeSnippets.Field.code
            ])
        ])

query_text = graphql_request.serialize()
query_json = json.loads(query_text)
print(json.dumps(query_json))

description_url = f"https://leetcode.com/problems/{title_slug}/description"
r = requests.get(description_url)
if r.status_code == 200:
    csrf_token_key = 'csrftoken'
    csrf_token = None
    cookies = dict()
    if csrf_token_key in r.cookies:
        csrf_token = r.cookies[csrf_token_key]
        cookies[csrf_token_key] = csrf_token
    print(cookies)
    headers = dict()
    headers["Content-Type"] = "application/json"
    headers["Referer"] = description_url
    if csrf_token is not None:
        headers["x-csrftoken"] = csrf_token
    response = requests.post('https://leetcode.com/graphql', json=query_json, cookies=cookies, headers=headers)
    if response.status_code == 200:
        print(json.dumps(response.json()))
    else:
        raise Exception("Query failed to run by returning code of {}: {}".format(response.status_code, response.content))
else:
    raise Exception("Failed cookie fetch with status code {}.".format(r.status_code))
