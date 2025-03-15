# NLP Text Analyzer

## Overview

The **NLP Text Analyzer** is a project designed to showcase natural language processing (NLP) capabilities by analyzing text data. It performs tasks such as sentiment analysis, text summarization, and named entity recognition (NER) using Hugging Face's Transformers library. The project also includes a simple Flask web interface to interact with the analyzer.

## Features

- **Sentiment Analysis:** Determine whether a text expresses positive, negative, or neutral sentiment.
- **Text Summarization:** Generate concise summaries from longer texts.
- **Named Entity Recognition (NER):** Identify and categorize entities such as names, organizations, and dates.
- **Web Interface:** Interact with the analyzer through a user-friendly Flask-based web app.
- **Unit Testing:** Includes tests to ensure each component works correctly.

## Setup and Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation Steps

1. **Clone the Repository (if applicable):**

   ```bash
   git clone https://github.com/yourusername/nlp-text-analyzer.git
   cd nlp-text-analyzer

### Create a Python Virtual Environment:

bash
Copy
python3 -m venv nlp-env
source nlp-env/bin/activate  # On Windows: nlp-env\Scripts\activate

### Install Dependencies:

bash
Copy
pip install -r requirements.txt

### Usage
## Running the Core Analyzer (Command Line)
To test the core NLP functionalities (sentiment analysis, summarization, and NER), run:

bash
Copy
python src/analyzer.py
This will execute a sample analysis using predefined text and print the results to the console.

### Running the Web Interface
To start the Flask web app:

bash
Copy
python src/app.py
Open your web browser and navigate to http://127.0.0.1:5000/ to interact with the analyzer. You can input your text, choose the type of analysis, and view the results on the page.

### Testing
Unit tests are provided to verify that each function works correctly.

## Run the Unit Tests:

Make sure you’re in the project root directory and run:

bash
Copy
python -m unittest tests/test_analyzer.py
## Module Import Error Troubleshooting:

If you encounter a ModuleNotFoundError for the src module, ensure you run the tests from the project root or adjust the PYTHONPATH. For example, you can add the following snippet at the top of tests/test_analyzer.py:

python
Copy
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

