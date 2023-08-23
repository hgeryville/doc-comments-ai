import pytest


@pytest.fixture
def python_code_fixture():
    return """
import os
import re
from doc_comments_ai.constants import Language


def get_programming_language(file_extension: str) -> Language:
    \"\"\"
    Returns the corresponding programming language based on the given file extension.

    Args:
        file_extension (str): The file extension of the programming file.

    Returns:
        Language: The corresponding programming language if it exists in the mapping, otherwise Language.UNKNOWN.
    \"\"\"
    language_mapping = {
        ".py": Language.PYTHON,
        ".js": Language.JAVASCRIPT,
        ".ts": Language.TYPESCRIPT,
        ".java": Language.JAVA,
        ".kt": Language.KOTLIN,
        ".lua": Language.LUA,
        # ".rs": Language.RUST,
        # ".cpp": Language.CPP,
        # ".c": Language.C,
        # ".html": Language.HTML,
        # ".css": Language.CSS,
        # ".php": Language.PHP,
        # ".rb": Language.RUBY,
        # ".go": Language.GO,
        # ".swift": Language.SWIFT,
        # ".cs": Language.C_SHARP,
        # ".m": Language.OBJECTIVE_C,
        # ".scala": Language.SCALA,
        # ".pl": Language.PERL,
        # ".r": Language.R,
    }
    return language_mapping.get(file_extension, Language.UNKNOWN)


def get_file_extension(file_name: str) -> str:
    return os.path.splitext(file_name)[-1]
    
    """
