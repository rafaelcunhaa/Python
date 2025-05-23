import requests

def converter_moeda(valor, de, para):
    url = f"https://economia.awesomeapi.com.br/last/{de}-{para}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Erro ao acessar a API")
        return

    data = response.json()
    par = f"{de}{para}"
    taxa = float(data[par]['bid'])
    convertido = valor * taxa

    print(f"{valor:.2f} {de} = {convertido:.2f} {para}")

if __name__ == "__main__":
    print("Conversor de Moedas")
    de = input("Moeda de origem (ex: USD, BRL): ").upper()
    para = input("Moeda de destino (ex: BRL, EUR): ").upper()
    valor = float(input(f"Valor em {de}: "))

    converter_moeda(valor, de, para)
