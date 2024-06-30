from transformers import AutoModelForCausalLM, AutoTokenizer
class Chatbot : 
    
    ### Attributes ###
    # _______________#
    _use_llm : bool
    _model_name : str
    _llm_model : AutoModelForCausalLM
    _llm_tokenizer : AutoTokenizer
    # _______________________________________________________________________________________________#
    
    ### The Constructor ###
    #____________________#
    def __init__(self, use_llm=False, model_name='gpt2'):
        self._use_llm = use_llm
        self._model_name = model_name
        # Initialize model and tokenizer if the use_llm flag is set to true
        self._initialize_llm() if use_llm else None

    def _initialize_llm(self):
        """Initialize the language model and tokenizer."""
        self._llm_model = AutoModelForCausalLM.from_pretrained(self._model_name)
        self._llm_tokenizer = AutoTokenizer.from_pretrained(self._model_name)
        
    # _______________________________________________________________________________________________#
    
    ### Setters and Getters ###
    def __setattr__(self, name, value):
        if name == '_use_llm':
            if value:
                # If setting _use_llm to True, initialize the model and tokenizer
                if not hasattr(self, '_llm_model') or not hasattr(self, '_llm_tokenizer'):
                    self._initialize_llm()
            # else clear the models as maybe the user wants to change the model
            elif hasattr(self, '_llm_model') and hasattr(self, '_llm_tokenizer'):
                del self._llm_model
                del self._llm_tokenizer
                
        super().__setattr__(name, value)
        
    @property
    def use_llm(self):
        return self._use_llm

    @use_llm.setter
    def use_llm(self, value):
        if value:
            # If setting use_llm to True, initialize the model and tokenizer
            if not self._llm_model or not self._llm_tokenizer:
                self._initialize_llm()
        else:
            # Optionally clear the model and tokenizer if setting use_llm to False
            self._llm_model = None
            self._llm_tokenizer = None

        self._use_llm = value

    @property
    def model_name(self):
        return self._model_name

    @model_name.setter
    def model_name(self, value):
        self._model_name = value
        if self._use_llm:
            # Re-initialize the model and tokenizer if the model name changes
            self._initialize_llm()
        
    # _______________________________________________________________________________________________#
        
    ### Output generation Methods ###
    #______________________________#
    
    def combine_responses(responses):
        return " ".join(responses)

    # Needs some work yet #
    def prepare_prompt(query= "Hi", responses = "Hello there, I am here to help you"):
        prompt = (
            "You are a helpful and knowledgeable chatbot for a university. Answer the following query based on the provided information.\n\n"
            "Query: {}\n\n"
            "Relevant Information:\n{}\n\n"
            "Provide a detailed and polite response to the query above."
        )
        combined_responses = "\n".join(responses)
        return prompt.format(query, combined_responses)
    
    
    # Needs some work yet #
    def generate_response(self,query = "", responses = []):
        result = ""
        if not self._use_llm:
            #iterate over the responses and display them
            # print(responses)
            for i in range(1, len(responses)+1):
                result+=f"{i}. {responses[i-1]}\n"
        # else:
        #     inputs = self._llm_tokenizer(prompt, return_tensors='pt')
        #     outputs = self._llm_model.generate(inputs['input_ids'], max_length=max_length, num_return_sequences=1)
        #     return self._llm_tokenizer.decode(outputs[0], skip_special_tokens=True)
        #     prompt = self.prepare_prompt(query, responses)
        #     inputs = gpt_tokenizer.encode(prompt, return_tensors="pt")
        #     outputs = gpt_model.generate(inputs, max_length=300, num_return_sequences=1)
        #     return gpt_tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        print(result)
        return result
    
    #