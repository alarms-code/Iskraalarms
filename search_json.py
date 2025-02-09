import json

# Carregar o ficheiro JSON
with open("alarms.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Função para pesquisar por código ou descrição
def search_alarm(search_term):
    results = [entry for entry in data if search_term.lower() in str(entry.values()).lower()]
    return results

# Pedir input ao utilizador
search_term = input("Digite o código ou descrição: ")
matches = search_alarm(search_term)

# Mostrar resultados
if matches:
    print("\nResultados encontrados:")
    for match in matches:
        print(match)
else:
    print("\nNenhum resultado encontrado.")
