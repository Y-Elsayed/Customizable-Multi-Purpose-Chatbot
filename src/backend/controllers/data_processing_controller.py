from ..models.data_processing import DataProcessing


class DataProcessingController:

    def __init__(self, config):
        self.config = config
        self.data_processing = DataProcessing()

    def load_data(self):
        if self.data_processing.fetch_data(file_path=self.config["data_json_path"]):
            self.create_data_embeddings()

    def reload_data(self):
        self.data_processing.fetch_data(
            file_path=self.config["data_json_path"], reload=True
        )
        self.create_data_embeddings()


def process_and_search_input(self, user_inp: str):
    user_questions_split = self.data_processing(user_input=user_inp)
    embeddings_list = self.data_processing.create_user_input_embedding(
        user_input_list=user_questions_split
    )
    responses = self.data_processing.compute_similarity(
        user_input_list=user_questions_split, input_embeddings=embeddings_list
    )

    return responses
