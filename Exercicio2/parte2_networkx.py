import re
import json
import networkx as nx
from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Load the API key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Initializing the Groq language model
model = init_chat_model("llama3-70b-8192", model_provider="groq")
parser = StrOutputParser()

# -------------------------------
# 1. Question Validation
# -------------------------------
def validate_question(question):
    pattern = r"[+\-*/=x]"
    if re.search(pattern, question):
        return True
    else:
        return False

# -------------------------------
# 2. Integration with the Virtual Teacher
# -------------------------------

message_template = ChatPromptTemplate.from_messages([
    ("system", "Answer the following math question:"),
    ("user", "{question}")
])

chain = message_template | model | parser

# -------------------------------
# 3. Creating the Graph with NetworkX
# -------------------------------
def create_graph():
    G = nx.DiGraph()  # Directed graph
    G.add_node("Receiver")  # Adding the Receiver as a node
    G.add_node("Virtual Teacher")  # Adding the Virtual Teacher as a node
    G.add_edge("Receiver", "Virtual Teacher")  # Creating the relationship between the two
    return G

# -------------------------------
# Main Execution Flow
# -------------------------------
def run_flow():
    # Create the graph
    G = create_graph()

    # Receive the question
    question = input("Enter your math question: ")

    # Validate the question
    if validate_question(question):
        # Structure the communication in JSON format
        json_data = {
            "question": question,
            "category": "math"
        }

        # Display the graph and data
        print(f"Current graph: {G.nodes()}")  # Shows the graph's nodes
        print(f"Data sent to the Virtual Teacher: {json.dumps(json_data, ensure_ascii=False, indent=4)}")

        # Send the question to the Virtual Teacher
        text = chain.invoke({"question": question})
        print(f"The answer to your question '{question}' is: {text}")
    else:
        print("The question is not valid. Please ask a math question containing symbols like '+', '-', '*', '/', '='.")

# Call the function
run_flow()
