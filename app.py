from flask import Flask, render_template, request
#aplicación de calculadora y rutas repticiones 


app = Flask(__name__)
@app.route('/')
def home():
    return render_template("inicio.html")

@app.route("/suma", methods=["GET", "POST"])
def sumar():
    if request.method == "POST":
        if not request.form.get("numero1") or not request.form.get("numero2"):
            return f"Ingrese ambos números para realizar la suma."
        else:
            numero1 = float(request.form.get("numero1"))
            numero2 = float(request.form.get("numero2"))
            resultado = numero1 + numero2
            return render_template("suma.html", resultado=resultado)
    return render_template("suma.html")


@app.route("/resta", methods=["GET", "POST"])
def resta():
    if request.method == "POST":
        num1 = float(request.form.get("num1"))
        num2 = float(request.form.get("num2"))
        print(num1 - num2)
        resultado = num1 - num2
        return render_template("resta.html", resultado=resultado)
    return render_template("resta.html")

@app.route("/multiplicacion", methods=["GET", "POST"])
def multiplicacion():
    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        print(num1 * num2)
        resultado = num1 * num2
        return render_template("multiplicacion.html", resultado=resultado)
    return render_template("multiplicacion.html")

@app.route("/division", methods=["GET", "POST"])
def division():
    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        print(num1 / num2)
        if num2 != 0:
            resultado = num1 / num2
            return render_template("division.html", resultado=resultado)
        else:
            return render_template("error.html") 
    return render_template("division.html")






if __name__ == '__main__':
    app.run(debug=True)  # Ejecuta la aplicación en modo de depuración para facilitar el desarrollo y recargar la pagina.