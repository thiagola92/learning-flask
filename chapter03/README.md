# API
> Isto é mais um comentário do que qualquer coisa

Não existe diferença entre montar uma página e montar uma API.  
Quando você está acessando a página pelo navegador, você está fazendo um simple GET request.  

Uma maneira de você confirmar isto é utilizando a biblioteca **requests**.  
Inicialize o Flask e acesse qualquer página criada.  
```python
response = requests.get('http://127.0.0.1:5000/')
print(response.text)
```

Este código vai exibir exatamente o retornado da função linkada com este URL.  