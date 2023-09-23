COLUNAS = {
    'CO_ENTIDADE':'id_escola',
    'NO_REGIAO':'regiao',
    'NO_UF':'estado',
    'SG_UF':'estado_sigla',
    'NO_MUNICIPIO':'municipio',
    'NO_ENTIDADE':'escola',
    'TP_DEPENDENCIA':'tipo_administracao',
    'TP_SITUACAO_FUNCIONAMENTO':'status_funcionamento',
    'TP_LOCALIZACAO':'escola_urbana',
    'TP_LOCALIZACAO_DIFERENCIADA': 'especificacao_tipo_localizacao',
    'DS_ENDERECO':'endereco',
    'NU_ENDERECO':'endereco_numero',
    'NO_BAIRRO':'bairro',
    'CO_CEP':'cep',
    'DT_ANO_LETIVO_INICIO':'data_inicio_ano_letivo',
    'DT_ANO_LETIVO_TERMINO':'data_fim_ano_letivo',
    'IN_AGUA_POTAVEL':'possui_agua_potavel',
    'IN_ENERGIA_INEXISTENTE':'possui_energia_eletrica',
    'IN_ESGOTO_INEXISTENTE':'possui_esgoto',
    'IN_BANHEIRO':'possui_banheiro',
    'IN_BIBLIOTECA':'possui_biblioteca',
    'IN_EQUIP_TV':'possui_tv',
    'IN_EQUIP_LOUSA_DIGITAL':'possui_tv_digital',
    'IN_EQUIP_MULTIMIDIA':'possui_multimidia',
    'IN_TABLET_ALUNO':'possui_tablet_estudante',
    'IN_INTERNET':'possui_acesso_internet',
    'IN_INTERNET_APRENDIZAGEM':'possui_acesso_internet_aprendizagem',
    'QT_DOC_BAS':'qtde_docentes_ed_basica',
    'QT_DOC_INF':'qtde_docentes_ed_infantil',
    'QT_DOC_FUND':'qtde_docentes_ed_fundamental',
    'QT_DOC_MED':'qtde_docentes_ensino_medio',
    'QT_PROF_PSICOLOGO':'qtde_psicologo_escolar',
    'IN_NOTURNO':'possui_turno_noturno',
    'IN_INF':'possui_matricula_ed_infantil',
    'IN_FUND':'possui_matricula_ed_fundamental',
    'IN_MED':'possui_matricula_ensino_medio',
    'IN_EJA':'possui_matricula_eja',
    'QT_MAT_BAS':'qtde_matriculas_ed_basica',
    'QT_MAT_INF':'qtde_matriculas_ed_infantil',
    'QT_MAT_FUND':'qtde_matriculas_ed_fundamental',
    'QT_MAT_MED':'qtde_matriculas_ensino_medio',
    'QT_MAT_EJA':'qtde_matriculas_eja',
    'QT_MAT_BAS_ND':'qtde_matriculas_cor_raca_nao_declarada',
    'QT_MAT_BAS_BRANCA':'qtde_matriculas_cor_raca_branca',
    'QT_MAT_BAS_PRETA':'qtde_matriculas_cor_raca_preta',
    'QT_MAT_BAS_PARDA':'qtde_matriculas_cor_raca_parda',
    'QT_MAT_BAS_AMARELA':'qtde_matriculas_cor_raca_amarela',
    'QT_MAT_BAS_INDIGENA':'qtde_matriculas_cor_raca_indigena'
}

TIPO_ADMINISTRACAO = {
    1: 'Federal',
    2: 'Estadual',
    3: 'Municipal',
    4: 'Privada'
}

TIPO_LOCALIZACAO = {
    0: 'Sem especificação',
    1: 'Área de assentamento',
    2: 'Terra indígena',
    3: 'Área de comunidade remanescente de quilombos'
}

STATUS_FUNCIONAMENTO = {
    1: 'Ativa',
    2: 'Paralisada',
    3: 'Extinta',
    4: 'Extinta'
}

INVERTER_VALORES = {
    1:0,
    0:1
}

ESCOLA_URBANA = {
    1:1,
    2:0
}