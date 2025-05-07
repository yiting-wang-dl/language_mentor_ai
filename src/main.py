import gradio as gr
from tabs.conversation_tab import create_conversation_tab
from tabs.scenario_tab import create_scenario_tab
from tabs.vocab_tab import create_vocab_tab
from utils.logger import LOG

def main():
    with gr.Blocks(title="LanguageMentor AI") as language_mentor_app:
        create_scenario_tab()
        create_conversation_tab()
        create_vocab_tab()
    
    # Initialize the application
    language_mentor_app.launch(share=True, server_name="0.0.0.0")

if __name__ == "__main__":
    main()
    
    
# TODO: 1. add user id?
# 2. handle session id correctly