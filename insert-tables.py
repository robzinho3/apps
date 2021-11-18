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

        if "insert" in line.lower(): 
            if (acumulador == 0):
                f = open("/mnt/c/Users/robert.santos/Desktop/Chunk/sql_insert_"+ str(i) +".sql","w") 

            acumulador = acumulador + (len(line))
            
            #Check se última linha contem insert
            if countlines > 250:
                f.write("GO\r\n")
                countlines = 0

            if (acumulador > 2000000000):
                f.close
                infile.close
                acumulador = 0
                countlines = 0
                i=i+1

            countlines = countlines + 1

            f.write(line)
