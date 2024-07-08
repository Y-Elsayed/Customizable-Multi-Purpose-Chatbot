from .chatbot_controller import ChatbotController
from .data_processing_controller import DataProcessingController
from .database_controller import DatabaseController
from scripts.initialize import *


class BackendController:

    def __init__(self):
        self.__initialize_environment()

        self.chatbot_controller = ChatbotController(self._config)
        self.data_processing_controller = DataProcessingController(self._config)
        self.database_controller = DatabaseController(self._config)

        self.__load_data()

    def __initialize_environment(self):
        initialize()
        self._config = load_config()

    def __load_data(self):
        self.data_processing_controller.load_data()
        self.database_controller.create_tables()
        pass

    def run(self):
        # main-loop logic
        pass
