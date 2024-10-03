# PDF Splitter

A simple and efficient Python application to split multi-page PDF files into individual single-page PDFs. Each split page is saved with a filename in the format "Page {page_number}.pdf".

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)
- [Additional Enhancements](#additional-enhancements)
- [License](#license)

## Features

- **General PDF Splitting:** Split any multi-page PDF into individual pages.
- **Custom Naming Convention:** Each split page is saved as "Page {page_number}.pdf".
- **User-Friendly Interface:** Prompt-based selection of source PDF and output directory.
- **Progress Indicator:** Visual progress bar to monitor splitting process.
- **Error Handling:** Graceful handling of common errors and informative messages.

## Prerequisites

- **Python 3.6 or higher**: Ensure you have Python installed on your system.

## Installation

```bash
# Activate venv:
source venv/bin/activate

# Install Deps:
pip install -r requirements.txt

# Drag source PDF to /source folder
# Change source file name in script

# Run:
python main.py

# Deactivate venv:
deactivate
```
