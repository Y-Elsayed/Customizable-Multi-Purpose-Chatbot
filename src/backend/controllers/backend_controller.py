import chatbot_controller, data_processing_controller, database_controller
import src.backend.models.chatbot as chatbot
import src.backend.models.data_processing as data_processing
import src.backend.models.database as database
from scripts.initialize import *

class BackendController:


    def __init__(self):
        self.chatbot_controller = chatbot_controller.ChatbotController()
        self.chatbot_controller = data_processing_controller.DataProcessingController()
        self.chatbot_controller = database_controller.DatabaseController()

    def initialize_environment(self):
        initialize()
        self.config = load_config()

    def run(self):
        # main-loop logic
        pass