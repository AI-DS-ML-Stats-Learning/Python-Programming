# email = input("What is your email? ").strip()

# if "@" in email and "." in email:
#     print("valid")
# else:
#     print("invalid")

# username, domain = email.split("@")

# if (username) and ("." in domain):
# if (username) and domain.endswith(".edu"):
#     print("valid")
# else:
#     print("invalid")

import re

email = input("What is your email? ").strip()

# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
if re.search(r"^\w(\w|.)+@(\w+\.)?\w+\.(edu|com|co)(.in)?$", email, re.IGNORECASE):
    print("valid")
else:
    print("invalid")


