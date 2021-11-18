from bs4 import BeautifulSoup
import sys
import numpy as np
import requests
import re
import datetime as dt
import csv

#taxnames = {"DOL":["DOL","DIXDOL"],"EUR":["EUC","R$ X EURO"],"PRE":["PRE","DIXPRE"],"PTX":["ACC"]}
f = open("feriados.txt","r")
f_r = f.read().split(',')
f.close()
feriados = np.array(f_r,dtype='datetime64')
taxnames = {"DIC":["DIC","DI X IPCA"],"PRE":["PRE","DIxPRE"],"DIM":["DIM","DIxIGPM"],"EUR":["EUR","R$ x EURO"]}
data_entrada = dt.date.today().strftime("%d/%m/%Y")
data_entrada = dt.date(2012,11,14)
data_fim = dt.date(2013,7,1)

while(data_entrada <= data_fim):
        data_entrada = data_entrada.strftime("%d/%m/%Y")
        data_str = data_entrada
        data = data_entrada.split("/")
        dataTaxa = dt.date(int(data[2]),int(data[1]),int(data[0]))

        cont_linha = 1
        f = open("/mnt/c/TaxaSwap/new/"+str(dataTaxa).replace("-","")+".txt","w")
        for chaves in taxnames.keys():       
                url = "http://www2.bmf.com.br/pages/portal/bmfbovespa/boletim1/TxRef1.asp?Data="+data_str+"&Data1="+str(data_str.replace("/",""))+"&slcTaxa="+str(taxnames[chaves][0])                 
                print(url)
                html = requests.get(url).content
                soup = BeautifulSoup(html, 'html.parser')
                precos = soup.findAll("td",{"class": re.compile("tabelaConteudo.*")})
                taxas = []
                cont = 0
                for item in precos:
                        if not item in (None,''):
                                valor = item.getText().strip()
                                taxas.append(valor)
                if(taxnames[chaves][1] == "DIxPRE"):
                        taxa_completa_dias = taxas[0::3]
                        taxa_completa = taxas[1::3]
                else:
                        taxa_completa_dias = taxas[0::2]
                        taxa_completa = taxas[1::2]

                for tax in taxa_completa:
                        codificacao_txt = []
                        codificacao_txt.append("0"*(6-len(str(cont_linha)))+str(cont_linha)) #aqui deve ser o conta linha
                        codificacao_txt.append("00101")
                        codificacao_txt.append(str(dataTaxa).replace("-",""))
                        codificacao_txt.append("T1")
                        codificacao_txt.append(chaves)
                        codificacao_txt.append("  "+taxnames[chaves][1]+" "*(15-len(taxnames[chaves][1])))
                        codificacao_txt.append("0"*(5-len(str(taxa_completa_dias[cont])))+""+str(taxa_completa_dias[cont]))
                        #calcular dias uteis
                        proxData = dataTaxa+dt.timedelta(days=int(taxa_completa_dias[cont]))
                        dias = np.busday_count( dataTaxa, proxData,holidays=feriados)
                        codificacao_txt.append("0"*(5-len(str(dias)))+""+str(dias))
                        NumberBroker = taxa_completa[cont].split(",")
                        partefracionaria = NumberBroker[1]+"0"*(7-len(NumberBroker[1]))
                        parteinteira = NumberBroker[0]
                        
                        if ("-" in parteinteira):
                                codificacao_txt.append("-")
                                parteinteira = str(abs(int(parteinteira)))
                        else:
                                codificacao_txt.append("+")
                        parteinteira = "0"*(7-len(parteinteira))+parteinteira
                        #Colocar ValorTaxa
                        codificacao_txt.append(parteinteira+partefracionaria)
                        codificacao_txt.append("F")
                        codificacao_txt.append("0"*(5-len(str(taxa_completa_dias[cont])))+""+str(taxa_completa_dias[cont]))                
                        
                        for cod in codificacao_txt:
                                f.write(cod)
                        f.write('\r\n')
                        cont+=1
                        cont_linha+=1
                f.close
        
        data_entrada = dt.datetime.strptime(data_entrada,'%d/%m/%Y') + dt.timedelta(days=1)
        data_entrada = data_entrada.date()
        


       

