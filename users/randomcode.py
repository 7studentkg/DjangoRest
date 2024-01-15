
import random
import string

def generate_random_code():
    code_length = 6
    characters = string.ascii_uppercase + string.digits
    random_code = ''.join(random.choice(characters) for i in range(code_length))
    return random_code
