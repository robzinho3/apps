import sqlite3
import pandas as pd
cnx = sqlite3.connect('/mnt/c/Users/robert.santos/Desktop/BDM.sqlite')




tabelas = ["ANBIMA_CRI_CRA","ANBIMA_CURVAS_CREDITO","ANBIMA_DEBENTURES","ANBIMA_DEBENTURES_SECUNDARIO","ANBIMA_ETTJ","ANBIMA_PROJECAO_IGP","ANBIMA_TITULOS_PUBLICOS","ANBIMA_VNA","ATIVOS_CAPITANIA","B3_SECUNDARIO","B3_SECUNDARIO_T","BACEN_NEGOCIOS_TPF","BACEN_SERIE","BACEN_SERIE_DESCRICAO","BATIMENTO_FUNDOS","BMF_BVBG","BMF_COTAHIST","BMF_DEBMTM","BMF_INDICES","BMF_TAXASWAP","BOLETAGEM_HISTORICO","CALLS_CORRETORAS","CALL_NTNB_XP","CAPITANIA_APORTES","CAPITANIA_RESGATES","CARTEIRAS_CAPITANIA","CARTEIRAS_CAPITANIA_F","CDI_CETIP","CURVA_DEB","DECOMPOSICAO_IPCA","DF_ANUAL_2010","DF_ANUAL_2011","DF_ANUAL_2012","DF_ANUAL_2013","DF_ANUAL_2014","DF_ANUAL_2015","DF_ANUAL_2016","DF_ANUAL_2017","DF_ANUAL_2018","DF_ANUAL_2019","DF_ANUAL_2020","FIDC_CVM_DESEMPENHO","FIDC_CVM_EVENTOS","FIDC_CVM_NRCOTIST","FIDC_CVM_QTD","FIDC_CVM_RENTABILIDADE","IMBARQ_02","IMBARQ_12","IMBARQ_28","IPEA_INFO","POSICAORF_IMB_CETIP","REALOCADOR","RELATORIO_BRADESCO","RELATORIO_ITAU","RELATORIO_MELLON","RELATORIO_XP_MARGEM","REUNE_TOTAL","REUNE_TOTAL_SPREAD"]
#tabelas = ["ANBIMA_CRI_CRA"]

cursor = cnx.cursor()
for item in tabelas:
    #data = pd.read_sql_query(f"DELETE FROM {item}",cnx)
    cursor.execute(f"DELETE FROM {item} ")
    print(item)
    cnx.commit()
    
    
        
cnx.close()