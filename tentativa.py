from flask import Flask,render_template
import csv , re


arquivo = open("./static/trabalho.csv", 'r+', encoding='iso-8859-1')
linhas = csv.reader(arquivo, delimiter="\t")

for linha in linhas:
    if((str(linha).find("BELEM") != -1) and str(linha).find("PA") != -1 and str(linha).find("GASOLINA") != -1) :
        print(str(linha))
