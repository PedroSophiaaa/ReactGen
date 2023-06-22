from grupos_funcionais import grupos_funcionais, detector_de_grupos_funcionais, seletor_de_grupos_funcionais, grupo_funcional_aleatorio
import random

def fitness(pop, mol):
    """Utilizada para gerar o score de um indivíduo seguindo suposições químicas (não necessariamente precisas e talvez até duvidosas).
    Suposições qúimicas:
        - O número de grupos funcionais de um mesmo tipo em uma molécula é inversamente proporcional ao score do indivíduo;
        - A área de superfície do indivíduo deve ser próxima da área de superfície do grupo funcional presente na molécula de interesse, tal como o LogP e polaridade;
        - O número de anéis aromáticos é inversamente proporcional ao score do indivíduo;
        - Quanto maior o raio molecular e a massa molecular mais difícil é para o indivíduo se ligar à molécula de interesse;
        - A densidade de carga do indivíduo deve ser igual à densidade de carga do grupo funcional da molécula de interesse multiplicada de -1, a fim de equilibrar as cargas do sistema.
    
    Args:
        pop: lista de dicionário com as informações do indivíduo
        mol: nome da molécula de interesse
        
    Return:
        O score do indivíduo (grupo funcional) ao pensar no quesito de reação com a molécula de interesse"""
    
    dic_mol = seletor_de_grupos_funcionais(detector_de_grupos_funcionais(mol))
    fitness_populacao =[]
    for dic_ind in pop:
        fitness_individuo =[]
        for chave_dict in dic_ind.keys():
            dic_scores = {}

            grupo = list(dic_ind[chave_dict].keys())[0]

            massa_molecular_ind = dic_ind[chave_dict][grupo]["Massa Molecular"]
            area_de_superfície_ind = dic_ind[chave_dict][grupo]["Área de Superfície"]
            logP_ind = dic_ind[chave_dict][grupo]["LogP"]
            aneis_aromáticos_ind = dic_ind[chave_dict][grupo]["Anéis Aromáticos"]
            polaridade_ind = dic_ind[chave_dict][grupo]["Polaridade"]
            raio_molecular_ind = dic_ind[chave_dict][grupo]["Raio Molecular"]
            densidade_de_carga_ind = dic_ind[chave_dict][grupo]["Densidade de carga"]

            for i in dic_mol:
                area_de_superfície_mol = dic_mol[i]["Área de Superfície"]
                logP_mol = dic_mol[i]["LogP"]
                polaridade_mol = dic_mol[i]["Polaridade"]
                densidade_de_carga_mol = dic_mol[i]["Densidade de carga"]
                numero_mol = dic_mol[i]["Número"]

                dic_scores[i] =  1 / (numero_mol*(1 + aneis_aromáticos_ind)*(1 + raio_molecular_ind + massa_molecular_ind + abs(area_de_superfície_mol - area_de_superfície_ind) + abs(logP_mol - logP_ind) + 10*abs(polaridade_mol - polaridade_ind) + 20*(densidade_de_carga_ind + densidade_de_carga_mol)))

            max_score_key = max(dic_scores, key=dic_scores.get)
            max_score_value = max(dic_scores.values())

            best_score = (grupo,max_score_key, max_score_value)
            fitness_individuo.append(best_score)
        fitness_individuo.append(("Soma: ",sum([item[2] for item in fitness_individuo])))
        fitness_populacao.append(fitness_individuo)
    return fitness_populacao

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
        ind_dic[i]=curr_group

    return ind_dic

def new_pop(tampop,max_groups):
    """Gera uma nova população aleatória.
    Args:
        tampop: tamanho da população
        max_groups: máximo de grupos funcionais
    Return:
        Uma lista de individuos
    """
    lista_pop = [] #Define o dicionário contendo os indivíduos

    for i in range(tampop):
        curr_ind = new_ind(max_groups)
        lista_pop.append(curr_ind)
    return lista_pop

def mutacao(indivíduo):
    """Realiza a mutação de um gene no problema

    Args:
        indivíduo: uma lista representando um individuo no problema.

    Return:
        Um individuo com um gene mutado.
    """
    gene_a_ser_mutado = random.randint(0, len(indivíduo) - 1)
    indivíduo[gene_a_ser_mutado] = grupo_funcional_aleatorio()
    return indivíduo

def cruzamento_ponto_simples(pai, mãe):
    """Operador de cruzamento de ponto simples.

    Args:
        pai: uma lista representando um individuo.
        mãe: uma lista representando um individuo.

    Returns:
        Duas listas, sendo que cada uma representa um filho dos pais que foram os argumentos.
    """

    ponto_de_corte = random.randint(1, len(pai) - 1)
    filho1 = pai[:ponto_de_corte] + mãe[ponto_de_corte:]
    filho2 = mãe[:ponto_de_corte] + pai[ponto_de_corte:]

    return filho1, filho2