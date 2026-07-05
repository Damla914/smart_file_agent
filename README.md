# Smart File Agent

A lightweight AI agent built with **smolagents** that can analyze text documents using multiple tools.

## Features

- Read the content of text files
- Summarize text documents
- Search for keywords
- Generate document statistics

## Technologies

- Python
- smolagents
- Hugging Face Inference API

## Project Structure

```
smart-file-agent/
│
├── agent.py
├── main.py
├── tools.py
├── requirements.txt
├── README.md
├── .env
│
└── sample_files/
    ├── notes.txt
    └── report.txt
```

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/smart-file-agent.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
HF_TOKEN=your_huggingface_token
```

Run the project:

```bash
python main.py
```

## Example Commands

```text
Read sample_files/report.txt
```

```text
Summarize sample_files/report.txt
```

```text
Search for Python in sample_files/report.txt
```

```text
Show statistics for sample_files/report.txt
```

## Sample Output

```
> Search for Python in sample_files/report.txt

Line 3:
Python is widely used for data science, machine learning and automation.
```

## License

MIT License
