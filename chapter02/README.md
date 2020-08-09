# Page
O decorador **route** recebe o URL a qual deve liga a função abaixo dele
```python
@app.route('/')
def example():
    return 'example'
```
O retorno da função será exibido na página do usuário  

# Example
No arquivo **run.py** foram criados alguns exemplos:  
http://127.0.0.1:5000/  
http://127.0.0.1:5000/foo  
http://127.0.0.1:5000/bar  
http://127.0.0.1:5000/foo/bar  