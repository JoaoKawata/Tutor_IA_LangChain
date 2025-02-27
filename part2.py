import re
import json
import os
from dotenv import load_dotenv
from langgraph import Graph, Node, Edge  # Importing LangGraph
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
    if re.search(pattern, question):
        return True
    else:
        return False

# -------------------------------
# 2. Message Template
# -------------------------------
message_template = ChatPromptTemplate.from_messages([
    ("system", "Answer the following math question:"),
    ("user", "{question}")
])

# -------------------------------
# 3. Defining the Graph with LangGraph
# -------------------------------

# Creating the graph
graph = Graph()

# "Receiver" node
receiver = Node(name="Receiver", function=lambda question: {
    "question": question,
    "category": "math"
})

# "Virtual Teacher" node
virtual_teacher = Node(name="Virtual Teacher", function=lambda json_data: model.invoke({
    "question": json_data["question"]
}))

# Connecting the nodes with a data flow (Edge)
receiver_to_teacher_flow = Edge(from_node=receiver, to_node=virtual_teacher)

# Adding the nodes and edge to the graph
graph.add_node(receiver)
graph.add_node(virtual_teacher)
graph.add_edge(receiver_to_teacher_flow)

# -------------------------------
# 4. Main Execution Flow
# -------------------------------

# Receive the question from the user
question = input("Enter your math question: ")

# Validate the question
if validate_question(question):
    # Send the question to the "Receiver" node
    json_data = receiver.function(question)
    print("Data sent to the Virtual Teacher:", json.dumps(json_data, ensure_ascii=False, indent=4))

    # Send the JSON to the "Virtual Teacher" and receive the response
    answer = virtual_teacher.function(json_data)
    print(f"The answer to your question '{question}' is: {answer}")
else:
    # If the question is not valid, notify the user
    print("The question is not valid. Please ask a math question containing symbols like '+', '-', '*', '/', '='.")
