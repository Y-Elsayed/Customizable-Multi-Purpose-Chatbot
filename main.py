import src.backend.controllers.backend_controller as bc


backend = bc.BackendController(load_data=False,use_llm=True,model_name = "tiiuae/falcon-7b")


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
