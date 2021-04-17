import json
import re
from operator import itemgetter

def array_jobs(arquivo, janela_inicio, janela_fim, horas_bloco_de_intervalo=8):
    """
    Retorna um array de execução de job dentro de uma janela.
    Cada array tem o limite máximo de execução de 8 horas (padrão), podendo ser alterado

    arquivo = "dados.json"
    janela_inicio = "2019-11-10 09:00:00"
    janela_fim = "2019-11-11 12:00:00"

    >>> array_jobs("dados/dados_01.json", "2019-11-10 09:00:00", "2019-11-11 12:00:00", 8)
    [[1, 3], [2]]

    >>> array_jobs("dados/dados_02.json", "2019-11-10 09:00:00", "2019-11-11 12:00:00")
    [[1, 5], [3, 8, 9], [11, 12, 2], [10]]
    """
    dados = open(arquivo).read()
    dados_json = json.loads(dados)
    dados_ordenados = sorted(dados_json, key=itemgetter("Data Máxima de conclusão", "Tempo estimado"))

    #print(f"Janela inicio: {janela_inicio} - Janela Fim: {janela_fim}")
    resultado = []
    bloco = []
    tempo_execucao = 0

    for job in dados_ordenados:
        if janela_inicio <= job["Data Máxima de conclusão"] <= janela_fim:
            tempo = re.match("^[0-9]+", job["Tempo estimado"])
            tempo_estimado = int(tempo.group(0))
            if tempo_estimado <= horas_bloco_de_intervalo:
                if (tempo_execucao + tempo_estimado) <= horas_bloco_de_intervalo:
                    tempo_execucao = tempo_execucao + tempo_estimado
                    bloco.append(job["ID"])
                else:
                    resultado.append(bloco)
                    bloco = []
                    tempo_execucao = tempo_estimado
                    bloco.append(job["ID"])
    resultado.append(bloco)

    print(json.dumps(resultado))

if __name__ == "__main__":
    import doctest
    import sys

    doctest.testmod()

    if len(sys.argv) != 4:
        print(f"Favor informar os campos na seguinte ordem: {sys.argv[0]} <arquivo> <janela inicio> <janela fim>")
        exit(1)
    array_jobs(sys.argv[1], sys.argv[2], sys.argv[3])