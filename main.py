import src.backend.controllers.backend_controller as bc


backend = bc.BackendController(load_data=False)


user_inp = """I was wondering what are the majors that are offered by the university. Also, are there any scholarships offered?
I would also like to know how to swim
Would you tell me how to paint my walls? plzzzz?
"""
print(backend.process_input_and_generate_response(user_inp=user_inp))
