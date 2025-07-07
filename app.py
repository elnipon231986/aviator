from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

historial_simulaciones = []

def generar_crash():
    return round(random.uniform(1.00, 10.00), 2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simular')
def simular():
    datos = [generar_crash() for _ in range(50)]
    historial_simulaciones.append(datos)

    promedio = round(sum(datos) / len(datos), 2)
    maximo = max(datos)
    minimo = min(datos)
    ultimos5 = datos[-5:]
    promedio_ultimos5 = round(sum(ultimos5) / 5, 2)

    decision = "🟡 Precaución"
    if all(x < 2 for x in ultimos5):
        decision = "🔴 Retírate rápido"
    elif promedio_ultimos5 > promedio:
        decision = "🟢 Puede subir más"

    return jsonify({
        'datos': datos,
        'promedio': promedio,
        'maximo': maximo,
        'minimo': minimo,
        'ultimos5': ultimos5,
        'promedio_ultimos5': promedio_ultimos5,
        'decision': decision,
        'historial': historial_simulaciones[-5:]
    })

if __name__ == '__main__':
    app.run(debug=True)
