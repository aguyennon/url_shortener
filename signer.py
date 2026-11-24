import os
import hmac
import hashlib
from dotenv import load_dotenv
from encoder import encode, decode

load_dotenv() # to read my .env file

SECRET_KEY = os.environ["URL_SECRET"].encode() # to turn text into bytes for hmac
SIG_LENGTH = 4 # to carry 4 extra char per code :P


def sign(url_id):
    digest = hmac.new(SECRET_KEY, str(url_id).encode(), hashlib.sha256).digest()

    first_four = digest[:4]
    int_first_four = int.from_bytes(first_four, "big")
    bytes_in_range = int_first_four % 62 ** SIG_LENGTH # since the integer can be huge, needs to fit 4 base62 chars

    result = encode(bytes_in_range).rjust(SIG_LENGTH, "0")
    return result


def make_code(url_id):
    return encode(url_id) + sign(url_id)


def read_code(code):
    if len(code) <= SIG_LENGTH: # needs to be at least one ID char (at least 5)
        return None

    id_part = code[:-SIG_LENGTH] # to grab everything but last 4 = SIG_LENGTH
    signature_part = code[-SIG_LENGTH:] # to grab last 4 = SIG_LENGTH

    try:
        decoded_id = decode(id_part)
    except ValueError:
        return None
    
    new_signature = sign(decoded_id)
    if not hmac.compare_digest(new_signature.encode(), signature_part.encode()): #.encode() to compare bytes instead of strings
        return None
    
    return decoded_id






    
