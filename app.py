from flask import Flask, request, render_template, send_file
import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, cos, pi
import io

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/plot", methods=["GET"])
def plot():
    try:
        # Obtener parámetros desde la URL
        u0 = float(request.args.get("u0", 40))
        theta1 = float(request.args.get("theta1", 45))
        theta2 = float(request.args.get("theta2", 30))
        g = 9.81

        # Cálculos de trayectorias
        ux1 = u0 * cos(theta1 * pi / 180)
        uy1 = u0 * sin(theta1 * pi / 180)
        ux2 = u0 * cos(theta2 * pi / 180)
        uy2 = u0 * sin(theta2 * pi / 180)

        t_total_1 = 2 * uy1 / g
        t_total_2 = 2 * uy2 / g

        t1 = np.linspace(0, t_total_1, 100)
        t2 = np.linspace(0, t_total_2, 100)

        sx1 = ux1 * t1
        sy1 = (uy1 * t1) - (0.5 * g * t1**2)

        sx2 = ux2 * t2
        sy2 = (uy2 * t2) - (0.5 * g * t2**2)

        # Ajustar límites dinámicamente
        max_x = max(sx1[-1], sx2[-1]) + 10
        max_y = max(max(sy1), max(sy2)) + 10

        # Crear gráfico
        plt.figure(figsize=(10, 5))
        plt.plot(sx1, sy1, label=f'θ={theta1}')
        plt.plot(sx2, sy2, label=f'θ={theta2}')
        plt.xlim(0, max_x)
        plt.ylim(0, max_y)
        plt.xlabel("Distancia (m)")
        plt.ylabel("Altura (m)")
        plt.legend()
        plt.grid()

        # Guardar en memoria y enviar la imagen
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)

        return send_file(img, mimetype='image/png')
    
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
