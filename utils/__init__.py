import string
import random

def create_new_ref_number(str_len = 10):
    S = str_len
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))
    return str(ran)