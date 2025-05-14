import requests
from requests.auth import HTTPBasicAuth

receiver_id = "254187"
secret = "5f3fcf1ed94cc42a1f2a4b2d8dd9dfeb0f3fba3c"

url = "https://khipu.com/api/2.0/payments"

data = {
    "subject": "Pago de prueba Khipu - Erick",
    "currency": "CLP",
    "amount": 4990,
    "transaction_id": "test-erick-001",
    "return_url": "https://demo.khipu.com/return",
    "cancel_url": "https://demo.khipu.com/cancel",
    "notify_url": "https://demo.khipu.com/notify"
}

response = requests.post(url, data=data, auth=HTTPBasicAuth(receiver_id, secret))

print("Código de respuesta:", response.status_code)
print("Respuesta JSON:")
print(response.json())
