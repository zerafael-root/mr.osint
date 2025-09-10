import requests
import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear()
    print("                   ___      _       _   ")
    print(" _ __ ___  _ __   / _ \\ ___(_)_ __ | |_ ")
    print("| '_ ` _ \\| '__| | | | / __| | '_ \\| __|")
    print("| | | | | | |_   | |_| \\__ \\ | | | | |_ ")
    print("|_| |_| |_|_(_)   \\___/|___/_|_| |_|\\__|")
    print(" ")
    print("O que você deseja fazer?")
    print("1. Ver localização de IP")
    print("2. Consultar CPF")
    print("3. Procurar se existe um vazamento de um email")
    print("4. Procurar se existe um vazamento de um usuário")
    print("0. Sair")
    choice = input().strip()

    if choice == "1":
        choice_ip = input("Digite o IP: ")
        try:
            req = requests.get(f"https://api.ipquery.io/{choice_ip}?format=yaml")
            if req.text.strip():
                print(req.text)
            else:
                print("Nenhum resultado encontrado para esse IP.")
        except Exception as e:
            print(f"Erro na requisição: {e}")

    elif choice == "2":
        headers = {
            'X-API-Key': '{CPF-API-KEY}',
            'Content-Type': 'application/json'
        }
        cpf = input("Digite o CPF (apenas números): ")
        try:
            response = requests.get(f'https://api.cpf-brasil.org/cpf/{cpf}', headers=headers)
            data = response.json()
            data_1 = data.get("data", {})
            if data_1:
                result = {
                    "CPF": data_1.get("CPF", "N/A"),
                    "Nome completo": data_1.get("NOME", "N/A"),
                    "Gênero": data_1.get("SEXO", "N/A"),
                    "Data de Nascimento": data_1.get("NASC", "N/A"),
                    "Nome da mãe": data_1.get("NOME_MAE", "N/A")
                }
                print(result)
            else:
                print("Nenhum resultado encontrado para esse CPF.")
        except Exception as e:
            print(f"Erro na requisição: {e}")

    elif choice == "3":
        email = input("Digite o email: ")
        API_KEY = "rwldJ8XjK2yg71Jgticl"
        url = f"https://ulpcloud.site/url?k={API_KEY}&q={email}&t=1"
        try:
            response = requests.get(url, timeout=12, headers={'User-Agent': 'Mozilla/5.0'})
            if response.status_code == 200 and response.text.strip():
                print("Resultado encontrado:")
                print(response.text)
            else:
                print("Nenhum resultado encontrado para esse email.")
        except Exception as e:
            print(f"Erro na requisição: {e}")

    elif choice == "4":
        user = input("Digite o user: ")
        API_KEY = "rwldJ8XjK2yg71Jgticl"
        url = f"https://ulpcloud.site/url?k={API_KEY}&q={user}&t=1"
        try:
            response = requests.get(url, timeout=12, headers={'User-Agent': 'Mozilla/5.0'})
            if response.status_code == 200 and response.text.strip():
                print("Resultado encontrado:")
                print(response.text)
            else:
                print("Nenhum resultado encontrado para esse usuário.")
        except Exception as e:
            print(f"Erro na requisição: {e}")

    elif choice == "0":
        print("Saindo...")
        time.sleep(0.5)
        break

    else:
        print("Você digitou algo errado, tente novamente")

    # Agora a mensagem de voltar ao menu sempre aparece
    input("\nPressione ENTER para voltar ao menu...")

