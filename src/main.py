import gradio as gr
from agents.conversation_agent import ConversationAgent
from agents.job_interview_agent import JobInterviewAgent
from agents.hotel_checkin_agent import HotelCheckInAgent
from agents.salary_negotiation_agent import SalaryNegotiationAgent
from agents.renting_agent import RentingAgent
from utils.logger import LOG

# Implement the selection and invocation of the conversation agent and scenario agent
conversation_agent = ConversationAgent()
job_interview_agent = JobInterviewAgent()
# small_talk_agent = SmallTalkAgent()
# salary_negotiation_agent = SalaryNegotiationAgent()
# renting_agent = RentingAgent()


# Conversation Agent
def handle_conversation(user_input, chat_history):
    LOG.debug(f"[ChatHistory]: {chat_history}")
    # bot_message = conversation_agent.chat(user_input)
    bot_message = conversation_agent.chat_with_history(user_input)
    LOG.info(f"[ChatBot]: {bot_message}")
    return bot_message



# Scenario agent handler function that invokes the corresponding agent based on the selected scenario.
def handle_scenario(user_input, history, scenario):
    agents = {
        "Job Interview": job_interview_agent,
        # "Small Talk": small_talk_agent,
        # "Salary Negotiation": salary_negotiation_agent,
        # "Renting": renting_agent
    }
    return agents[scenario].respond(user_input)

# Gradio
with gr.Blocks(title="Language Mentor AI") as language_mentor_app:
    with gr.Tab("Conversation"):
        gr.Markdown("## Practice Conversation ")
        conversation_chatbot = gr.Chatbot(
            placeholder="<strong>Your personal English tutor Eva </strong><br><br> What do you want to talk about today?",
            height=800,
        )

        gr.ChatInterface(
            fn=handle_conversation, 
            chatbot=conversation_chatbot,
            retry_btn=None,
            undo_btn=None,
            clear_btn="Clear History",
            submit_btn="Submit",
        )

    with gr.Tab("Senario Practice"):
        gr.Markdown("## Choose a senario and complete the tasks")
        scenario_dropdown = gr.Dropdown(choices=["Job Interview", "Small Talk", "Salary Negotiation", "Renting"], label="Choose your senario")
        scenario_chatbot = gr.Chatbot(
            placeholder="<strong>Your personal English tutor Eva</strong><br><br> choose your senario and start the conversation！",
            height=800,
        )
        
        gr.ChatInterface(
            fn=handle_scenario,
            chatbot=scenario_chatbot,
            additional_inputs=scenario_dropdown,
            retry_btn=None,
            undo_btn=None,
            clear_btn="Clear History",
            submit_btn="Submit",
        )

if __name__ == "__main__":
    language_mentor_app.launch(share=True, server_name="0.0.0.0")