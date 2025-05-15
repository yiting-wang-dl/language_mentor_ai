# tabs/vocab_tab.py

import gradio as gr
from agents.vocab_agent import VocabAgent
from utils.logger import LOG

vocab_agent = VocabAgent()

feature = "vocab_study"

def get_page_desc(feature):
    try:
        with open(f"content/page/{feature}.md", "r", encoding="utf-8") as file:
            scenario_intro = file.read().strip()
        return scenario_intro
    except FileNotFoundError:
        LOG.error(f"Vocab study file content/page/{feature}.md not found! ")
        return "Vocab study file not found. "
    

def restart_vocab_study_chatbot():
    vocab_agent.restart_session()

    # Define initial message and interact with vocab agent
    _next_round = "Start learning new words!"
    bot_message = vocab_agent.chat_with_history(_next_round)    

    return gr.Chatbot(
        value=[(_next_round, bot_message)],
        height=1000,
    )

def handle_vocab(user_input, chat_history):
    bot_message = vocab_agent.chat_with_history(user_input)
    LOG.info(f"[Vocab ChatBot]: {bot_message}")
    return bot_message

def create_vocab_tab():
    with gr.Tab("Vocab"):   
        gr.Markdown("## Learn new words and practice them in conversation")

        gr.Markdown(get_page_desc(feature))

        vocab_chatbot = gr.Chatbot(
            placeholder="<strong>Let's do it!</strong>",
            height=800,
        )   

        gr.ChatInterface(
            # type="messages",  # TODO: tuple will be deprecated, updated to message! message doesn't work with current implementation.
            fn=handle_vocab,
            chatbot=vocab_chatbot,
            submit_btn="Send",  
            title="<strong>Your English Mentor Eva</strong><br><br>Start learning new words!",
        )

        restart_btn = gr.ClearButton(value="Get Started!")

        restart_btn.click(
            fn=restart_vocab_study_chatbot,
            inputs=None,
            outputs=vocab_chatbot,
        )

        
        # gr.ChatInterface(
        #     fn=handle_vocab,
        #     submit_btn="Send",
        #     retry_btn=None,
        #     undo_btn=None,
        #     clear_btn="Next Level",
        #     title="<strong>你的英语私教 Eva</strong><br><br>Start learning new words!",
        # )
    

