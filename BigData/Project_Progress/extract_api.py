import requests, json, os

os.makedirs("data/raw", exist_ok=True)

url = "https://data.usajobs.gov/api/search"
params = {"JobCategoryCode": "2210"}

headers = {
    "Host": "data.usajobs.gov",
    "User-Agent": "sosa_brijj@icloud.com",  # <- reemplaza con tu correo real
    "Authorization-Key": "y2yB9N9+m6fIAm01J4xWvv19d69+/6e0uNNlwmQgLIo="  # <- pega tu API Key
}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    with open("data/raw/job_data.json", "w") as f:
        json.dump(response.json(), f, indent=4)
    print("✅ Datos guardados en data/raw/job_data.json")
else:
    print("❌ Error en la solicitud:", response.status_code)
