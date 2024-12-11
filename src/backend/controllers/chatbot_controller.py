# import backend.models.chatbot as chatbot
from ..models.chatbot import Chatbot


class ChatbotController:

    def __init__(self, config,use_llm = False,model_name = None):
        self.config = config
        self.chatbot = Chatbot(use_llm=use_llm, model_name= model_name)

    # Needs some work yet.
    # I am thinking of making it flexible
    # in some kind of way to be able to change according
    # to the chatbot's functionallity #

    def set_chatbot(self, use_llm: bool, model_name=None):
        self.chatbot.use_llm = use_llm
        if model_name != self.chatbot.model_name:
            self.chatbot.model_name = model_name

    def generate_response(self, responses, query=""):
        return self.chatbot.generate_response(responses=responses, query=query)
