import csv
import matplotlib.pyplot as plt
import io
import base64
import re

postos_belem = []
cidades = []
tipos = []
datas = []
valores = []

n = []
m = []


path = './static/trabalho.csv'

def graph(x,y):
    img = io.BytesIO()
    plt.plot(x,y)
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return (f'data:image/png;base64,{graph_url}')


def list_of_citys():
    arq = open(path, 'r+', encoding='iso-8859-1')

    linhas = csv.reader(arq, delimiter="\t")
    
    for linha in linhas:
        x = str(linha).replace('[','').replace(']','').split()
        cidades.append(x[2])
        
        if(cidades.count(x[2]) != 1):
            x = cidades.index(x[2])
            cidades.pop(x)
        else:
            pass
            
    return cidades

def list_of_types():
    arq = open(path, 'r+', encoding='iso-8859-1')

    opa = csv.reader(arq, delimiter="\t")
    
    for b in opa:
        q = str(b).replace('[','').replace(']','').split()
        if(q[8] == "GASOLINA" or q[8] == "DIESEL" or q[8] == "ETANOL"):
            tipos.append(q[8])
            if(tipos.count(q[8]) != 1):
                y = tipos.index(q[8])
                tipos.pop(y)

    return tipos


def build_graph(x,y):
    count = 0
    arquivao = open(path, 'r+',encoding='iso-8859-1')
    print(y)
    aaa = csv.reader(arquivao, delimiter="\t")
    for kkk in aaa:
        t = str(kkk).replace('[','').replace(']','').replace(",",".").split()
        if((cidades.__contains__(x) != False) and (tipos.__contains__(y) != False)):
            if(re.match(r'(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d{2,2}',t[8])):
                datas.append(t[8])
            if(re.match(r'(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d{2,2}',t[9])):
                datas.append(t[9])
            if(re.match(r'[+-]?([0-9]*[.])?[0-9]+',t[10]) and t[10].find("/") == -1 and t[10].find('.') != -1):
                valores.append(float(t[10]))
            if(re.match(r'[+-]?([0-9]*[.])?[0-9]+',t[11]) and t[11].find("/") == -1 and t[11].find('.') != -1):
                valores.append(float(t[11]))
            if(re.match(r'[+-]?([0-9]*[.])?[0-9]+',t[12]) and t[12].find("/") == -1 and t[12].find('.') != -1):
                valores.append(float(t[12]))    

    for i in range(0,1000):
        n.append(datas[i])
        n.sort()
        m.append(valores[i])    
        m.sort()
    return n,m

    
