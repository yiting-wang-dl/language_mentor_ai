# tabs/conversation_tab.py

import gradio as gr
from agents.conversation_agent import ConversationAgent
from utils.logger import LOG


conversation_agent = ConversationAgent()

def handle_conversation(user_input, chat_history):
    bot_message = conversation_agent.chat_with_history(user_input)
    LOG.info(f"[Conversation ChatBot]: {bot_message}")
    return bot_message

def create_conversation_tab():
    with gr.Tab("Conversation"):
        gr.Markdown("## Practice English Conversation")

        def handle_conversation(user_input, chat_history):
            bot_message = conversation_agent.chat_with_history(user_input)
            LOG.info(f"[Conversation ChatBot]: {bot_message}")
            return bot_message
        
        gr.ChatInterface(
            fn=handle_conversation,
            retry_btn=None, # Hide retry button
            undo_btn=None, # Hide undo button
            clear_btn="Clear History",
            title="Your English Mentor Eva",
            description="You can talk to me about anything, remember to use English!",
            submit_btn="Send",
        )