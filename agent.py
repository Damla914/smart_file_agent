import os
from dotenv import load_dotenv
from smolagents import CodeAgent, InferenceClientModel

from tools import (
    ReadFileTool,
    SummarizeTextTool,
    SearchKeywordTool,
    WordStatisticsTool,
)

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

model = InferenceClientModel(
    model_id="Qwen/Qwen2.5-7B-Instruct",
    token=HF_TOKEN,
)

agent = CodeAgent(
    model=model,
    tools=[
        ReadFileTool(),
        SummarizeTextTool(),
        SearchKeywordTool(),
        WordStatisticsTool(),
    ],
)

