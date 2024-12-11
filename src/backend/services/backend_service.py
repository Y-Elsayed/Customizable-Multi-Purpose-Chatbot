from .chatbot_service import ChatbotService
from .data_processing_service import DataProcessingService
from .database_service import DatabaseService
from scripts.initialize import *

# Will remove/change this class since it doesn't apply the SRP, but it's here to ease testing
class BackendService:

    def __init__(self, load_data=True,use_llm = False,model_name = None):
        self.__initialize_environment()
        self.__chatbot_service = ChatbotService(self._config,use_llm=use_llm,model_name=model_name)
        self.__data_processing_service = DataProcessingService(self._config)
        self.__database_service = DatabaseService(self._config)
        self.__database_service.create_tables()
        # maybe add a flag that chooses whether to load data or it's already loaded
        if load_data:
            self.__load_data()

    def __initialize_environment(self):
        initialize()
        self._config = load_config()

    def __load_data(self): # reloads the data into the chatbot in case the data is updated
        self.__data_processing_service.load_data()
        self.__database_service.fetch_and_export_data()

    def process_input_and_generate_response(self, user_inp):
        # dict(str:list(str))
        result = self.__data_processing_service.process_and_search_input(
            user_inp=user_inp
        )
        chatbot_response = self.__chatbot_service.generate_response(responses=result,query=user_inp) # Future Improvement: Refine the user input using an LLM
        # Future improvement: Maybe check the responses whether they are appropriate or not
        
        return chatbot_response
