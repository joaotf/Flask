from flask import Flask,render_template
import csv , re

postos_belem = []

    

app = Flask(__name__)
@app.route('/')
def mostrarCombustiveis():
    combustiveis_csv = "./static/trabalho.csv"
    postos = carrega_postos_belem(combustiveis_csv)
    return render_template('pagina.html',listaPostos=postos)

def carrega_postos_belem(caminho_arquivo):
    arquivo = open(caminho_arquivo, 'r+', encoding='iso-8859-1')

# lê o arquivo csv, nesse caso o delimitador é um 'tab'
    linhas = csv.reader(arquivo, delimiter="\t")
    for linha in linhas:
# a terceira coluna indica a cidade do posto de gasolina e o tipo de combustivel
        if((str(linha).find("BELEM") != -1) and str(linha).find("PA") != -1 and str(linha).find("GASOLINA") != -1) :
            postos_belem.append(str(linha))    
        
        
    arquivo.close()

    return postos_belem


app.run()