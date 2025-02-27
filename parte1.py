# Regular expressions in Python
import re
# Used to work with data in JSON format
import json
# Used to load variables from .env
from dotenv import load_dotenv
# Allows interaction with the operating system
import os
# Part of LangChain
# init_chat_model: Initializes a language model
# StrOutputParser: Used to process the model's output, ensuring the returned text is in the correct format.
# ChatPromptTemplate: Helps create prompts (messages) to interact with language models.
# SystemMessage and HumanMessage: Used to define how system and user messages will be structured in the interaction flow with the model.
from langchain_core.messages import SystemMessage, HumanMessage
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Load the API key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Initializing the virtual teacher model (LangChain)
model = init_chat_model("llama3-70b-8192", model_provider="groq")
parser = StrOutputParser()

# -------------------------------
# 1. Question Validation
# -------------------------------
def validate_question(question):
    # Regular expression to check if the question contains mathematical symbols
    pattern = r"[+\-*/=x]"
    # Checks if the pattern exists within the question
    if re.search(pattern, question):
        return True
    else:
        return False

# -------------------------------
# 2. Integration with the Virtual Teacher
# -------------------------------

# Template that will be used as a virtual teacher
message_template = ChatPromptTemplate.from_messages([
    ("system", "Answer the following math question:"),
    ("user", "{question}")
])

# Defining the execution chain (pipeline)
chain = message_template | model | parser

# -------------------------------
# Main Execution Flow
# -------------------------------

# Receive the question from the user
question = input("Enter your math question: ")

# Validate the question
if validate_question(question):
    # Structure the communication in JSON format
    json_data = {
        "question": question,
        "category": "math"
    }
    
    # Display the JSON (ensure_ascii=False is used for special characters)
    print("Data sent to the Virtual Teacher:", json.dumps(json_data, ensure_ascii=False, indent=4))

    # Send the JSON to the virtual teacher
    text = chain.invoke({"question": question})
    print(f"The answer to your question '{question}' is: {text}")
else:
    # If the question is not valid, notify the user
    print("The question is not valid. Please ask a math question containing symbols like '+', '-', '*', '/', '='.")
