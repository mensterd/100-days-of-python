import requests

# get question data from: https://opentdb.com/

base_url = "https://opentdb.com/api.php?"

# Nr. of questions to retrieve: amount
# Category of interest: category
# Type: formatting to return

options = {
    "amount": 10,
    "category": 9,
    "type": "boolean"
}

response = requests.get(url=base_url, params=options)
response.raise_for_status()
data = response.json()

question_data = data["results"]
