# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

formularios = [
    {"ID": {"2": 3, "3": 4}, "nombres": {"2": "Lucho Andreu Amat", "3": "Mat\u00edas Mauricio Castillo Barrera"},
     "fecha_nac": {"2": 640224000000, "3": 849484800000},
     "direccion": {"2": "9448 Fairfield St.", "3": "8143 College St."},
     "localidad": {"2": "Aberdeen, SD 57401", "3": "Trussville, AL 35173"},
     "telefono": {"2": "(246) 245-7306", "3": "(707) 933-2513"},
     "email": {"2": "psichel@sbcglobal.net", "3": "tbeck@optonline.net"},
     "fecha_ingreso": {"2": 1189825271000, "3": 1323271370000}, "grupo": {"2": "E", "3": "E"},
     "direccion_trabajo": {"2": "9448 Fairfield St.", "3": "8143 College St."},
     "localidad_trabajo": {"2": "Aberdeen, SD 57401", "3": "Trussville, AL 35173"},
     "telefono_trabajo": {"2": "(246) 245-7306", "3": "(707) 933-2513"},
     "email_trabajo": {"2": "psichel@sbcglobal.net", "3": "tbeck@optonline.net"},
     "fecha_ingreso_trabajo": {"2": 1189825271000, "3": 1323271370000},
     "direccion_corresp": {"2": "9448 Fairfield St.", "3": "8143 College St."},
     "localidad_corresp": {"2": "Aberdeen, SD 57401", "3": "Trussville, AL 35173"},
     "telefono_corresp": {"2": "(246) 245-7306", "3": "(707) 933-2513"},
     "email_corresp": {"2": "psichel@sbcglobal.net", "3": "tbeck@optonline.net"},
     "fecha_actualizacion": {"2": 1189825271000, "3": 1323271370000}, "calificacion_riesgo": {"2": "E", "3": "E"}}
]


def _find_next_id():
    return max(formulario["ID"] for formulario in formularios) + 1


def _existe_id(ID_CONS, formulario=None, formularios_duplicados=None):
    if formulario["ID"] == ID_CONS:
        formulario = request.get_json()
        formularios_duplicados.append(formulario)
        return formulario, 201
    else:
        formulario = request.get_json()
        formulario["id"] = _find_next_id()
        formularios.append(formulario)
        return formulario, 201


@app.get("/formularios")
def get_formularios():
    return jsonify(formularios)


@app.post("/formularios")
def add_formulario():
    if request.is_json:
        formulario = request.get_json()
        formulario["id"] = _find_next_id()
        formularios.append(formulario)
        return formulario, 201

    return {"error": "Request must be JSON"}, 415
