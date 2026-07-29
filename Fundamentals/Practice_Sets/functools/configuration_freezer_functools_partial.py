def send_request(base_url, endpoint, params):
    return f"Sending request to {base_url}/{endpoint} with params {params}"
    
# Since your app only talks to GitHub's API, it is tedious to keep typing the same 
# base URL ("https://api.github.com") every time you make a request.

# Your Task:

# Import partial from functools.
# Use partial to create a new function named github_request where the base_url parameter 
# is pre-filled (frozen) with the string "https://api.github.com".
# (It should output: "Sending request to https://api.github.com/users with params {'q': 'Salil'}")

from functools import partial

@partial
def send_request(base_url, endpoint, params):
    return f"Sending request to {base_url}/{endpoint} with params {params}"

github_request = partial(send_request, base_url = "https://api.github.com")

print(github_request(endpoint="users", params={"q": "Salil"}))
