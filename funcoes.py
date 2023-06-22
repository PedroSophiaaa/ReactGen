from grupos_funcionais import grupos_funcionais, detector_de_grupos_funcionais, seletor_de_grupos_funcionais, grupo_funcional_aleatorio

def fitness(dic_ind, mol):
    """Utilizada para gerar o score de um indivíduo seguindo suposições químicas (não necessariamente precisas e talvez até duvidosas).
    Suposições qúimicas:
        - O número de grupos funcionais de um mesmo tipo em uma molécula é inversamente proporcional ao score do indivíduo;
        - A área de superfície do indivíduo deve ser próxima da área de superfície do grupo funcional presente na molécula de interesse, tal como o LogP e polaridade;
        - O número de anéis aromáticos é inversamente proporcional ao score do indivíduo;
        - Quanto maior o raio molecular e a massa molecular mais difícil é para o indivíduo se ligar à molécula de interesse;
        - A densidade de carga do indivíduo deve ser igual à densidade de carga do grupo funcional da molécula de interesse multiplicada de -1, a fim de equilibrar as cargas do sistema.
    
    Args:
        dic_ind: dicionário com as informações do indivíduo
        mol: nome da molécula de interesse
        
    Return:
        O score do indivíduo (grupo funcional) ao pensar no quesito de reação com a molécula de interesse"""
    
    dic_mol = seletor_de_grupos_funcionais(detector_de_grupos_funcionais(mol))
    
    dic_scores = {}

    grupo = list(dic_ind.keys())[0]

    massa_molecular_ind = dic_ind[grupo]["Massa Molecular"]
    area_de_superfície_ind = dic_ind[grupo]["Área de Superfície"]
    logP_ind = dic_ind[grupo]["LogP"]
    aneis_aromáticos_ind = dic_ind[grupo]["Anéis Aromáticos"]
    polaridade_ind = dic_ind[grupo]["Polaridade"]
    raio_molecular_ind = dic_ind[grupo]["Raio Molecular"]
    densidade_de_carga_ind = dic_ind[grupo]["Densidade de carga"]

    for i in dic_mol:
        area_de_superfície_mol = dic_mol[i]["Área de Superfície"]
        logP_mol = dic_mol[i]["LogP"]
        polaridade_mol = dic_mol[i]["Polaridade"]
        densidade_de_carga_mol = dic_mol[i]["Densidade de carga"]
        numero_mol = dic_mol[i]["Número"]

        dic_scores[i] =  1 / (numero_mol*(1 + aneis_aromáticos_ind)*(1 + raio_molecular_ind + massa_molecular_ind + abs(area_de_superfície_mol - area_de_superfície_ind) + abs(logP_mol - logP_ind) + 10*abs(polaridade_mol - polaridade_ind) + 20*(densidade_de_carga_ind + densidade_de_carga_mol)))

    max_score_key = max(dic_scores, key=dic_scores.get)
    max_score_value = max(dic_scores.values())

    best_score = (max_score_key, max_score_value)

    return best_score

def new_ind(max_groups, grupos_f=grupos_funcionais):
    """Gera um novo indivíduo válido. Consideraremos que as propriedades do indivíduo serão a média ponderada das propriedades dos grupos presentes na molécula.
    Args:
        max_groups: máximo de grupos funcionais
    Return:
        Um dicionário com uma lista representando os grupos funcionais  com as propriedades do indivíduo. Cada indivíduo será uma molécula com esses grupos funcionais.
    """
    ind_dic = {}

    for i in range(max_groups):
        curr_group = grupo_funcional_aleatorio()
        ind_dic[i] = {}
        ind_dic[i][curr_group] = None#

    return ind_dic

def new_pop(tampop, mol):
    """Gera uma nova população aleatória.
    Args:
        tampop: tamanho da população
        mol: molécula desejada
    Return:
        Um dicionário com tag, indivíduo e fitness.
    """
    dicio_pop = {} #Define o dicionário contendo os indivíduos

    for i in range(tampop):
        curr_ind = grupo_funcional_aleatorio()
        dicio_pop[i+1] = { #Armazena o valor da função objetivo correspondente a cada indivíduo
            'tag': i+1,
            'ind': curr_ind,
            'fitness': fitness(curr_ind, mol)}
    return dicio_pop