from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('formulario.html')

@app.route('/generar', methods=['POST'])
def generar():
    data = request.json
    campos = [
        data.get("proveedor", ""),
        data.get("comprobante_relacionado", ""),
        data.get("numero_contrato", ""),
        data.get("factura_recibo", ""),
        data.get("numero_documento", ""),
        data.get("numero_pago", ""),
        data.get("glosa", ""),
        data.get("periodo_mensual", ""),
        data.get("comunicacion_interna", ""),
        data.get("banco", ""),
        data.get("numero_cuenta", ""),
        data.get("titular_cuenta", "")
    ]
    resultado = "; ".join(campos)
    return jsonify({"resultado": resultado})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
