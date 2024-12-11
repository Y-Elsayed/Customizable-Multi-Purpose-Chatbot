from ..services.chatbot_service import ChatbotService


class ChatbotController:
    def __init__(self, config):
        self.config = config
        self.chatbot_service = ChatbotService(config=config)

    def handle_user_input(self, user_input: str):
        pass

    def update_chatbot_settings(self, use_llm: bool, model_name=None):
        pass