import pandas as pd
from params import COLUNAS, TIPO_ADMINISTRACAO, TIPO_LOCALIZACAO, STATUS_FUNCIONAMENTO, INVERTER_VALORES, ESCOLA_URBANA

FILE_PATH = 'data/escolas/microdados_ed_basica_2022.csv'
SAVE_PATH = 'data/escolas/censo_escolas_ensino_basico_2022_tratado.csv'

class Extractor:
    def __init__(self):
        self.read_schools_file()

    def read_schools_file(self):
        self.data = pd.read_csv(FILE_PATH, delimiter=';',encoding='latin-1')

    def data_transform(self):
        df = self.data[COLUNAS.keys()].rename(columns=COLUNAS)

        df['tipo_administracao'] = df['tipo_administracao'].map(TIPO_ADMINISTRACAO)
        df['possui_energia_eletrica'] = df['possui_energia_eletrica'].map(INVERTER_VALORES)
        df['escola_urbana'] = df['escola_urbana'].map(ESCOLA_URBANA)
        df['especificacao_tipo_localizacao'] = df['especificacao_tipo_localizacao'].map(TIPO_LOCALIZACAO)
        df['status_funcionamento'] = df['status_funcionamento'].map(STATUS_FUNCIONAMENTO)
        df['endereco_completo'] = df['endereco'] + ', ' + df['endereco_numero'] + ', ' + df['bairro']
        self.data = df
        df.to_csv(SAVE_PATH, index=False)
        return df