def iniciar_chamado():
    return None

def atuar_sobre_o_chamado(acao, objeto, parametro_de_atuacao):
    if acao in ["atender"] and objeto == "chamado":
        print("atendendo chamado")
    elif acao in ["esperar"] and objeto == "chamado":
        print("chamado em espera")
    elif acao in ["aguardando"] and objeto == "chamado":
        print("chamado aguardando peça")
    elif acao in ["finalizar"] and objeto == "chamado":
        print("finalizando o chamado")
    elif acao in ["parecer"] and objeto == "chamado":
        print("Parecer técnico do chamado")