# Funções para cada camada do modelo OSI

# def define função: def_nome(parametros):
# dado é o que a função recebe pra trabalhar: a função aplicacao espera receber um valor chamado dado (a entrada)
# dentro da função, usamos esse valor pra contruir a saída

# return indica o que a função vai entregar de volta
# Em [] é um texto fixo (obs: as [] é apenas para marcar as etiuetas) e {dado} é substituído pelo valor ue foi passado como parâmetro

def aplicacao(dado):
    return f"[APLICAÇÃO]: {dado}"

def apresentacao(dado):
    return f"[APRESENTAÇÃO]: {dado}"

def sessao(dado):
    return f"[SESSÃO]: {dado}"

def transporte(dado):
    return f"[TRANSPORTE]: {dado}"

def rede(dado, origem, destino):
    return f"[REDE: Origem={origem}, Destino={destino}] {dado}"

def enlace(dado):
    return f"[ENLACE]: {dado}"

def fisica(dado):
    # Converte todo o quadro para binário
    # ''.join(...) junta os pedaços de binário em uma string
    # format(ord(c), '08b') converte o número para binário com 8 bits
    # for c in dado percorre cada caractere dentro da string dado
    binario = ''.join(format(ord(c), '08b') for c in dado)
    return f"[FÍSICA]: {binario}"

# Funções de desencapsulamento (recepção)
# Abre dados até chegar no conteúdo original
def desfisica(dado_binario):
    # Converte binário de volta para texto
    texto = ''.join(chr(int(dado_binario[i:i+8], 2)) for i in range(0, len(dado_binario), 8))
    return texto.replace("[FÍSICA]: ", "")

def desenlace(dado):
    return dado.replace("[ENLACE]: ", "")

def derede(dado):
    # Remove cabeçalho da rede
    inicio = dado.find("]") + 1
    return dado[inicio:].strip()

def detransporte(dado):
    return dado.replace("[TRANSPORTE]: ", "")

def dessessao(dado):
    return dado.replace("[SESSÃO]: ", "")

def desapresentacao(dado):
    return dado.replace("[APRESENTAÇÃO]: ", "")

def desaplicacao(dado):
    return dado.replace("[APLICAÇÃO]: ", "")

# Simulação de envio
print("=== ENVIO ===")
origem = "#B"
destino = "9g"
dado = "A"

camada1 = aplicacao(dado)
print(camada1)

camada2 = apresentacao(camada1)
print(camada2)

camada3 = sessao(camada2)
print(camada3)

camada4 = transporte(camada3)
print(camada4)

camada5 = rede(camada4, origem, destino)
print(camada5)

camada6 = enlace(camada5)
print(camada6)

camada7 = fisica(camada6)
print(camada7)

# Simulação de recepção
print("\n=== RECEPÇÃO ===")

# Desencapsulamento inverso
recebido = desfisica(camada7.replace("[FÍSICA]: ", ""))
print(recebido)

recebido = desenlace(recebido)
print(recebido)

recebido = derede(recebido)
print(recebido)

recebido = detransporte(recebido)
print(recebido)

recebido = dessessao(recebido)
print(recebido)

recebido = desapresentacao(recebido)
print(recebido)

recebido = desaplicacao(recebido)
print(recebido)

print(f"\nMensagem final recebida pelo dispositivo {destino}: {recebido}")
