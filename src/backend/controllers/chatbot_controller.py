

class ChatbotController:

    def __init__(self, chatbot):
        self.chatbot = chatbot


    # Needs some work yet.
    # I am thinking of making it flexible
    # in some kind of way to be able to change according
    # to the chatbot's functionallity #
    
    def prepare_prompt(query="", responses="Hello there, I am here to help you"):
        prompt = (
            "You are a helpful and knowledgeable chatbot for a university. Answer the following query based on the provided information.\n\n"
            "Query: {}\n\n"
            "Relevant Information:\n{}\n\n"
            "Provide a detailed and polite response to the query above."
        )
        combined_responses = "\n".join(responses)
        return prompt.format(query, combined_responses)
    
    def set_chatbot(self, use_llm: bool, model_name = 'gpt2'):
        self.chatbot.use_llm = use_llm
        if model_name != self.chatbot.model_name:
            self.chatbot.model_name = model_name
            
    def generate_response(self, query, responses):
        return self.chatbot.generate_response(query, responses)

