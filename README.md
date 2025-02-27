# Projeto de Validação e Resposta Matemática com LangChain, LangGraph e NetWork

Este projeto oferece uma solução para validar perguntas matemáticas e obter respostas utilizando um "Professor Virtual", com a integração da biblioteca **LangChain** e a criação de um grafo de fluxo de dados com **LangGraph**. O código é dividido em dois módulos principais, sendo um para validar a pergunta matemática e integrar com o modelo de linguagem, e outro para adicionar a camada de grafo com LangGraph para um fluxo de execução mais estruturado.

## Funcionalidades

1. **Validação de Perguntas Matemáticas**: As perguntas inseridas pelo usuário são validadas utilizando expressões regulares, garantindo que contenham símbolos matemáticos, como `+`, `-`, `*`, `/`, `=`, etc.
2. **Integração com o Professor Virtual**: O modelo de linguagem **Llama3-70b-8192** é utilizado para responder às perguntas matemáticas do usuário. O modelo é inicializado através do **LangChain** e utiliza a chave da API do Groq para interação com o modelo.
3. **Utilização de LangGraph**: No segundo código, foi introduzido o uso do **LangGraph** para criar um fluxo de execução de dados, criando um grafo de nós (nós de recepção e professor virtual) e arestas (fluxo de dados entre os nós).

## Requisitos

- **Python 3.x**
- **Bibliotecas necessárias**:
    - `re` (expressões regulares)
    - `json` (manipulação de dados JSON)
    - `os` (acesso a variáveis de ambiente)
    - `dotenv` (para carregar variáveis de ambiente de um arquivo `.env`)
    - `langchain` (framework para trabalhar com modelos de linguagem)
    - `langgraph` (framework para criar grafos de fluxo de dados)
    - `networkx` (para criar e visualizar grafos)

  Para instalar as dependências, use o seguinte comando:

    ```bash
    pip install python-dotenv langchain langgraph networkx
    ```

## Passos para Execução

### Passo 1: Configuração do Ambiente

Antes de executar o código, é necessário configurar sua chave da API do **Groq**. Crie um arquivo `.env` no mesmo diretório do código e adicione a chave da API:

```env
GROQ_API_KEY=your_api_key_here

```


### Passo 2: Execução do Código

#### **Código 1: Validação de Perguntas e Integração com o Professor Virtual**

1. **Recebe a pergunta matemática do usuário.**
   - O código solicita que o usuário insira uma pergunta matemática via input no terminal.
   
2. **Valida a presença de símbolos matemáticos na pergunta.**
   - A validação é feita utilizando uma expressão regular para garantir que a pergunta contenha operadores matemáticos como `+`, `-`, `*`, `/`, `=`, etc.

3. **Envia a pergunta validada para o modelo de linguagem Llama3-70b-8192.**
   - Se a pergunta for válida, ela é enviada para o modelo de linguagem **Llama3-70b-8192** por meio da integração com o **Groq API**.

4. **Exibe a resposta do modelo de linguagem.**
   - Após a execução do modelo, a resposta gerada é exibida no terminal para o usuário.

#### Exemplo de execução:

```bash
Digite sua pergunta matemática: 3 + 4 * 5
Dados enviados para o Professor Virtual: {
    "pergunta": "3 + 4 * 5",
    "categoria": "matemática"
}
A resposta para sua pergunta '3 + 4 * 5' é: 23


```


