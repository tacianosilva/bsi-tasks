import webbrowser
from urllib.parse import urlencode
from decouple import config

# Configurações
client_id = config('CLIENT_ID_2')
redirect_uri = 'http://127.0.0.1:8000/callback/'
authorize_url = 'http://127.0.0.1:8000/o/authorize/'

# Parâmetros
params = {
    'client_id': client_id,
    'response_type': 'code',
    'redirect_uri': redirect_uri,
    'scope': 'read write',
}

# Abre no navegador
url = f'{authorize_url}?{urlencode(params)}'
print("Abra essa URL no navegador e autorize o app:")
print(url)
webbrowser.open(url)
