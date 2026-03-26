# Website Summarizer using Local LLMs

This project implements an end-to-end pipeline that extracts content from a webpage and generates a concise summary using a locally hosted large language model via Ollama.

## Overview

The system combines web scraping and language model capabilities to convert unstructured webpage content into a readable summary. It is designed to work with dynamic websites where content is rendered using JavaScript.

## Features

* Extracts visible text from webpages using Selenium
* Handles dynamically loaded content
* Summarizes extracted text using a local LLM
* Uses OpenAI-compatible API interface with Ollama
* Modular design with separate scraping and summarization components

## Architecture

Input URL
→ Selenium-based content extraction
→ Text preprocessing and truncation
→ LLM-based summarization (Ollama)
→ Output summary

## Project Structure

projects/04_website_summarizer

scraper.py
Handles webpage loading and text extraction

summarizer.py
Interacts with the local LLM to generate summaries

main.py
Entry point that connects scraping and summarization

## Tech Stack

Python
Selenium
Ollama (local LLM)
OpenAI-compatible API

## Setup Instructions

1. Install Ollama and start the server
   ollama serve

2. Pull a model
   ollama pull llama3

3. Install dependencies
   uv add selenium openai

4. Run the application
   uv run main.py https://example.com

Alternatively, modify main.py to accept user input via prompt.

## Key Design Decisions

* Local LLM usage ensures privacy and no API cost
* Modular structure improves maintainability and extensibility
* Input truncation prevents model overload and ensures performance
* Selenium is used to handle JavaScript-rendered content

## Limitations

* Extracted text may include navigation or irrelevant content
* Performance depends on system resources due to local model usage
* Very large pages require truncation

## Future Improvements

* Clean HTML extraction using parsing libraries
* Multi-page summarization support
* Integration with vector databases for retrieval-based summarization
* User interface for interactive usage
* Domain-specific summarization enhancements

## Motivation

This project is part of a broader effort to build practical LLM-based systems that integrate real-world data sources with AI-driven processing.

## Contributions

This is a personal project. Feedback and suggestions are welcome.
