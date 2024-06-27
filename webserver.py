from flask import Flask, render_template

app = Flask("my-second-website-in-python")


@app.route("/inicio")
def osteotronik():
    return render_template("index.html")


@app.route("/productos")
def productos():
    return render_template("productos.html")


@app.route("/clavofemur")
def clavofemur():
    return render_template("clavodefemur.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5000')
