# projeto-Softex-LLM-P0

Repositório criado para o P0-PRIMEIRO-FLUXO-LLM da Softex

## 🎯 O problema

Uma professora de inglês autônoma controla os pagamentos dos alunos por mensagens soltas: quem paga quanto, quando vence e quem já pagou. Esse formato dificulta saber, de relance, o que está em dia e o que está pendente.

## 💡 A solução

O script envia a mensagem para o modelo do Gemini junto com uma instrução (_prompt de sistema_) que define o papel de **assistente financeiro** e o formato exato da resposta. O resultado é uma lista padronizada, pronta para consulta:

```
- Nome: [Nome do aluno]
- Valor: [Valor do pagamento]
- Vencimento: [Data de vencimento]
- Status: [Pago ou Pendente]
```

## ⚙️ Como funciona

1. Carrega a chave da API a partir do arquivo `.env` (`python-dotenv`).
2. Inicializa o cliente do Google GenAI.
3. Monta o prompt: **instrução** (papel + formato de saída) + **mensagem** (dados dos alunos).
4. Chama `client.models.generate_content(...)` com o modelo Gemini configurado.
5. Exibe a lista gerada no terminal.

## 🧰 Tecnologias

- Python 3.9+
- [Google GenAI SDK](https://github.com/googleapis/python-genai) (`google-genai`)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- Modelo Gemini (definido em `src/app.py`)

## 📁 Estrutura do projeto

```
projeto-softex-llm-p0/
├── src/
│   └── app.py          # Script principal (prompt + chamada ao Gemini)
├── .env.example        # Modelo do arquivo de variáveis de ambiente
├── .gitignore          # Ignora o .env para não vazar a chave
├── requirements.txt    # Dependências do projeto
└── README.md
```

## 🚀 Como executar

### 1. Pré-requisitos

- Python 3.9 ou superior
- Uma chave de API do Gemini (gratuita no [Google AI Studio](https://aistudio.google.com/apikey))

### 2. Clone o repositório

```bash
git clone https://github.com/renatovsantos/projeto-Softex-LLM-P0.git
cd projeto-Softex-LLM-P0
```

### 3. Crie e ative um ambiente virtual (recomendado)

```bash
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Configure a chave da API

Copie o arquivo de exemplo e preencha com a sua chave:

```bash
# Linux / macOS
cp .env.example .env

# Windows
copy .env.example .env
```

Edite o `.env`:

```env
GEMINI_API_KEY="sua-chave-aqui"
```

### 6. Execute

```bash
python src/app.py
```

## 🖥️ Exemplo de uso

**Entrada** (a mensagem definida em `src/app.py`(Informações fictícias)):

> Olá, eu sou uma professora de inglês autônoma e preciso de ajuda para organizar as informações de pagamento dos meus alunos. Os alunos João da Silva, Maria de Oliveira, Fernando Henrique e Ana Paula pagam respectivamente R$ 200,00, R$ 150,00, R$ 180,00 e R$ 160,00. Os vencimentos são 10/10/2023, 15/10/2023, 20/10/2023 e 25/10/2023. João e a Ana Paula já fizeram o pagamento. Os demais estão pendentes.

**Saída esperada** (o texto exato pode variar a cada execução):

```
- Nome: João da Silva
- Valor: R$ 200,00
- Vencimento: 10/10/2023
- Status: Pago

- Nome: Maria de Oliveira
- Valor: R$ 150,00
- Vencimento: 15/10/2023
- Status: Pendente

- Nome: Fernando Henrique
- Valor: R$ 180,00
- Vencimento: 20/10/2023
- Status: Pendente

- Nome: Ana Paula
- Valor: R$ 160,00
- Vencimento: 25/10/2023
- Status: Pago
```

## 🛠️ Personalização

Para usar com os seus próprios dados, edite as variáveis em `src/app.py`:

| Variável    | O que faz                                                       |
| ----------- | --------------------------------------------------------------- |
| `instrucao` | Define o papel do assistente e o formato da resposta            |
| `mensagem`  | Texto com os dados a serem organizados (alunos, valores, datas) |
| `model`     | Modelo Gemini usado na chamada a `generate_content`             |
