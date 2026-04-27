import requests
from decouple import config

# Replace with your actual client ID and secret
client_id = config('CLIENT_ID_2')
client_secret = config('CLIENT_SECRET_2')

print(client_id)
print(client_secret)

redirect_uri = 'http://localhost:8000/callback/'

# Token endpoint
token_url = 'http://127.0.0.1:8000/o/token/'

auth_code =

# Data for token request
data = {
    'grant_type': 'authorization_code',
    'code': auth_code,
    'redirect_uri': redirect_uri,
    'client_id': client_id,
    'client_secret': client_secret,
}

# Request the token
response = requests.post(token_url, data=data)
token = response.json().get('access_token')
print(response.json())
print(token)

# Endpoint de introspecção
introspect_url = 'http://127.0.0.1:8000/o/introspect/'

# Autenticação básica com client_id e client_secret
auth = (client_id, client_secret)

# Dados da requisição
data = {
    'token': token
}

# Faz a requisição POST
response = requests.post(introspect_url, auth=auth, data=data)

# Exibe a resposta
print(response.status_code)
#print(response.json())

api_url = 'http://127.0.0.1:8000/api/rooms/'  # Replace with your actual API endpoint
api_response = requests.get(api_url)
print(api_response.json())

# Use the token to access the protected API
headers = {'Authorization': f'Bearer {token}'}

debug_url = 'http://127.0.0.1:8000/api/debug/'
debug_response = requests.get(debug_url, headers=headers)
print(debug_response.json())

api_url = 'http://127.0.0.1:8000/api/rooms/'  # Replace with your actual API endpoint
api_response = requests.get(api_url, headers=headers)

print(api_response.json())


