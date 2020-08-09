from flask import Flask

app = Flask(__name__)

@app.route('/test1')
def main():
    return 'String'

@app.route('/test2')
def main2():
    return {'example': 'dict'}

if __name__ == '__main__':
    app.run()