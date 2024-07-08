# from src.backend.models.data_processing import *
# from src.backend.models.chatbot import *
# from scripts.initialize import *

import src.backend.controllers.backend_controller as bc
# initialize()
# config = load_config()

# data_processing = DataProcessing()
# chatbot = Chatbot()


# data_processing.fetch_data(file_path=config["data_json_path"])
# data_processing.create_data_embeddings()

# # TEST CASE
# user_inp = "I was wondering what are the majors that are offered by the university. Also, are there any scholarships offered?."

# user_inp_list = data_processing.split_input(user_input=user_inp)
# # print(user_inp_list)

# user_inp_embedding = data_processing.create_user_input_embedding(
#     user_input_list=user_inp_list
# )

# results_dict = data_processing.compute_similarity(
#     user_input_list=user_inp_list, input_embeddings=user_inp_embedding, threshold=0.5
# )
# # print(responses)

# results = chatbot.generate_response(responses=results_dict["responses"])
# print(results)

bc.BackendController()