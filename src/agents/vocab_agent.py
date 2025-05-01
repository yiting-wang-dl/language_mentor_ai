from langchain_core.messages import AIMessage 

from .session_history import get_session_history
from .agent_base import AgentBase
from utils.logger import LOG

class VocabAgent(AgentBase):
    """
    Vocab Agent Class responsible for handling interactions with the user.
    """
    def __init__(self, session_id=None):
        super().__init__(
            name="vocab_study",
            prompt_file="prompts/vocab_study_prompt.txt",
            session_id=session_id
        )
        
    def restart_session(self, session_id=None):
        """
        Restart the session, clear the session history.

        Parameters:
            session_id (str, optional): The session ID to restart. If not provided, the current session ID will be used.

        Returns:
            str: The initial AI message.    
        """ 
        if session_id is None:
            session_id = self.session_id
            
        history = get_session_history(session_id)
        history.clear()
        LOG.debug(f"[history][{session_id}]:{history}")

        return history