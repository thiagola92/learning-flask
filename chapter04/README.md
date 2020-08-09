# Parameters
É possível receber parâmetros passados pela URL.  
```python
@app.route('/<parameter_name>')
def example(parameter_name):
    return
```

Barras podem ser usadas para separar parâmetros mas não é a melhor opção.  
```python
@app.route('/<parameter_name>/<parameter_name2>')
def example(parameter_name, parameter_name2):
    return
```

