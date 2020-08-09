from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def main(name):
    return f'Hello {name}'

@app.route('/<name>/<second_name>')
def main2(name, second_name):
    return f'Hello {name} & {second_name}'

if __name__ == '__main__':
    app.run()