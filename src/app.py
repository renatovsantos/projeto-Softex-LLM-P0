import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Inicializa o cliente GenAI com a chave da API do Gemini
client = genai.Client()

# Define a instrução e a mensagem. Nesse caso, usei uma situacao real de uma professora de 
# inglês autônoma que  precisa controlar o fluxo de pagamentos dos alunos. 
# Ela forneceu os dados em uma mensagem, mas precisa que sejam organizados em uma lista
#clara para facilitar o controle financeiro. 
instrucao = "Você deve agir como um assistente financeiro de uma professora de inglês, " \
"responsável por fornecer informações estruturadas em listas após receber uma " \
"solicitação." \
"Essa informação deve ser apresentada em uma lista clara com nome, valor de pagamento, " \
"data de vencimento e status." \
"Por favor, organize as informações em uma lista no formato: " \
"- Nome: [Nome do aluno] " \
"- Valor: [Valor do pagamento " \
"- Vencimento: [Data de vencimento] " \
"- Status: [informe se o valor foi pago ou está pendente]" \
" " \
# Mensagem que deve ser tratada pelo modelo. A mensagem contém informações sobre os alunos
# , valores de pagamento, datas de vencimento e status de pagamento.
mensagem = "Olá, eu sou uma professora de inglês autônoma e preciso de ajuda para " \
"organizar as informações de pagamento dos meus alunos. Os alunos João da Silva, Maria de Oliveira," \
"Fernando Henrique e Ana Paula pagam respectivamente R$ 200,00, R$ 150,00, R$ 180,00 e R$ 160,00." \
"Os vencimentos são 10/10/2023, 15/10/2023, 20/10/2023 e 25/10/2023." \
"João e a Ana Paula já fizeram o pagamento. Os demais estão pendentes" \

prompt = f"{instrucao}\n\nMensagem recebida:\n{mensagem}"

print("Elaborando lista. Aguarde, por favor...")

resposta = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt,
)

# Exibe a resposta do modelo
print("\nResultado:\n")
print(resposta.text)