from os import lchown
import sys;
import re;

acumulador = 0
countlines = 0
tabela= ''
liberado = 0
i = 1
with open("/mnt/c/Users/robert.santos/Desktop/FULL.sql") as infile:

    for line in infile:

        if (acumulador == 0):
            f = open("/mnt/c/Users/robert.santos/Desktop/Chunk/sql_parte_"+ str(i) +".sql","w")
            
        acumulador = acumulador + (len(line))
        
        #Check se última linha contem insert
        if countlines > 250:
            if "insert" in line.lower():
                f.write("GO\r\n")
                countlines = 0

        #Coloca um GO antes de ter uma tabela nova a ser criada e pega tabela
        if "create" in line.lower():
            #liberado = 1
            #tabela = re.search(r'TABLE (.*) ',line)
            f.write("USE teste\r\n")
            f.write("GO\r\n")
            countlines = 0

        #Retira autoincrement AUTOINCREMENT
        if 'autoincrement' in line.lower():
           line = line.replace('AUTOINCREMENT','')

        #Remove todos os unique
        if 'unique' in line.lower():
            for line in infile:
                if ');' in line:
                    break
            pass    

        if (acumulador > 2000000000):
            f.close
            infile.close
            acumulador = 0
            countlines = 0
            i=i+1
            break

        countlines = countlines + 1
        #if liberado==1 and 'insert' in line.lower():
        #    f.write("USE "+tabela.group(1)+"\r\n")
        #    liberado = 0

        f.write(line)
