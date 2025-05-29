import requests

try:
    resposta = requests.get(url="https://www.pudim.com.br", timeout=10)
    resposta.raise_for_status()
    print(f'O site www.pudim.com.br está acessível. código de status = {resposta.status_code} ')

except requests.exceptions.RequestException as e:
    print(f'Erro ao acessar: {e}')