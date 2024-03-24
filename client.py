import requests
response=requests.post(
    "http://localhost:8000/essay/invoke",
                    json={"input":{"topic":"my favourite cricket player"}})

print(response.json()["output"]["content"])