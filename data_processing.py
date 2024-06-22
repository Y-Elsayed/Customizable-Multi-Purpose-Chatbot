import json
from sentence_transformers import SentenceTransformer, util
from pydantic import BaseModel
from spacy.lang.en import English
import torch



class Query(BaseModel):
    text: str

class DataProcessing:
    ### Attributes ###
    #_______________#
    _embedding_model : SentenceTransformer
    _nlp : English
    _data : json
    _data_embeddings : list
    
    #_______________________________________________________________________________________________#
    
    #The Constructor
    def __init__(self,embedding_model = 'all-MiniLM-L6-v2'):
        self._embedding_model = SentenceTransformer(embedding_model)
        self._nlp = English()
        self._nlp.add_pipe("sentencizer")
        self._data = None
        
    #_______________________________________________________________________________________________#
    
    ### Data preprocessing ###
    #________________________#
    
    # Read chatbot's data from the json file
    def fetch_data(self, file_path = 'university_data.json',reload = False):
        if self._data == None or reload == True:
            with open(file_path, 'r') as f:
                self._data = json.load(f)
        return
        
    # Create embeddings for the data
    def create_data_embeddings(self, data):
        self.fetch_data()
        embeddings = []
        for category in self._data['categories']:
            for entry in category['entries']:
                question = entry['question']
                embeddings.append(self._embedding_model.encode(question, convert_to_tensor=True))
        self._data_embeddings = embeddings
    
    #_______________________________________________________________________________________________#
    
    ### User Input Processing ###
    #________________________#
    
    # Split the user input to a list sentences to detect different prompts
    def split_input(self, user_input): 
        questions = list(self._nlp(user_input))
        return questions
    
    # Create embedding for the user's input
    def create_user_input_embedding(self, user_input_list ):
        # list of user input embeddings with their same order
        user_input_embedding = [self.embedding_model.encode(embedding) for embedding in user_input_list]
        return user_input_embedding
    
    def process_questions(self, input_embeddings,threshold = 0.5):
        
        # for each embedding in the user's input embeddings
        # compute the cosine similarity between it and the data_embeddings
        # then check if the max score is greater than the threshold. If so append to the in context list
        # otherwise append to the append the I'm here to help with university-related questions.
        responses = list()
        out_of_context = list()
        not_found = list()
        
        for input_embedding in input_embeddings:
            cosine_scores = util.pytorch_cos_sim(input_embedding, torch.stack(self._data_embeddings))[0]
            max_score, idx = torch.max(cosine_scores, dim=0)
            if(max_score >= threshold):
                found = False
                for category in self._data['categories']:
                    if idx < len(category['entries']):
                        responses.append(category['entries'][idx]['answer'])
                        found = True
                        break
                    idx -= len(category['entries'])
                    #continue
                if not found:
                    not_found.append("I couldn't find an exact match for one of your questions.")
            else:
                out_of_context.append("I'm here to help with university-related questions. For information on other topics, you might want to check online resources or community centers.")
            return responses,out_of_context,not_found