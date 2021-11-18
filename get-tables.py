from os import lchown
import sys;
import re;
acumulador = 0
countlines = 0
tabela= ''
liberado = 0
i = 1

f = open("/mnt/c/Users/robert.santos/Desktop/Chunk/sql_tables.sql","w")
with open("/mnt/c/Users/robert.santos/Desktop/FULL.sql") as infile:
    f.write("USE teste\r\n")
    for line in infile:
        
        if "create" in line.lower():
            if ");" in line.lower():
                if 'UNIQUE' in line:
                    tabela = re.search(r'UNIQUE (.*)\)',line).group(0)
                    line = line.replace(tabela[:len(tabela)-1],'')
                line = line.replace('AUTOINCREMENT','')                    
                f.write(line);
            else:
                f.write(line)
                for line in infile:
                    line = line.replace('AUTOINCREMENT','')
                    if "unique" in line.lower():
                        for line in infile:
                            if ");" in line:
                                break
                    f.write(line)
                    if ");" in line:
                        break
            f.write("GO\r\n")
            
