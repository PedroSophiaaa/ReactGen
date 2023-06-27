import random as rd
import copy

import pubchempy as pcp

from rdkit import Chem
from rdkit.Chem import Fragments

my_seed = 32 # Seed aleatória contendo valores aleatórios das propriedades

rd.seed(my_seed)

#########################
#   Grupos funcionais   #
#########################

grupos_funcionais = {
        "Ácidos carboxilicos alifáticos": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10),
        },
        "Hidroxilas alifáticas": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Hidroxilas alifáticas excluindo tert-OH": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Grupos funcionais N ligado à aromáticos": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Ácidos carboxilicos aromáticos": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Nitrogênios aromáticos": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Aminas aromáticas": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Hidroxilas aromáticas": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Ácidos carboxilicos": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Ácidos carboxílicos": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Carbonilas O": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Carbonilas O excluindo COOH": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Tiocarbonilas": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "C(OH)CCN-Ctert-alkyl ou C(OH)CCNcyclic": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Iminas": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Aminas": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Aminas secundárias": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Aminas primárias": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Hidroxilaminas": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "XCCNR": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Aminas terc-alicíclicas": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Nitrogênios H-Pirrol": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Grupos tiol": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Aldeídos": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Alquil carbamatos (sujeitos a hidrólise)": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Haletos de alquila": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Isotiocianatos": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Sítios de oxidação alílica excluindo dienona esteróide": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Amidas": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Grupos de amidina": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Anilinas": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Sítios aril metil para hidroxilação": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Azidas": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Grupos azo": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Grupos de barbitúricos": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Anéis de benzeno": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Benzodiazepínicos sem anéis fundidos adicionais": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Biciclicos": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Grupos diazo": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Diidropiridinas": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Anéis de expóxido": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Ésters": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Éters": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Furano": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Grupos guanidina": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Halogênios": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Grupos de hidrazina": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Grupos de hidrazona": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Anéis de imidazol": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Grupos imide": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Isocianatos": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Tioéteres": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Cetonas": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Cetonas excluindo diaril, a,b-insat. dienonas, heteroátomo em Calpha": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Beta lactâmicos": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Ésteres cíclicos (lactonas)": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Grupos metoxi -OCH3": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Anéis de morfolina": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Nitrilos": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Grupos nitro": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Substituintes do anel nitro benzeno": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Substituintes do anel nitro benzeno não orto": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Grupos nitroso excluindo NO2": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Anéis de oxazol": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Grupos oxima": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Locais de para-hidroxilação": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Fenóis": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "OH fenólico excluindo substituintes Hbond intramoleculares orto": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Grupos de ácido fosfórico": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Grupos éster fosfórico": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Anéis de piperdina": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Anéis de piperzina": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Amidas primárias": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Sulfonamidas primárias": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Anéis de piridina": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Nitrogênios quaternários": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Sulfonamidas": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Grupos sulfona": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Acetilenos terminais": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Anéis de tetrazol": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Anéis tiazólicos": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Tiocianatos": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Anéis de tiofeno": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Alcanos não ramificados de pelo menos 4 membros (exclui alcanos halogenados)": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
        "Grupos de ureia": {
            "Massa Molecular": rd.uniform(0.5, 50),
            "Área de Superfície": rd.uniform(0.1, 5),
            "LogP": rd.random(),
            "Anéis Aromáticos": rd.randint(0, 5),
            "Polaridade": rd.uniform(0, 300),
            "Raio Molecular": rd.randint(0, 100),
            "Densidade de carga": rd.randint(-10,10)
        },
    }


#########################
#   Gerador aleatório   #
#########################

def grupo_funcional_aleatorio(grupos_f=grupos_funcionais):
    """ Função que computa um grupo funcional aleatório a partir de grupos funcionais disponíveis
    
    Args:
        grupos_f: Grupos funcionais disponíveis a serem sorteados
        
    Returns:
        Um grupo funcional escolhido dentre todos possíveis
    """
    lista_grupos = list(grupos_f.keys()) # Nomes dos grupos funcionais da lista de grupos funcionais
    grupo = rd.choice(lista_grupos) # Escolha aleatória de um grupo da lista de grupos

    grupo_dic = {}
    grupo_dic[grupo] = {}

    for i in grupos_f[grupo]:
        grupo_dic[grupo][i] = grupos_f[grupo][i]

    return grupo_dic


#########################
#   Detector de grupos  #
#########################

def detector_de_grupos_funcionais(mol_name):
    """ Função a qual detecta grupos funcionais presentes em moléculas obtidas pelo pubchempy, através de seu nome
    
    Args:
        mol_name: O nome da molécula a qual desejamos encontrar seus grupos funcionais
    
    Returns:
        Grupos funcionais que foram encontrados na molécula requisitada
    """
    compound = pcp.get_compounds(mol_name, "name") # Obtenção dos compostos da molécula na biblioteca pubchempy, a partir de seu nome

    mol = Chem.MolFromSmiles(compound[0].isomeric_smiles) # Através de seu nome, encontramos o seu SMILES na forma isomérica

    grupos_funcionais_mol = copy.deepcopy(grupos_funcionais)

    grupos_funcionais_mol["Ácidos carboxilicos alifáticos"]["Número"] = Fragments.fr_Al_COO(mol)
    grupos_funcionais_mol["Hidroxilas alifáticas"]["Número"] = Fragments.fr_Al_OH(mol)
    grupos_funcionais_mol["Hidroxilas alifáticas excluindo tert-OH"]["Número"] = Fragments.fr_Al_OH_noTert(mol)
    grupos_funcionais_mol["Grupos funcionais N ligado à aromáticos"]["Número"] = Fragments.fr_ArN(mol)
    grupos_funcionais_mol["Ácidos carboxilicos aromáticos"]["Número"] = Fragments.fr_Ar_COO(mol)
    grupos_funcionais_mol["Nitrogênios aromáticos"]["Número"] = Fragments.fr_Ar_N(mol)
    grupos_funcionais_mol["Aminas aromáticas"]["Número"] = Fragments.fr_Ar_NH(mol)
    grupos_funcionais_mol["Hidroxilas aromáticas"]["Número"] = Fragments.fr_Ar_OH(mol)
    grupos_funcionais_mol["Ácidos carboxilicos"]["Número"] = Fragments.fr_COO(mol)
    grupos_funcionais_mol["Ácidos carboxílicos"]["Número"] = Fragments.fr_COO2(mol)
    grupos_funcionais_mol["Carbonilas O"]["Número"] = Fragments.fr_C_O(mol)
    grupos_funcionais_mol["Carbonilas O excluindo COOH"]["Número"] = Fragments.fr_C_O_noCOO(mol)
    grupos_funcionais_mol["Tiocarbonilas"]["Número"] = Fragments.fr_C_S(mol)
    grupos_funcionais_mol["C(OH)CCN-Ctert-alkyl ou C(OH)CCNcyclic"]["Número"] = Fragments.fr_HOCCN(mol)
    grupos_funcionais_mol["Iminas"]["Número"] = Fragments.fr_Imine(mol)
    grupos_funcionais_mol["Aminas"]["Número"] = Fragments.fr_NH0(mol)
    grupos_funcionais_mol["Aminas secundárias"]["Número"] = Fragments.fr_NH1(mol)
    grupos_funcionais_mol["Aminas primárias"]["Número"] = Fragments.fr_NH2(mol)
    grupos_funcionais_mol["Hidroxilaminas"]["Número"] = Fragments.fr_N_O(mol)
    grupos_funcionais_mol["XCCNR"]["Número"] = Fragments.fr_Ndealkylation1(mol)
    grupos_funcionais_mol["Aminas terc-alicíclicas"]["Número"] = Fragments.fr_Ndealkylation2(mol)
    grupos_funcionais_mol["Nitrogênios H-Pirrol"]["Número"] = Fragments.fr_Nhpyrrole(mol)
    grupos_funcionais_mol["Grupos tiol"]["Número"] = Fragments.fr_SH(mol)
    grupos_funcionais_mol["Aldeídos"]["Número"] = Fragments.fr_aldehyde(mol)
    grupos_funcionais_mol["Alquil carbamatos (sujeitos a hidrólise)"]["Número"] =  Fragments.fr_alkyl_carbamate(mol)
    grupos_funcionais_mol["Haletos de alquila"]["Número"] = Fragments.fr_alkyl_halide(mol)
    grupos_funcionais_mol["Isotiocianatos"]["Número"] = Fragments.fr_isothiocyan(mol)
    grupos_funcionais_mol["Sítios de oxidação alílica excluindo dienona esteróide"]["Número"] = Fragments.fr_allylic_oxid(mol)
    grupos_funcionais_mol["Amidas"]["Número"] = Fragments.fr_amide(mol)
    grupos_funcionais_mol["Grupos de amidina"]["Número"] = Fragments.fr_amidine(mol)
    grupos_funcionais_mol["Anilinas"]["Número"] = Fragments.fr_aniline(mol)
    grupos_funcionais_mol["Sítios aril metil para hidroxilação"]["Número"] = Fragments.fr_aryl_methyl(mol)
    grupos_funcionais_mol["Azidas"]["Número"] = Fragments.fr_azide(mol)
    grupos_funcionais_mol["Grupos azo"]["Número"] = Fragments.fr_azo(mol)
    grupos_funcionais_mol["Grupos de barbitúricos"]["Número"] = Fragments.fr_barbitur(mol)
    grupos_funcionais_mol["Anéis de benzeno"]["Número"] = Fragments.fr_benzene(mol)
    grupos_funcionais_mol["Benzodiazepínicos sem anéis fundidos adicionais"]["Número"] = Fragments.fr_benzodiazepine(mol)
    grupos_funcionais_mol["Biciclicos"]["Número"] = Fragments.fr_bicyclic(mol)
    grupos_funcionais_mol["Grupos diazo"]["Número"] = Fragments.fr_diazo(mol)
    grupos_funcionais_mol["Diidropiridinas"]["Número"] = Fragments.fr_dihydropyridine(mol)
    grupos_funcionais_mol["Anéis de expóxido"]["Número"] = Fragments.fr_epoxide(mol)
    grupos_funcionais_mol["Ésters"]["Número"] = Fragments.fr_ester(mol)
    grupos_funcionais_mol["Éters"]["Número"] = Fragments.fr_ether(mol)
    grupos_funcionais_mol["Furano"]["Número"] = Fragments.fr_furan(mol)
    grupos_funcionais_mol["Grupos guanidina"]["Número"] = Fragments.fr_guanido(mol)
    grupos_funcionais_mol["Halogênios"]["Número"] = Fragments.fr_halogen(mol)
    grupos_funcionais_mol["Grupos de hidrazina"]["Número"] = Fragments.fr_hdrzine(mol)
    grupos_funcionais_mol["Grupos de hidrazona"]["Número"] = Fragments.fr_hdrzone(mol)
    grupos_funcionais_mol["Anéis de imidazol"]["Número"] = Fragments.fr_imidazole(mol)
    grupos_funcionais_mol["Grupos imide"]["Número"] = Fragments.fr_imide(mol)
    grupos_funcionais_mol["Isocianatos"]["Número"] = Fragments.fr_isocyan(mol)
    grupos_funcionais_mol["Tioéteres"]["Número"] = Fragments.fr_sulfide(mol)
    grupos_funcionais_mol["Cetonas"]["Número"] = Fragments.fr_ketone(mol)
    grupos_funcionais_mol["Cetonas excluindo diaril, a,b-insat. dienonas, heteroátomo em Calpha"]["Número"] = Fragments.fr_ketone_Topliss(mol)
    grupos_funcionais_mol["Beta lactâmicos"]["Número"] = Fragments.fr_lactam(mol)
    grupos_funcionais_mol["Ésteres cíclicos (lactonas)"]["Número"] =  Fragments.fr_lactone(mol)
    grupos_funcionais_mol["Grupos metoxi -OCH3"]["Número"] = Fragments.fr_methoxy(mol)
    grupos_funcionais_mol["Anéis de morfolina"]["Número"] = Fragments.fr_morpholine(mol)
    grupos_funcionais_mol["Nitrilos"]["Número"] = Fragments.fr_nitrile(mol)
    grupos_funcionais_mol["Grupos nitro"]["Número"] = Fragments.fr_nitro(mol)
    grupos_funcionais_mol["Substituintes do anel nitro benzeno"]["Número"] = Fragments.fr_nitro_arom(mol)
    grupos_funcionais_mol["Substituintes do anel nitro benzeno não orto"]["Número"] = Fragments.fr_nitro_arom_nonortho(mol)
    grupos_funcionais_mol["Grupos nitroso excluindo NO2"]["Número"] = Fragments.fr_nitroso(mol)
    grupos_funcionais_mol["Anéis de oxazol"]["Número"] = Fragments.fr_oxazole(mol)
    grupos_funcionais_mol["Grupos oxima"]["Número"] = Fragments.fr_oxime(mol)
    grupos_funcionais_mol["Locais de para-hidroxilação"]["Número"] = Fragments.fr_para_hydroxylation(mol)
    grupos_funcionais_mol["Fenóis"]["Número"] = Fragments.fr_phenol(mol)
    grupos_funcionais_mol["OH fenólico excluindo substituintes Hbond intramoleculares orto"]["Número"] = Fragments.fr_phenol_noOrthoHbond(mol)
    grupos_funcionais_mol["Grupos de ácido fosfórico"]["Número"] = Fragments.fr_phos_acid(mol)
    grupos_funcionais_mol["Grupos éster fosfórico"]["Número"] = Fragments.fr_phos_ester(mol)
    grupos_funcionais_mol["Anéis de piperdina"]["Número"] = Fragments.fr_piperdine(mol)
    grupos_funcionais_mol["Anéis de piperzina"]["Número"] = Fragments.fr_piperzine(mol)
    grupos_funcionais_mol["Amidas primárias"]["Número"] = Fragments.fr_priamide(mol)
    grupos_funcionais_mol["Sulfonamidas primárias"]["Número"] = Fragments.fr_prisulfonamd(mol)
    grupos_funcionais_mol["Anéis de piridina"]["Número"] = Fragments.fr_pyridine(mol)
    grupos_funcionais_mol["Nitrogênios quaternários"]["Número"] = Fragments.fr_quatN(mol)
    grupos_funcionais_mol["Sulfonamidas"]["Número"] = Fragments.fr_sulfonamd(mol)
    grupos_funcionais_mol["Grupos sulfona"]["Número"] = Fragments.fr_sulfone(mol)
    grupos_funcionais_mol["Acetilenos terminais"]["Número"] = Fragments.fr_term_acetylene(mol)
    grupos_funcionais_mol["Anéis de tetrazol"]["Número"] = Fragments.fr_tetrazole(mol)
    grupos_funcionais_mol["Anéis tiazólicos"]["Número"] = Fragments.fr_thiazole(mol)
    grupos_funcionais_mol["Tiocianatos"]["Número"] = Fragments.fr_thiocyan(mol)
    grupos_funcionais_mol["Anéis de tiofeno"]["Número"] = Fragments.fr_thiophene(mol)
    grupos_funcionais_mol["Alcanos não ramificados de pelo menos 4 membros (exclui alcanos halogenados)"]["Número"] =  Fragments.fr_unbrch_alkane(mol)
    grupos_funcionais_mol["Grupos de ureia"]["Número"] = Fragments.fr_urea(mol)

    return grupos_funcionais_mol


#########################
#   Seletor de grupos   #
#########################

def seletor_de_grupos_funcionais(dic_mol):
    """ Função que seleciona grupos funcionais de uma molécula para possíveis mutações, cruzamento ou interações com outras moléculas
    
    Args:
        dic_mol: Dicionário contendo os grupos funcionais da molécula
        
    Returns:
        Grupos funcionais selecionados da molécula
    """
    dic_mol_seleto = {} # Dicionário contendo os grupos funcionais selecionados da molécula
    # Para cada grupo funcional, se o valor de alguma propriedade for diferente de 0, este é um grupo funcional válido para ser selecionado.
    for i in dic_mol:
        if dic_mol[i]["Número"] != 0:
            dic_mol_seleto[i] = dic_mol[i]
            for u in dic_mol[i]:
                dic_mol_seleto[i][u] = dic_mol[i][u]
    
    return dic_mol_seleto