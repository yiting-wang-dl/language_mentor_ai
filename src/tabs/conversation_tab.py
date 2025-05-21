# tabs/conversation_tab.py

import gradio as gr
from agents.conversation_agent import ConversationAgent
from utils.logger import LOG


conversation_agent = ConversationAgent()

def restart_conversation_chatbot():
    conversation_agent.start_new_session()

    # Define initial message and interact with vocab agent
    _next_round = "Start new conversation!"
    bot_message =conversation_agent.chat_with_history(_next_round)    

    return gr.Chatbot(
        value=[(_next_round, bot_message)],
        height=600,
    )

def create_conversation_tab():
    with gr.Tab("Conversation"):
        gr.Markdown("## Practice English Conversation")

        conversation_chatbot = gr.Chatbot(
            placeholder="<strong>Your English Mentor Eva</strong><br><br>You can talk to me about anything, remember to use English!",
            height=800, 
        )

        def handle_conversation(user_input, chat_history):
            bot_message = conversation_agent.chat_with_history(user_input)
            LOG.info(f"[Conversation ChatBot]: {bot_message}")
            return bot_message
        
        gr.ChatInterface(
            # type="messages",  # TODO: tuple will be deprecated, updated to message! message doesn't work with current implementation.
            fn=handle_conversation,
            chatbot=conversation_chatbot,
            submit_btn="Send",
            title="Your English Mentor Eva",
        )

        # TODO: history is not correctly cleared. 
        clear_btn = gr.ClearButton(value="Clear History")
        clear_btn.click(
            fn=restart_conversation_chatbot, 
            inputs=None,
            outputs=conversation_chatbot,
        )
