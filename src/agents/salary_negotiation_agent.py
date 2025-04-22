from .base_scenario_agent import ScenarioAgent

class SalaryNegotiationAgent(ScenarioAgent):
    def __init__(self):
        super().__init__()
        self.name = "Salary Negotiation Agent"

    def respond(self, user_input):
        return f"Salary Negotiation Agent Response: {user_input}"