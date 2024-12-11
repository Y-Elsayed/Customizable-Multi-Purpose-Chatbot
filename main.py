import src.backend.services.backend_service as bc


backend = bc.BackendService(load_data=False,use_llm=False,model_name = "GPT2")


user_inp = """Can you tell me which majors are available at the university and if they offer any scholarships?
What academic programs does the university provide, and do they have scholarships?
Are there any scholarships available at the university, and what majors can I choose from?
What are the available courses of study at the university, and are there any scholarship opportunities?
I'm interested in knowing the university's offered majors and if there are any scholarships that I can apply for.
I would also like to know how to swim
Would you also tell me how to paint my walls? plzzzz?
"""

user_inp2 = "Hello I wanted to know whether you guys offer any scholarships?"
print(backend.process_input_and_generate_response(user_inp=user_inp2))
