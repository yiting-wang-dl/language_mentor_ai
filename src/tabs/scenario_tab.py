# tabs/scenario_tab.py

import gradio as gr
from agents.scenario_agent import ScenarioAgent
from utils.logger import LOG

agents = {
    "job_interview": ScenarioAgent("job_interview"),
    "small_talk": ScenarioAgent("small_talk"),
}

def get_page_desc(scenario):
    try:
        with open(f"content/page/{scenario}.md", "r", encoding="utf-8") as file:
            scenario_intro = file.read().strip()
        return scenario_intro
    except FileNotFoundError:
        LOG.error(f"Senario Intro file content/page/{scenario}.md not found! ")
        return "Senario Intro file not found. "
    
def start_new_scenario_chatbot(scenario):
    initial_ai_message = agents[scenario].start_new_session()

    return gr.Chatbot(
        value=[(None, initial_ai_message)],
        height=600,
        show_progress=False,
    )

def handle_scenario(scenario, user_input, chat_history):
    bot_message = agents[scenario].chat_with_history(user_input)
    LOG.info(f"[ChatBot]: {bot_message}")
    return bot_message

def create_scenario_tab():
    with gr.Tab("Scenario"):
        gr.Markdown("## Pick a scenario to practice and complete the goal and challenges")

        scenario_radio = gr.Radio(
            choices=[
                "Job Interview",
                "Small Talk",
            ],
            label="Scenario",
        )

        scenario_intro = gr.Markdown()
        # scenario_chatbot = gr.Chatbot(
        #     placeholder="<strong>Your English Mentor Eva</strong><br><br>Pick a scenario and start the conversation!",
        #     height=600,
        # )

        # scenario_radio.change(
        #     fn=lambda s: (get_page_desc(s), start_new_scenario_chatbot(s)), # update scenario intro and chatbot
        #     inputs=scenario_radio,
        #     outputs=[scenario_intro, scenario_chatbot], # output scenario intro and chatbot components
        # )

        # gr.ChatInterface(
        #     fn=handle_scenario,
        #     chatbot=scenario_chatbot,
        #     additional_inputs=scenario_radio,
        #     retry_btn=None,
        #     undo_btn=None,
        #     clear_btn="Clear History",
        #     submit_btn="Send",
        #     title="<strong>你的英语私教 Eva</strong><br><br>Pick a scenario and start the conversation!",
        # )


        selected_scenario = gr.State()

        def on_scenario_change(s):
            desc = get_page_desc(s)
            return desc, s

        scenario_radio.change(
            fn=on_scenario_change,
            inputs=scenario_radio,
            outputs=[scenario_intro, selected_scenario],
        )

        gr.ChatInterface(
            fn=handle_scenario,
            additional_inputs=[selected_scenario],
            submit_btn="Send",
            retry_btn=None,
            undo_btn=None,
            clear_btn="Clear History",
            title="<strong>你的英语私教 Eva</strong><br><br>Pick a scenario and start the conversation!",
        )