from enum import Enum, auto

from leetcode.graphql.compound_field import CompoundField
from leetcode.graphql.simple_field import SimpleField


class QuestionFields(SimpleField, Enum):
    """
    An enumeration of all the simple fields supported by Leetcode's GraphQL API for questions.
    """
    questionId = auto(),
    questionFrontendId = auto(),
    title = auto(),
    titleSlug = auto(),
    boundTopicId = auto(),
    content = auto(),
    translatedTitle = auto(),
    translatedContent = auto(),
    isPaidOnly = auto(),
    difficulty = auto(),
    likes = auto(),
    dislikes = auto(),
    isLiked = auto(),
    similarQuestions = auto(),
    exampleTestcases = auto(),
    companyTagStats = auto(),
    stats = auto(),
    hints = auto(),
    status = auto(),
    sampleTestCase = auto(),
    metaData = auto(),
    judgerAvailable = auto(),
    judgeType = auto(),
    mysqlSchemas = auto(),
    enableRunCode = auto(),
    enableTestMode = auto(),
    enableDebugger = auto(),
    envInfo = auto(),
    libraryUrl = auto(),
    adminUrl = auto(),
    __typename = auto()


class Contributors(CompoundField):
    """
    A compound field representing the contributors to a question.
    """
    class Field(SimpleField, Enum):
        username = auto(),
        profileUrl = auto(),
        avatarUrl = auto(),
        __typename = auto()

    def __init__(self, fields=None):
        super().__init__("contributors", fields)


class TopicTags(CompoundField):
    """
    A compound field representing topic tags associated with a question.
    """
    class Field(SimpleField, Enum):
        name = auto(),
        slug = auto(),
        translatedName = auto(),
        __typename = auto()

    def __init__(self, fields=None):
        super().__init__("topicTags", fields)


class CodeSnippets(CompoundField):
    """
    A compound field representing code snippets associated with a question.
    """
    class Field(SimpleField, Enum):
        lang = auto(),
        langSlug = auto(),
        code = auto(),
        __typename = auto()

    def __init__(self, fields=None):
        super().__init__("codeSnippets", fields)


class Solution(CompoundField):
    """
    A compound field representing the solution associated with a question.
    """
    class Field(SimpleField, Enum):
        id = auto(),
        canSeeDetail = auto(),
        paidOnly = auto(),
        hasVideoSolution = auto(),
        paidOnlyVideo = auto(),
        __typename = auto()

    def __init__(self, fields=None):
        super().__init__("solution", fields)
