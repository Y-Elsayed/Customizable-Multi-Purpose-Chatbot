from .chatbot_controller import ChatbotController
from .data_processing_controller import DataProcessingController
from .database_controller import DatabaseController
from scripts.initialize import *


class BackendController:

    def __init__(self, load_data=True):
        self.__initialize_environment()
        self.__chatbot_controller = ChatbotController(self._config)
        self.__data_processing_controller = DataProcessingController(self._config)
        self.__database_controller = DatabaseController(self._config)
        self.__database_controller.create_tables()
        # maybe add a flag that chooses whether to load data or it's already loaded
        if load_data:
            self.__load_data()

    def __initialize_environment(self):
        initialize()
        self._config = load_config()

    def __load_data(self):
        self.__data_processing_controller.load_data()
        self.__database_controller.fetch_and_export_data()

    def process_input_and_generate_response(self, user_inp):
        # dict(str:list(str))
        result = self.__data_processing_controller.process_and_search_input(
            user_inp=user_inp
        )
        chatbot_response = self.__chatbot_controller.generate_response(responses=result)
        # Future improvement: Maybe check the responses whether they are appropriate or not
        
        return chatbot_response
