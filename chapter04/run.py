from flask import Flask, request

app = Flask(__name__)

@app.route('/test1/<foo>')
def main(foo):
    return f'Hello {foo}'

@app.route('/test2/<foo>/<bar>')
def main2(foo, bar):
    return f'Hello {foo} & {bar}'
    
@app.route('/test3/<int:foo>')
def main3(foo):
    return f'{1 + foo}'

if __name__ == '__main__':
    app.run()