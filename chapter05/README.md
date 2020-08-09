# Return
O retorno a qualquer request ao website/api deve ser um objeto **Response**.  
Caso o retorno das funções não seja Response, Flask tenta fazer uma conversão de alguns tipos básicos para Response.  

As duas maneiras de retornar mais populares são:  
**String**: Cria uma Response com os parâmetros padrões e a string passada.  
**Dict**: Cria uma Response utilizando `jsonify()` onde converte dicionário para json, muito utilizado para APIs.  
