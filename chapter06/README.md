# Arguments
Existe diversas formas de passar argumentos e recebe-los. Mas antes você precisa importar `request` para interagir com o request feito.  
```python
from flask import request
```

Maioria dos objetos que vão trazer argumentos podem ser tratados como se fossem dicionários normais de python, isso torna o comportamento deles quase que idênticos na hora de receber no Flask.  

Se você vai obter o argumento utilizando colchetes (`exemplo['foo']`) ou utilizando get (`exemplo.get('foo')`), depende da maneira que o conteúdo está vindo. Ou seja, argumentos que podem ou não ter durante a requisição é recomendado utilizar get e tratar para não dar erro, porém argumentos que precisam ter é recomendado utilizar colchete (quando não tiver irá dar um erro na página mas não é necessário você tratar, flask continuára funcionando para próximas requisições)  

# Headers
Referência: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers  
Headers não costumam passar informação sobre a requisição em si mas sim sobre quem o client/server é.  

`request.headers['host']` (utilizado normalmente)  
`request.headers.get('host')`  

# Args
Estes argumentos são passados pelo URL  
https://127.0.0.1/pagina?argumento1=123&argumento2=456  

Se você olhar no final do URL, você consegue obter os valores de **argumento1** e **argumento2**  
**argumento1**: 123  
**argumento2**: 456  

Isto torna bem mais fácil o comportilhamento de um link ou salva-lo no favoritos para futuro uso, porém torna ele visível para qualquer um que tiver o URL.  

`request.args['argumento1']`  
`request.args.get('argumento2')` (utilizado normalmente)  

# Forms
Formulários são muito utilizados em POST requests.  

`request.form['argumento1']` (utilizado normalmente)  
`request.form.get('argumento2')`  

# Values
Combina **Args** com **Forms**, priorizando Args.  

`request.values['argumento1']`  
`request.values.get('argumento2')`  

# Raw
Existem diversas baneiras de enviar informação bruta.  
O método que você utilizara para tratar depende do formato da informação passada.  
O formato da informação se encontra no campo **Content-type** do headers.  

Exempo:  
`Content-Type: application/json`  
`Content-Type: text/plain`  

## Data
Independete do tipo do conteúdo, você vai receber os bytes daquele conteúdo.  
`request.get_data()`  

## JSON
Se o tipo do conteúdo for JSON, é possível utilizar o seguinte método para obter um dicionário com os valores do JSON.  
`request.get_json()`  

# More
More: https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request