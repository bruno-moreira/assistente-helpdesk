import json

CAMINHO_CONFIGURACAO = "/home/bruno/Documentos/ia/assistente/config.json"

# Carregar o JSON
try:        
    with open(CAMINHO_CONFIGURACAO, "r", encoding="utf8") as arquivo:
        dados = json.load(arquivo)
        arquivo.close()
except Exception as e:
    print(f"Erro iniciando o assistente: {str(e)}")

# Iterar sobre as ações e acessar o item "chamado"
for index, acao in enumerate(dados["acoes"], start=1):
    item_chamado = acao["objetos"][0]
    print(f"Ação {index}: {acao['nome']} - Item: {item_chamado}")
