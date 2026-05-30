import requests
response = requests.get("https://catfact.ninja/fact")
if response.status_code == 200:
    data = response.json()
    print("🐱 Cat Fact of the Day")
    print("-" * 22)
    print(data["fact"])
else:
    print("Failed to fetch cat fact.")
