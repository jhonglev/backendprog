from config import *
from model import Calcado

@app.route("/")
def inicio():
    return 'Sistema de cadastro de calcados. '+\
        '<a href="/listar_calcados">Operação listar</a>'

@app.route("/listar_calcados")
def listar_calcados():
    calcados = db.session.query(Calcado).all()
    calcados_em_json = [ calcado.json() for calcado in calcados ]
    resposta = jsonify(calcados_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta