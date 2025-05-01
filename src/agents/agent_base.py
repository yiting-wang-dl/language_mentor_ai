import json
from abc import ABC, abstractmethod

from langchain_ollama.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage
from langchain_core.runnables.history import RunnableWithMessageHistory

from .session_history import get_session_history
from utils.logger import LOG

class AgentBase(ABC):
    """
    Abstract base class providing common functionality for agents.
    """
    #TODO: Add UserID to session_id
    def __init__(self, name, prompt_file, intro_file=None, session_id=None):
        self.name = name
        self.prompt_file = prompt_file

        self.intro_file = intro_file
        self.session_id = session_id if session_id else self.name
        self.prompt = self.load_prompt()
        self.intro_messages = self.load_intro() if self.intro_file else []
        self.create_chatbot()
        
    def load_prompt(self):
        """
        Load system prompt from a file.
        """
        try:
            with open(self.prompt_file, 'r', encoding='utf-8') as f:
                return f.read().strip()
                # self.prompt = f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Prompt file {self.prompt_file} not found!")

    def load_intro(self):
        """
        Load initial messages from a JSON file.
        """
        try:
            with open(self.intro_file, 'r', encoding='utf-8') as f:
                return json.load(f)
                # self.intro = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Intro messages file {self.intro_file} not found!")
        except json.JSONDecodeError:
            raise ValueError(f"Intro messages file {self.intro_file} contains invalid JSON!")

    def create_chatbot(self):
        """
        Initialize the chatbot with system prompt and message history.
        """
        # Create chat prompt template including system prompt and message placeholder
        chat_prompt_template = ChatPromptTemplate.from_messages([
            ("system", self.prompt),
            MessagesPlaceholder(variable_name="messages"),  # Message placeholder
        ])

        self.chatbot = chat_prompt_template | ChatOllama(
            model="llama3.1:8b-instruct-q8_0",
            max_tokens=8192,
            temperature=0.8,
        )

        # Initialize ChatOllama model with configuration
        self.chatbot_with_history = RunnableWithMessageHistory(self.chatbot, get_session_history)


    def chat_with_history(self, user_input, session_id=None):
        """
        Process user input and generate a response including conversation history.

        Args:
            user_input (str): The user's input message.
            session_id (str, optional): Unique identifier for the session.

        Returns:
            str: The AI-generated response.
        """
        if session_id is None:
            session_id = self.session_id

        response = self.chatbot_with_history.invoke(
            [HumanMessage(content=user_input)],  # Wrap user input as HumanMessage
            {"configurable": {"session_id": session_id}},  # Pass configuration with session_id
        )

        LOG.debug(f"[ChatBot][{self.name}] {response.content}")

        return response.content
        