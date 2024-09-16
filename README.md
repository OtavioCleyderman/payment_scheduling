# Teste para vaga Desenvolvedor Júnior

**Objetivo:** Desenvolver uma API utilizando Python com Django para gerenciar
agendamentos de pagamentos. A API deve permitir a criação, listagem, consulta e exclusão
de agendamentos.

# Requisitos Técnicos 

- Utilizar Python com Django.
- Utilize o banco de dados padrão do Django “SQLite”.
- Retornar dados no formato JSON.
- Receber campo de valor em Decimal, mas converter para inteiro antes de salvar no
banco de dados.

# Endpoints Requeridos 

**1 - Criar agendamento de pagamento:**

- Método: POST
- URL: /api/agendamentos
- Campos requeridos no corpo da requisição:
    - data_pagamento (data do pagamento no formato YYYY-MM-DD)
    - permite_recorrencia (booleano, indica se permite recorrência)
    - quantidade_recorrencia (inteiro, número de recorrências)
    - intervalo_recorrencia (inteiro, intervalo em dias entre as recorrências)
    - status_recorrencia (string, status da recorrência)
    - agencia (inteiro, número da agência)
    - conta (inteiro, número da conta)
    - valor_pagamento (decimal, valor do pagamento, convertido para inteiro no banco de dados)
- Resposta Esperada:
    - Código HTTP: 201
    - Corpo da Resposta:

        ```json
            {
                "id": <id do agendamento>,
                "data_pagamento": "<data do pagamento>",
                "permite_recorrencia": <booleano>,
                "quantidade_recorrencia": <inteiro>,
                "intervalo_recorrencia": <inteiro>,
                "status_recorrencia": "<status>",
                "agencia": <inteiro>,
                "conta": <inteiro>,
                "valor_pagamento": <valor em inteiro>
            }
        ```
        
**2 - Listar todos os agendamentos:**

- Método: GET
- URL: /api/agendamentos
- Resposta Esperada:
    - Código HTTP: 200
    - Corpo da Resposta:

        ```json
            [
                {
                    "id": <id do agendamento>,
                    "data_pagamento": "<data do pagamento>",
                    "permite_recorrencia": <booleano>,
                    "quantidade_recorrencia": <inteiro>,
                    "intervalo_recorrencia": <inteiro>,
                    "status_recorrencia": "<status>",
                    "agencia": <inteiro>,
                    "conta": <inteiro>,
                    "valor_pagamento": <valor em inteiro>
                }
            ]
        ```

**3 - Consultar agendamento de pagamento:**

- Método: GET
- URL: /api/agendamentos/:id/
- Parâmetros da URL:
    - id (inteiro, identificador do agendamento)
- Resposta Esperada:
    - Código HTTP: 200
    - Corpo da Resposta:

        ```json
            [
                {
                    "id": <id do agendamento>,
                    "data_pagamento": "<data do pagamento>",
                    "permite_recorrencia": <booleano>,
                    "quantidade_recorrencia": <inteiro>,
                    "intervalo_recorrencia": <inteiro>,
                    "status_recorrencia": "<status>",
                    "agencia": <inteiro>,
                    "conta": <inteiro>,
                    "valor_pagamento": <valor em inteiro>
                }
            ]
        ```

**4 - Deletar agendamento de pagamento:**
- Método: DELETE
- URL: /api/agendamentos/:id/
- Parâmetros da URL:
    - id (inteiro, identificador do agendamento)
- Resposta Esperada:
    - Código HTTP: 204 (sem conteúdo)


**Observações:**
- Não é necessário implementar todos os endpoints se o tempo for curto.
- Faça o seu melhor para garantir que os endpoints implementados funcionem
corretamente e que a API retorne os dados no formato JSON conforme especificado.

# Passos para implementação:

1. Configuração do projeto django:
    - Crie um novo projeto Django e um novo app para os agendamentos.
2. Modelagem:
    - Crie um modelo para os agendamentos de pagamento com os campos
especificados.
    - Converta o valor do pagamento de decimal para inteiro antes de salvar no
banco de dados.
3. Serializers:
    - Implementar o response em JSON.
4. Views e URLs:
    - Implemente as views para os endpoints de criação, listagem, consulta e
exclusão de agendamentos.
    - Configure as URLs correspondentes.
5. Testes:
    - Teste os endpoints utilizando qualquer ferramenta como Postman, Insomnia
ou cURL para garantir que a API está funcionando conforme esperado.

# Instruções finais:

- Faça um commit do código em um repositório Git e envie o link para revisão.

# Teste realizado por:

- [@OtavioCleyderman](https://github.com/OtavioCleyderman)

# Observação: 
 - Seguindo o teste, realizei a conversão do decimal inserido para inteiro, tanto para salvar no banco e para retorno do banco em consultas. No entanto, deixei pronto para que, se necessário, o salvamento no banco continue sendo em inteiro mas os retornos das consultas possa ser retornado o valor em decimal, assim como o usuário informou. 
 - Incluído testes no projeto, testes unitários e de integração. 
 - Também realizado teste no postman para confirmar que tudo está saindo como proposto.

# Estrutura e stack utilizada

**Stack:** Python e Django

**Estrutura do projeto:**

```shell
  $ payment_scheduling
  ├── .venv
  ├── .vscode
  ├── payment_scheduler
  │   ├── __init__.py
  │   ├── migrations
  │       ├── __init__.py
  │       ├── 0001_initial.py
  │       └── 0002_paymentscheduler_unique_paymentscheduler.py 
  │   └── tests
  │       ├── test_integration.py
  │       ├── test_models.py
  │       └── test_views.py 
  │   ├── apps.py
  │   ├── models.py
  │   ├──  serializer.py
  │   ├──  urls.py
  │   ├──  validates.py
  │   └── views.py
  ├── setup
  │   ├── __init__.py
  │   ├── asgi.py
  │   ├── settings.py
  │   ├── urls.py
  │   └── wsgi.py
  ├── .env
  ├── .gitignore
  ├── db.sqlite3
  ├── manage.py
  ├── README.md
  └── requirements.txt

```

## Para rodar o projeto em sua máquina

Clone este repositorio ou baixe o código fonte. Em seguida, abra a pasta do projeto no seu editor de código favorito.

Após isso, crie seu ambiente virtual para o projeto e instale as dependências:
```
    python -m venv .venv
    .\.venv\Scripts\activate (Windows) / source .venv/bin/activate (Linux/MacOs)
    pip install -r requirements.txt 
```
Após as dependências do projeto serem instaladas, execute o projeto:
```
    python .\manage.py runserver 
```


Pronto, após realizar os passos acima o projeto já iniciou e está rodando na porta **8000**. Acesse o postman ou qualquer outra qualquer ferramenta como Postman, Insomnia ou cURL e configure os endpoints da aplicação, após isso pode testar a API. Exemplo:
```
    http://localhost:8000/api/agendamentos
```

# Contato

Seus comentários, dicas, sugestões são sempre bem vindos. Entre em contato:

**LinkedIn:** www.linkedin.com/in/otavio-ferraz

**E-mail:** otavio.cleydermann@gmail.com