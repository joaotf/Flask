import csv
import functions as f
from flask import Flask,render_template,request,url_for

path = './static/trabalho.csv'
app = Flask(__name__)


@app.route('/index')
def index():
    city = f.list_of_citys()
    types = f.list_of_types()
    return render_template('index.html', cidadees = city , tipoos = types)

@app.route('/graph',methods=["GET","POST"])
def graph():
    
    if(request.method == "POST"):
        cidade = request.form.get('cidade')
        combustivel = request.form.get('combustível')
        x,y = f.build_graph(cidade,combustivel)
        grafo = f.graph(x,y)
        return render_template('graph.html',graph1 = grafo)


if(__name__ == '__main__'):
    app.run(debug=True)