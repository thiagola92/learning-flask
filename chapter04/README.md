# URL
Existem caracteres especiais dentro de um url.  

Barra (**/**): Originalmente utilizado para indicar em qual diretório e arquivo você deseja acessar.  
Interrogação (**?**): Utilizado no **final** do url para indicar o início de uma query.  
E comercial (**&**): Utilizando dentro de uma query para indicar multiplos parâmetros.  

# Parameters
É possível receber como parâmetros valores passados na rota.  
```python
@app.route('/test1/<foo>')
def main(foo):
    return f'{foo}'

@app.route('/test2/<foo>/<bar>')
def main2(foo, bar):
    return f'{foo} & {bar}'
```

E até mesmo especificar o tipo esperado.  
```python
@app.route('/test3/<int:foo>')
def main3(foo):
    return f'{1 + foo}'
```