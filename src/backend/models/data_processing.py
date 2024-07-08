import json
from sentence_transformers import SentenceTransformer, util
from pydantic import BaseModel
from spacy.lang.en import English
import torch
import os


class Query(BaseModel):
    text: str


class DataProcessing:
    ### Attributes ###
    # _______________#
    # _embedding_model: SentenceTransformer
    # _nlp: English
    # _data: json
    # _data_embeddings: list
    # __device: str
    # _______________________________________________________________________________________________#

    ### The Constructor ###
    #____________________#
    def __init__(self, embedding_model="all-MiniLM-L6-v2"):
        self._embedding_model = SentenceTransformer(embedding_model)
        self._nlp = English()
        self._nlp.add_pipe("sentencizer")
        self._data = None
        self.__device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # _______________________________________________________________________________________________#

    ### Data preprocessing methods ###
    # ______________________________#

    # Read chatbot's data from the json file
    def fetch_data(self, file_name="data.json", reload=False):
        if self._data is None or reload:
            # Get the path to the current directory where the script is located
            current_dir = os.path.dirname(os.path.abspath(__file__))
            # Construct the path to the data file in the data folder
            file_path = os.path.join(current_dir, f'../../data/{file_name}')
            try:
                with open(file_path, "r") as f:
                    self._data = json.load(f)
            except FileNotFoundError:
                print(f"Error: The file {file_path} was not found.")
                self._data = None
            except json.JSONDecodeError:
                print("Error: Failed to decode JSON from the file.")
                self._data = None
        else:
            return False
        # reload = False
        return True

    # Create embeddings for the data
    def create_data_embeddings(self):
        self.fetch_data()
        embeddings = []
        for category in self._data["categories"]:
            for entry in category["entries"]:
                question = entry["question"]
                embedding = self._embedding_model.encode(
                    question, convert_to_tensor=True
                )
                embedding = embedding.to(
                    self.__device
                )  # Move embedding to the desired device
                embeddings.append(embedding)
        self._data_embeddings = embeddings

    # _______________________________________________________________________________________________#

    ### User Input Processing methods ###
    # _________________________________#

    # Split the user input to a list sentences to detect different prompts
    def split_input(self, user_input):
        doc = self._nlp(user_input)
        questions = [str(sent) for sent in doc.sents]
        return questions

    # Create embedding for the user's input
    def create_user_input_embedding(self, user_input_list):
        # list of user input embeddings with their same order
        user_input_embedding = [
            self._embedding_model.encode(embedding, convert_to_tensor=True)
            for embedding in user_input_list
        ]
        return user_input_embedding

    def compute_similarity(self, user_input_list, input_embeddings, threshold=0.6):

        # for each embedding in the user's input embeddings
        # compute the cosine similarity between it and the data_embeddings
        # then check if the max score is greater than the threshold. If so append to the in context list
        # otherwise append to the append the I'm here to help with university-related questions.
        responses = list()
        out_of_context = list()
        not_found = list()
        i = 0
        for input_embedding in input_embeddings:
            # #Reshape to be a column vector
            # input_embedding = np.expand_dims(input_embedding, axis=0) if input_embedding.ndim == 1 else input_embedding

            cosine_scores = util.pytorch_cos_sim(
                input_embedding, torch.stack(self._data_embeddings)
            )[0]
            max_score, idx = torch.max(cosine_scores, dim=0)
            if max_score >= threshold:
                found = False
                for category in self._data["categories"]:
                    if idx < len(category["entries"]):
                        responses.append(category["entries"][idx]["answer"])
                        found = True
                        break
                    idx -= len(category["entries"])

                if not found:
                    # not_found.append("I couldn't find an exact match for one of your questions.")
                    not_found.append(user_input_list[i])
            else:
                # out_of_context.append("I'm here to help with university-related questions. For information on other topics, you might want to check online resources or community centers.")
                out_of_context.append(user_input_list[i])
            i = i + 1
            
        return {
            "responses": responses,
            "not_found": not_found,
            "out_of_context": out_of_context,
        }
