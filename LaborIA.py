
# Importa módulo para interagir com o sistema operacional
import os

# Importa a biblioteca Streamlit para criar a interface web interativa
import streamlit as st

# Importa a classe Groq para se conectar à API da plataforma Groq e acessar o LLM
from groq import Groq

# Configura a página do Streamlit com título, ícone, layout e estado inicial da sidebar
st.set_page_config(
    page_title="LaborIA",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define um prompt de sistema que descreve as regras e comportamento do assistente de IA
CUSTOM_PROMPT = """
Você é o "Consultor CLT", um assistente de IA especialista em leis trabalhistas brasileiras. Sua missão é ajudar trabalhadores a compreenderem seus direitos e deveres de forma clara, humanizada e baseada estritamente na Consolidação das Leis do Trabalho (CLT).

REGRAS DE OPERAÇÃO:

Foco em Direito do Trabalho: Responda apenas a perguntas relacionadas à CLT, direitos trabalhistas, deveres do empregado/empregador e procedimentos legais do trabalho. Se o usuário perguntar sobre outros ramos do direito ou assuntos diversos, responda educadamente que seu foco é exclusivamente a legislação trabalhista brasileira.

Estrutura da Resposta: Sempre formate suas respostas da seguinte maneira:

Explicação Legal: Comece com uma explicação clara e didática sobre o direito ou dever mencionado. Traduza o "juridiquês" para uma linguagem acessível.

Referência na CLT: Cite o(s) artigo(s) específico(s) da CLT que fundamentam a resposta. Transcreva o trecho principal se for relevante.

Providências Práticas: Forneça um guia passo a passo de quais ações o usuário pode tomar na situação descrita (ex: conversar com o RH, buscar o sindicato, registrar provas, etc.).

Aviso de Isenção (Disclaimer): Ao final, inclua obrigatoriamente uma nota informando que você é uma IA e que suas orientações são educativas, não substituindo a consulta com um advogado especializado.

📚 Fonte Oficial: Inclua um link direto para a CLT no portal do Planalto (presidencia.gov.br) ou para o artigo específico pesquisado.

Clareza e Precisão: Use uma linguagem acolhedora, mas tecnicamente precisa. Evite opiniões pessoais; baseie-se na lei e na jurisprudência consolidada.
"""

# Cria o conteúdo da barra lateral no Streamlit
with st.sidebar:
    
    # Define o título da barra lateral
    st.title("💼 LaborIA")
    
    # Mostra um texto explicativo sobre o assistente
    st.markdown("Um assistente de IA focado em Direito do Trabalho para ajudar trabalhadores.")
    
    # Campo para inserir a chave de API da Groq
    groq_api_key = st.text_input(
        "Insira sua API Key Groq", 
        type="password",
        help="Obtenha sua chave em https://console.groq.com/keys"
    )

    # Adiciona linhas divisórias e explicações extras na barra lateral
    st.markdown("---")
    st.markdown("Desenvolvido para auxiliar em suas dúvidas de Direito do Trabalho com base na CLT. IA pode cometer erros. Sempre verifique as respostas.")

    st.markdown("---")
    st.markdown("Conheça o meu GitHub de projetos:")

    # Link para o github
    st.markdown("🔗 [Maria_Laura 梅花](https://github.com/Maria-laura-cruvinel)")
    


# Título principal do app
st.title("LaborIA")

# Subtítulo adicional
st.title("Assistente Pessoal de Direito do Trabalho 🧑‍💼")

# Texto auxiliar abaixo do título
st.caption("Faça sua pergunta sobre a CLT e obtenha explicações e referências.")

# Inicializa o histórico de mensagens na sessão, caso ainda não exista
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe todas as mensagens anteriores armazenadas no estado da sessão
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Inicializa a variável do cliente Groq como None
client = None

# Verifica se o usuário forneceu a chave de API da Groq
if groq_api_key:
    
    try:
        
        # Cria cliente Groq com a chave de API fornecida
        client = Groq(api_key = groq_api_key)
    
    except Exception as e:
        
        # Exibe erro caso haja problema ao inicializar cliente
        st.sidebar.error(f"Erro ao inicializar o cliente Groq: {e}")
        st.stop()

# Caso não tenha chave, mas já existam mensagens, mostra aviso
elif st.session_state.messages:
     st.warning("Por favor, insira sua API Key da Groq na barra lateral para continuar.")

# Captura a entrada do usuário no chat
if prompt := st.chat_input("Qual sua dúvida sobre a CLT?"):
    
    # Se não houver cliente válido, mostra aviso e para a execução
    if not client:
        st.warning("Por favor, insira sua API Key da Groq na barra lateral para começar.")
        st.stop()

    # Armazena a mensagem do usuário no estado da sessão
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Exibe a mensagem do usuário no chat
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepara mensagens para enviar à API, incluindo prompt de sistema
    messages_for_api = [{"role": "system", "content": CUSTOM_PROMPT}]
    for msg in st.session_state.messages:
        
        messages_for_api.append(msg)

    # Cria a resposta do assistente no chat
    with st.chat_message("assistant"):
        
        with st.spinner("Analisando sua pergunta..."):
            
            try:
                
                # Chama a API da Groq para gerar a resposta do assistente
                chat_completion = client.chat.completions.create(
                    messages = messages_for_api,
                    model = "openai/gpt-oss-20b", 
                    temperature = 0.7,
                    max_tokens = 2048,
                )
                
                # Extrai a resposta gerada pela API
                clt_ai_resposta = chat_completion.choices[0].message.content
                
                # Exibe a resposta no Streamlit
                st.markdown(clt_ai_resposta)
                
                # Armazena resposta do assistente no estado da sessão
                st.session_state.messages.append({"role": "assistant", "content": clt_ai_resposta})

            # Caso ocorra erro na comunicação com a API, exibe mensagem de erro
            except Exception as e:
                st.error(f"Ocorreu um erro ao se comunicar com a API da Groq: {e}")




