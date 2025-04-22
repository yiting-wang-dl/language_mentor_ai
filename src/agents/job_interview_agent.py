from .base_scenario_agent import ScenarioAgent

class JobInterviewAgent(ScenarioAgent):
    def __init__(self):
        super().__init__()
        self.name = "Job Interview Agent"

    def respond(self, user_input):
        # Invoke the conversation logic related to job interviews
        return f"Job Interview Agent Response: {user_input}"