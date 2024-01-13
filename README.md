# Conversational AI Chatbot with Flask

## Overview

This project is a Conversational AI chatbot implemented with microsoft/DailoGPT-large chatbots.

## Features

- **Natural Language Processing (NLP):** Utilizes state-of-the-art NLP models for understanding and generating human-like responses.
- **Flask Framework:** Leverages Flask for creating a web-based API to interact with the chatbot.
- **Customizable Responses:** Easily extend and customize the chatbot's responses based on your specific use case.

## Getting Started

### Prerequisites

- Python 3.x installed
- [Virtualenv](https://pypi.org/project/virtualenv/) (recommended)

### Installation

1. Clone the repository:

   choose directory where you want to create the project.

   Open Git Bash and execute the clone command.
   
    <i> git clone https://github.com/thedeveloper2104/bits-wilp-ai-ml-sem-3-nlpapp.git </i>

2. Navigate to the project directory:
    Open cmd prompt
3. Create a virtual environment (optional but recommended):
    virtualenv venv

4. Activate the virtual environment:

    - **Linux/Mac:**
        source venv/bin/activate

    - **Windows:**
        .\venv\Scripts\activate

5. Install the required dependencies:
    pip install -r requirements.txt
 

### Usage

1. Run the Flask application:

   python app.py

   The ChatBot will be accessible at `http://127.0.0.1:5000/`.

2. Now you can chat with Bot using Text field
   
  Bot: Hi, welcome to ChatBot! Go ahead and send me a message. 😄
  
  User: Does money buy happiness?
  
  Bot: If you're buying pizza, then yes.

  User: Okay I will buy pizza for you.
  
  Bot : You're a saint
  
## Dependencies

- Flask
- Tensorflow
- Huggingface
- python
  
