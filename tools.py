from pathlib import Path
from collections import Counter
import re

from smolagents import Tool


def _load_text(file_path: str) -> str:
    path = Path(file_path)

    if not path.exists():
        return f"Error: File '{file_path}' not found."

    return path.read_text(encoding="utf-8")


class ReadFileTool(Tool):

    name = "read_file"

    description = (
        "Read the content of a UTF-8 text file."
    )

    inputs = {
        "file_path": {
            "type": "string",
            "description": "Path of the text file."
        }
    }

    output_type = "string"

    def forward(self, file_path: str):

        return _load_text(file_path)


class SummarizeTextTool(Tool):

    name = "summarize_text"

    description = (
        "Summarize a text document by returning its first sentences."
    )

    inputs = {
        "file_path": {
            "type": "string",
            "description": "Path of the text file."
        },
        "max_sentences": {
            "type": "integer",
            "description": "Maximum number of sentences.",
            "nullable": True
        }
    }

    output_type = "string"

    def forward(self, file_path: str, max_sentences: int = 2):

        text = _load_text(file_path)

        if text.startswith("Error"):
            return text

        sentences = re.split(
            r'(?<=[.!?])\s+',
            text.strip()
        )

        return " ".join(sentences[:max_sentences])


class SearchKeywordTool(Tool):

    name = "search_keyword"

    description = (
        "Search for a keyword in a text file."
    )

    inputs = {
        "file_path": {
            "type": "string",
            "description": "Path of the text file."
        },
        "keyword": {
            "type": "string",
            "description": "Word or phrase to search."
        }
    }

    output_type = "string"

    def forward(self, file_path: str, keyword: str):

        text = _load_text(file_path)

        if text.startswith("Error"):
            return text

        lines = text.splitlines()

        results = []

        for i, line in enumerate(lines, start=1):

            if keyword.lower() in line.lower():
                results.append(
                    f"Line {i}: {line}"
                )

        if not results:
            return f'"{keyword}" was not found.'

        return "\n".join(results)



class WordStatisticsTool(Tool):

    name = "word_statistics"

    description = (
        "Calculate word statistics for a text file."
    )

    inputs = {
        "file_path": {
            "type": "string",
            "description": "Path to the text file."
        }
    }

    output_type = "string"

    def forward(self, file_path: str):

        text = _load_text(file_path)

        if text.startswith("Error"):
            return text

        words = re.findall(r"\b\w+\b", text.lower())

        counter = Counter(words)


        result = (
            f"Characters: {len(text)}\n"
            f"Words: {len(words)}\n"
            f"Lines: {len(text.splitlines())}\n\n"
            "Top 10 Words:\n"
        )

        for word, count in counter.most_common(10):
            result += f"- {word}: {count}\n"


        return result
    
