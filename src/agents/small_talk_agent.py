from .base_scenario_agent import ScenarioAgent

class SmallTalkAgent(ScenarioAgent):
    def __init__(self):
        super().__init__()
        self.name = "Small Talk Agent"

    def respond(self, user_input):
        return f"Small Talk Agent Response: {user_input}"
