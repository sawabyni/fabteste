from flask import Flask, render_template, send_from_directory, request # Importando bibliotecas para o python

app = Flask(__name__) #Cria um site vazio

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/videos/<filename>')
def serve_video(filename):
    return send_from_directory('videos', filename)

def numerology(name):
    # Tabela de conversão letra/número
    letters = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
        'j': 1, 'k': 2, 'l': 3, 'm': 4, 'n': 5, 'o': 6, 'p': 7, 'q': 8, 'r': 9,
        's': 1, 't': 2, 'u': 3, 'v': 4, 'w': 5, 'x': 6, 'y': 7, 'z': 8
    }

    # Converter para minúsculas e remover espaços
    name = name.lower().replace(" ", "")

    # Calcular o valor numerológico
    value = sum(letters.get(c, 0) for c in name)

    # Verificar se o número é um número mestre
    if value in [11, 22, 33, 44, 55, 66, 77, 88, 99]:
        return value, f"{value} mestre"

    # Verificar se os dígitos das casas são iguais
    houses = [int(d) for d in str(value)]
    if all(digit == houses[0] for digit in houses):
        return value, f"{value} é um número com dígitos iguais"

    # Calcular o valor reduzido se o número não for mestre nem tiver dígitos iguais
    while value > 9:
        houses = [int(d) for d in str(value)]
        value = sum(houses)
    return value, value

@app.route('/', methods=['POST'])
def separar():
    name = request.form['palavra']
    value, description = numerology(name)
    return render_template('resultado.html', name=name, value=value, description=description)

if __name__ == "__main__":
    app.run(debug=True) #coloca o site no ar
