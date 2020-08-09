# Installing
`pip install flask`  

# Run
Existem duas maneiras de inicializar a aplicação flask

## Flask module
Bote na variável de ambiente do flask o arquivo o qual ele deve executar quando for inicializado.  
```shell
$export FLASK_APP=run01.py
```  

Para inicializar flask  
```shell
$flask run
```  

## In code
Caso você queira executar igual a outros programas de python, você deve declarar no arquivo python:  
```python
if __name__ == "__main__":
    app.run()
```  

Para inicializar flask basta executar como se fosse um programa de python  
```shell
$python run.py
```

# Page
No terminal deve exibir que a página pode ser acessada pelo url http://127.0.0.1:5000/  

# Reference
https://flask.palletsprojects.com/en/1.1.x/server/#server  