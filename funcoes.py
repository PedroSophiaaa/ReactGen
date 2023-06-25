from grupos_funcionais import grupos_funcionais, detector_de_grupos_funcionais, seletor_de_grupos_funcionais, grupo_funcional_aleatorio
import random as rd
import copy


#########################
#        Objetivo       #
#########################

def fitness(dic_ind, mol):
    """Utilizada para gerar o score de um indivíduo seguindo suposições químicas (não necessariamente precisas e talvez até duvidosas).
    Suposições qúimicas:
        - O número de grupos funcionais de um mesmo tipo em uma molécula é inversamente proporcional ao score do indivíduo;
        - A área de superfície do indivíduo deve ser próxima da área de superfície do grupo funcional presente na molécula de interesse, tal como o LogP e polaridade;
        - O número de anéis aromáticos é inversamente proporcional ao score do indivíduo;
        - Quanto maior o raio molecular e a massa molecular mais difícil é para o indivíduo se ligar à molécula de interesse;
        - A densidade de carga do indivíduo deve ser igual à densidade de carga do grupo funcional da molécula de interesse multiplicada de -1, a fim de equilibrar as cargas do sistema.
    
    Args:
        ind: dicionário com as informações do indivíduo
        mol: nome da molécula de interesse
        
    Return:
        O score do indivíduo (grupo funcional) ao pensar no quesito de reação com a molécula de interesse"""
    
    dic_mol = seletor_de_grupos_funcionais(detector_de_grupos_funcionais(mol))
    
    dic_scores = {}

    grupo = "Propriedades"

    massa_molecular_ind = dic_ind[grupo]["Massa Molecular"]
    area_de_superfície_ind = dic_ind[grupo]["Área de Superfície"]
    logP_ind = dic_ind[grupo]["LogP"]
    aneis_aromáticos_ind = dic_ind[grupo]["Anéis Aromáticos"]
    polaridade_ind = dic_ind[grupo]["Polaridade"]
    raio_molecular_ind = dic_ind[grupo]["Raio Molecular"]
    densidade_de_carga_ind = dic_ind[grupo]["Densidade de carga"]

    if dic_mol == {}:
        raise Exception("A molécula não possui grupos funcionais aceitos pelo código.")
    
    else:
        for i in dic_mol:
            area_de_superfície_mol = dic_mol[i]["Área de Superfície"]
            logP_mol = dic_mol[i]["LogP"]
            polaridade_mol = dic_mol[i]["Polaridade"]
            densidade_de_carga_mol = dic_mol[i]["Densidade de carga"]
            numero_mol = dic_mol[i]["Número"]

            diff_area = abs(area_de_superfície_mol - area_de_superfície_ind)
            diff_logp = abs(logP_mol - logP_ind)
            diff_polaridade = abs(polaridade_mol - polaridade_ind)
            diff_carga = abs(densidade_de_carga_mol - (-1*densidade_de_carga_ind))

            curr_score = 1 / ((numero_mol * (1 + aneis_aromáticos_ind) * (1 + diff_area*diff_logp*diff_polaridade*diff_carga)) + raio_molecular_ind + massa_molecular_ind)

            dic_scores[i] =  curr_score

        max_score_key = max(dic_scores, key=dic_scores.get)
        max_score_value = max(dic_scores.values())

        best_score = (max_score_key, max_score_value)

        return best_score


#########################
#       Individuo       #
#########################

def new_ind(max_groups, grupos_f=grupos_funcionais):
    """Gera um novo indivíduo (molécula) válido. Consideraremos que as propriedades do indivíduo serão a média ponderada das propriedades dos grupos presentes na molécula.
    Args:
        max_groups: máximo de grupos funcionais
    Return:
        Um dicionário com uma lista representando os grupos funcionais  com as propriedades do indivíduo. Cada indivíduo será uma molécula com esses grupos funcionais.
    """
    ind_dic = {}

    num_groups = rd.randint(1, max_groups)

    for _ in range(num_groups):
        curr_group = grupo_funcional_aleatorio(grupos_f)
        ind_dic.update(curr_group)

    lista_propriedades = list(list(curr_group.values())[0].keys())

    dic_propriedades = {}

    for i in lista_propriedades:
        dic_propriedades[i] = []
        for u in ind_dic:
            dic_propriedades[i].append(ind_dic[u][i])

    ind_dic["Propriedades"] = {}

    for i in dic_propriedades:
        media_propriedades = sum(dic_propriedades[i])/len(dic_propriedades[i])
        ind_dic["Propriedades"][i] = media_propriedades

    return ind_dic


#########################
#       População       #
#########################

def new_pop(tampop, max_groups, mol):
    """Gera uma nova população aleatória.
    Args:
        tampop: tamanho da população
        max_groups: máximo de grupos funcionais por indivíduo
        mol: molécula desejada
    Return:
        Um dicionário com tag, indivíduo e fitness.
    """
    dicio_pop = {} #Define o dicionário contendo os indivíduos

    for i in range(tampop):
        curr_ind = new_ind(max_groups)
        dicio_pop[i+1] = { #Armazena o valor da função objetivo correspondente a cada indivíduo
            'tag': i+1,
            'ind': curr_ind,
            'fitness': fitness(curr_ind, mol)}
    return dicio_pop


#########################
#        Mutação        #
#########################

def mutacao(ind, pm):
    """Realiza a mutação de um indivíduo, respeitando o fator pm
    
    Args:
        ind: indivíduo a ser mutado
        pm: probabilidade de mutação
        
    Returns:
        indivíduo mutado"""
    
    ind_init = copy.deepcopy(ind)

    for i in ind_init['ind']:
        if i != "Propriedades":
            mut = rd.random()
            if mut < pm:
                ind['ind'].pop(i)
                novo_grupo_aleatorio = grupo_funcional_aleatorio()
                ind['ind'].update(novo_grupo_aleatorio)

                ind['ind'].pop('Propriedades')

                lista_propriedades = list(list(novo_grupo_aleatorio.values())[0].keys())

                dic_propriedades = {}

                for i in lista_propriedades:
                    dic_propriedades[i] = []
                    for u in ind['ind']:
                        dic_propriedades[i].append(ind['ind'][u][i])

                ind['ind']["Propriedades"] = {}

                for i in dic_propriedades:
                    media_propriedades = sum(dic_propriedades[i])/len(dic_propriedades[i])
                    ind['ind']["Propriedades"][i] = media_propriedades

    return ind


#########################
#      Cruzamentos      #
#########################

def crossover(p1_ori, p2_ori, pc):
    """Realiza o cruzamento entre 2 pais, respeitando o fator pc
    
    Args:
        p1: pai1
        p2: pai2
        pc: probabilidade de cruzamento
        
    Return:
        Lista contendo os 2 indivíduos filhos"""
    
    p1 = copy.deepcopy(p1_ori)
    p2 = copy.deepcopy(p2_ori)

    p1.pop('Propriedades')
    p2.pop('Propriedades')

    c1 = {}
    c2 = {}
    cross = rd.random()
    if cross < pc:
        max_crosspoint = min(len(p1), len(p2))

        if (len(p1) == 1) and (len(p2) == 1):
            c1 = p1
            c2 = p2
        else:
            cross_point = rd.randint(1, max_crosspoint)

            grupos_p1 = list(p1.keys())
            grupos_p2 = list(p2.keys())

            c = 0
            for _ in range(len(grupos_p1)):
                if c < cross_point:
                    c1[grupos_p2[c]] = p2[grupos_p2[c]]
                else:
                    c1[grupos_p1[c]] = p1[grupos_p1[c]]

                c += 1

            c = 0
            for _ in range(len(grupos_p2)):
                if c < cross_point:
                    c2[grupos_p1[c]] = p1[grupos_p1[c]]
                else:
                    c2[grupos_p2[c]] = p2[grupos_p2[c]]

                c += 1
    else:
        c1 = p1
        c2 = p2

    lista_propriedades = list(p1[list(p1.keys())[0]].keys())


    dic_propriedades = {}

    for i in lista_propriedades:
        dic_propriedades[i] = []
        for u in c1:
            dic_propriedades[i].append(c1[u][i])

    c1["Propriedades"] = {}

    for i in dic_propriedades:
        media_propriedades = sum(dic_propriedades[i])/len(dic_propriedades[i])
        c1["Propriedades"][i] = media_propriedades


    dic_propriedades = {}

    for i in lista_propriedades:
        dic_propriedades[i] = []
        for u in c2:
            dic_propriedades[i].append(c2[u][i])

    c2["Propriedades"] = {}

    for i in dic_propriedades:
        media_propriedades = sum(dic_propriedades[i])/len(dic_propriedades[i])
        c2["Propriedades"][i] = media_propriedades


    return [c1,c2]


#########################
#        Seleção        #
#########################

def roull_sel_max(pop):
    """Seleciona os individuos de uma população pelo método da roleta para problemas de maximização.
    
    Args:
      pop: dicionário com todos os individuos da população e seus valores da funcao objetivo
    
    Return:
      Dicionário com a população dos indivíduos selecionados, a tag e o fitness.
    """
    fitness = [pop[i]['fitness'][1] for i in pop]
    all_zero = True
    for i in fitness:
        if i != 0:
            all_zero = False
            break
    if all_zero == True:
        for i in range(len(fitness)):
            fitness[i] = 1
    pop_list = [pop[j]['ind'] for j in pop]
    populacao_selecionada = rd.choices(pop_list, weights=fitness, k=len(pop_list))
    pop_dic = {}
    for i in range(len(populacao_selecionada)):
        pop_dic[i+1] = {
            'tag': i+1,
            'ind': populacao_selecionada[i]}
    return pop_dic

