from .base_scenario_agent import ScenarioAgent

class RentingAgent(ScenarioAgent):
    def __init__(self):
        super().__init__()
        self.name = "Renting Agent"

    def respond(self, user_input):
        return f"Renting Agent Response: {user_input}"