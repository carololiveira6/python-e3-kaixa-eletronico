## **Table of Contents**
- [E3 - Kaixa eletrônico](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1b_e_01_kaixa-eletronico.html&ref=master#mcetoc_1esj4slvm0)
  - [Objetivo](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1b_e_01_kaixa-eletronico.html&ref=master#mcetoc_1f362b6b10)
  - [Preparativos](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1b_e_01_kaixa-eletronico.html&ref=master#mcetoc_1f362b6b11)
  - [Caixa Eletrônico](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1b_e_01_kaixa-eletronico.html&ref=master#mcetoc_1eg6l938o6l)
- [Entregáveis](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1b_e_01_kaixa-eletronico.html&ref=master#mcetoc_1f362b6b12)
  - [Repositório](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1b_e_01_kaixa-eletronico.html&ref=master#mcetoc_1egvrpv6k1l4)
- [Critérios de aceitação](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1b_e_01_kaixa-eletronico.html&ref=master#mcetoc_1eh146n6m3)
# **E3 - Kaixa eletrônico**
Para essa entrega você criará um sistema de caixa eletrônico que irá registrar as entradas e saídas de uma conta bancária.
## **Objetivo**
Essa atividade foi elaborada para trabalhar seus conhecimentos de manipulação de arquivos JSON.
## **Preparativos**
Você devera criar um arquivo chamado kaixa.py e implementar as funções conforme as descrições.

Utilize a documentação de auxílio: [os.stat,](https://www.techiedelight.com/get-size-file-python/) [json](https://docs.python.org/3/library/json.html), [datetime](https://docs.python.org/pt-br/3/library/datetime.html)** e sinta-se à vontade para pesquisar em outros fóruns de python sobre as bibliotecas citadas.
## **Kaixa Eletrônico**
Crie um arquivo chamado transactions.json (**vazio**) que será utilizado para salvar os dados de novas transações, após implementadas às duas funções, ele deve **ser** **populado apenas pela sua função** post\_transaction.

- **all\_transactions(filename)**
  - **Parâmetros:** A função recebe o nome do arquivo a ser lido filename
  - **Procedimento:** 
    - Verifique se o arquivo **não** **existe** ou se está **vazio**, caso uma das duas seja verdade, retorne uma **lista vazia.**
    - Caso nenhuma das variantes acima for verdadeira, abra o arquivo filename e retorne uma lista contendo todas as transações listadas.
  - **Dica ->** Utilize o exemplo de transactions.json abaixo para realizar os testes iniciais para a função all\_transactions

"""

Exemplo de transação dentro de transactions.json

[{"title": "Mercado", "transaction\_type": "outcome", "value": 200, "date": "29/01/2021"}, 

{"title": "Cinema", "transaction\_type": "outcome", "value": 150, "date": "30/01/2021"}]

"""

FILENAME = 'transactions.json'

transactions = all\_transactions(FILENAME)

print(transactions)

\>[{"title": "Mercado", "transaction\_type": "outcome", "value": 200, "date": "29/01/2021"}, 

{"title": "Cinema", "transaction\_type": "outcome", "value": 150, "date": "30/01/2021"}]

- **post\_transaction(filename, title, transaction\_type, value)**
  - **Parâmetros:**
    - O parâmetro filename é o nome do arquivo em string que será utilizado para escrever uma nova transação.
    - O parâmetro title representa um nome que o usuário da função deve dar para a transação realizada.
    - O parâmetro transaction\_type representa o tipo de transação realizada, e pode assumir os valores **income** e **outcome.**
    - O parâmetro value é o valor da transação em **float**.
  - **Procedimento:** 
    - A função post\_transaction deve escrever uma **nova transação** no arquivo especificado no parâmetro filename, **mantendo todas que já estavam no arquivo.**
    - Caso o arquivo não exista, você deverá criá-lo.
    - Monte um dicionário com as informaçoes pertinentes (descritas no exemplo), **adicionando** um campo **date,** com a **data atual** no formato **dd/MM/AAAA** (Reveja os links de documentação auxiliar no início da atividade).
    - **Dica ->** Pense em uma forma de utilizar a função all\_transactions para não perder as transações já escritas no arquivo.
  - **Retorno:**
    - A função deve retornar um dicionário com os dados pertinentes como especificado no exemplo abaixo:

\# Exemplo de chamada

FILENAME = 'transactions.json'

post\_transaction(FILENAME, 'Salário', 'income', 250)

\> {'title': 'Salário', 'transaction\_type': 'income', 'value': 250, 'date': '03/02/2021'}

- **calculate\_balance(filename)**
  - **Parâmetros:**
    - O parâmetro filename é o nome do arquivo em string que será utilizado para escrever uma nova transação.
  - **Procedimento:** 
    - A função calculate\_balance deve calcular o saldo atual, considerando os valores das transações **outcome** como **gastos** e os **incomes** como **ganhos.** 
  - **Retorno:**
    - Deve retornar o **saldo** (podendo ser positivo ou negativo) do usuário (**int** ou **float**) sinalizado em uma string no formato do exemplo.
    - Deve retornar uma lista vazia caso o nome do arquivo seja incorreto ou se não existir nenhuma transação no arquivo específicado.
  - **Dica ->** Utilize all\_transactions para ter fácil acesso a todas as transações do arquivo JSON.

Esse é o conteúdo do nosso arquivo transactions.json:

[{"title": "Mercado", "transaction\_type": "outcome", "value": 200, "date": "29/01/2021"}, 

` `{"title": "Salário", "transaction\_type": "income", "value": 1200, "date": "30/01/2021"}]

E esse é o nosso código kaixa.py: 

FILENAME = 'transactions.json'

saldo = calculate\_balance(FILENAME)

print(saldo)

\>'Seu saldo é de: R$ 1000'

-----
# **Entregáveis**
## **Repositório**
- Link do **repositório** do **GitLab**
- **Código-fonte:**
  - Arquivo **kaixa.py**.
- **Privacidade**
  - Incluir **ka-br-out-2020-correcoes** como **reporter**.
-----
# **Critérios de aceitação**

|**pts**|**Dado**|**Quando**|**É esperado**|
| :-: | :-: | :-: | :-: |
|2|**all\_transactions**|Executada a função|Lista de dicionários com todas as transações do arquivo JSON|
|2|**post\_transaction**|Executada a função|Dicionário da transação adicionada|
|1|**calculate\_balance**|Executada a função|Saldo atual considerando todas as transações listadas no arquivo|

**Boa diversão, devs! 🧛‍♀️**

