
def BL(grafo, noInicial, noObjetivo): 
    # Lista que contém os próximos nós a serem visitados, implementados como FIFO
    fila = [noInicial]
    # Lista que contém os nós que já foram visitados, inicialmente ninguem foi visitado
    visitado = []
    # Executa até que a fila esteja vazia ou no objetivo seja encontrado
    while fila: 
       # Pega o primeiro nó da fila
        no = fila.pop(0)
        # Adiciona o nó atual na lista de visitado, se ainda não estiver no visitado
        if no not in visitado:
            visitado.append(no)
            print(visitado)
        # Retorna a lista de visitados se encontrou o no objetivo    
        if no == noObjetivo:
            print("Fim da busca, achou o no objetivo:", no)
            return visitado
        else:
            # Caso contrário, adicione os nós vizinhos no final da fila
            for visinhos in grafo[no]:
                if visinhos not in visitado:
                    fila.append(visinhos)

    return visitado

if __name__ == '__main__':
    #Um dicionario representando o grafo com uma lista de adjacencia, onde cada vertice está armazenando o vertice adjacente
    grafo = {

    'B1':['Biblioteca','BE'],
    'B2':['B1','BF'],
    'B3':['B2','Cuica','BG','Reitoria'], 
    'BB':['BD','BC','LabJornalismo'],
    'BC':['BD','BB'],
    'BD':['BC','BB'],
    'BE':['B1','BalaI'],
    'BF':['BE','B2'],
    'BG':['Reitoria','B3','Lab1'],
    'BH':['Cuica','BI','BJ'],
    'BI':['BH','BJ'],
    'BJ':['BH','BI','RU'],
    'Lab1':['BG','Reitoria','Lab2'],
    'Lab2':['Lab1'],
    'Lab3':['Lab2'],
    'LabJornalismo':['BB','LabNutricao'],
    'LabNutricao':['LabJornalismo','LabEngenharia'],
    'LabEngenharia':['LabNutricao','UMA'],
    'Biblioteca':['B1','BD'],
    'BalaI':['BF','BalaII'],
    'BalaII':['BalaI','RU'],
    'Cuica':['B3','BH'],
    'UFTFM':['UMA','RU'],
    'RU':['BJ','BalaII','UFTFM'],
    'Reitoria':['B3','BG','Lab1'],
    'UMA':['LabEngenharia','UFTFM']

    }

    noInicial = "B3"
    noObjetivo = "RU"

    resultado = BL(grafo, noInicial, noObjetivo)
    print("\nO caminho da busca de", noInicial, "ate", noObjetivo, ":", resultado)
    
