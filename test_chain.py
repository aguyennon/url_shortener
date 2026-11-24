from db import save_url, get_url, init_db
from encoder import encode, decode

EXAMPLE_URL = "https://example.com/some/long/path"

init_db()

stored_id = save_url(EXAMPLE_URL)
print(stored_id)
stored_code = encode(stored_id)
print(stored_code)
decoded_id = decode(stored_code)
print(decoded_id)
get_id = get_url(decoded_id)
print(get_id)