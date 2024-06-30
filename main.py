from src.backend.data_processing import *
from src.backend.chatbot import *
from scripts.initialize import *


initialize()
data_processing = DataProcessing()
chatbot = Chatbot()


university_data = data_processing.fetch_data()
embeddings = data_processing.create_data_embeddings(university_data)

# TEST CASE
user_inp = "I was wondering what are the majors that are offered by the university. Also, are there any scholarships offered?."

user_inp_list = data_processing.split_input(user_input=user_inp)
# print(user_inp_list)

user_inp_embedding = data_processing.create_user_input_embedding(
    user_input_list=user_inp_list
)

results_dict = data_processing.compute_similarity(
    user_input_list=user_inp_list, input_embeddings=user_inp_embedding, threshold=0.5
)
# print(responses)

results = chatbot.generate_response(responses=results_dict["responses"])
# print(results)
