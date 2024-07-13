from transformers import AutoModelForCausalLM, AutoTokenizer


class Chatbot:

    ### Attributes ###
    # _______________#
    _use_llm: bool
    _model_name: str
    _llm_model: AutoModelForCausalLM
    _llm_tokenizer: AutoTokenizer
    # _______________________________________________________________________________________________#

    ### The Constructor ###
    # ____________________#
    def __init__(self, use_llm=False, model_name="gpt2"):
        self._use_llm = use_llm
        self._model_name = model_name
        # Initialize model and tokenizer if the use_llm flag is set to true
        self._initialize_llm() if use_llm else None

    def _initialize_llm(self):
        """Initialize the language model and tokenizer."""
        self._llm_model = AutoModelForCausalLM.from_pretrained(self._model_name)
        self._llm_tokenizer = AutoTokenizer.from_pretrained(self._model_name)

    # _______________________________________________________________________________________________#

    @property
    def use_llm(self):
        return self._use_llm

    @use_llm.setter
    def use_llm(self, value):
        if value:
            if not self._llm_model or not self._llm_tokenizer:
                self._initialize_llm()
        else:
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
            self._initialize_llm()

    # _______________________________________________________________________________________________#

    ### Output generation###
    # ______________________________#

    # Needs some work yet #
    # query parameter will be used with the LLM
    def generate_response(self, responses, query=""):
        result = ""
        answers = responses.get("responses")
        no_answers = responses.get("out_of_context")
        not_found = responses.get("not_found")

        if not self._use_llm:
            # iterate over the responses and display them
            # print(responses)
            for i in range(1, len(answers) + 1):
                result += f"{i}. {answers[i-1]}\n"

            # temp to test:
            result += "\nNo Answers for:\n"
            for i in range(1, len(no_answers) + 1):
                result += f"- {no_answers[i-1]}\n"
            
            result += "\nNot Found:\n"
            for i in range(1, len(not_found) + 1):
                result += f"- {not_found[i-1]}\n"
                
                
            
        # else:
        #     inputs = self._llm_tokenizer(prompt, return_tensors='pt')
        #     outputs = self._llm_model.generate(inputs['input_ids'], max_length=max_length, num_return_sequences=1)
        #     return self._llm_tokenizer.decode(outputs[0], skip_special_tokens=True)
        #     prompt = self.prepare_prompt(query, responses)
        #     inputs = gpt_tokenizer.encode(prompt, return_tensors="pt")
        #     outputs = gpt_model.generate(inputs, max_length=300, num_return_sequences=1)
        #     return gpt_tokenizer.decode(outputs[0], skip_special_tokens=True)

        return result

    #
