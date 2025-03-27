import secrets
import requests

# Documentation: https://trackapi.nutritionix.com/docs/#/default/post_v2_natural_exercise


base_url = "https://trackapi.nutritionix.com/"
natural_lan = "v2/natural/exercise"

activity = input("What did you do? ")


headers = {
    "x-app-id": secrets.NUTRICIONIX_APP_ID,
    "x-app-key": secrets.NUTRICIONIX_API_KEY
  }

user_params = {
    "query": activity,
    "gender": "male",
    "weight_kg": 62,
    "height_cm": 172,
    "age": 53,
}

response = requests.post(url=base_url + natural_lan, headers=headers, json=user_params)
result = response.json()

print(result)
calories = result["exercises"][0]["nf_calories"]
print(f"\nCalories burnt: {calories}")
