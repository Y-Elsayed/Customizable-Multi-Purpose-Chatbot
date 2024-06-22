import json
from sentence_transformers import SentenceTransformer, util
from pydantic import BaseModel




class Query(BaseModel):
    text: str

class DataProcessing:
    _embedding_model : SentenceTransformer
    
    
    def __init__(self,embedding_model = 'all-MiniLM-L6-v2'):
        self._embedding_model = SentenceTransformer(embedding_model)
        
    # Data preprocessing
    def fetch_data(file_path = 'university_data.json'):
        with open(file_path, 'r') as f:
            return json.load(f)
        
    # Create embeddings for the data
    def create_embeddings(self, data):
        embeddings = []
        for category in data['categories']:
            for entry in category['entries']:
                question = entry['question']
                embeddings.append(self._embedding_model.encode(question, convert_to_tensor=True))
        return embeddings
    
    def split_input(user_input):# Need some work. Will use NLP to detect different questions
        questions = re.split(r'[.?!]\s*', user_input)
        questions = [q for q in questions if q]
        return questions