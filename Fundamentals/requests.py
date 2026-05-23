import json
import Fundamentals.requests as requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/us/search?entity=song&limit=5&term=" + sys.argv[1])

o = response.json()

for result in o["results"]:
    print(result["trackName"])

# print(json.dumps(response.json(),indent=2))