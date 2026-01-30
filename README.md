# 💼 LaborIA: Assistente de Direito do Trabalho (CLT)

O **LaborIA** é uma aplicação web interativa desenvolvida para ajudar trabalhadores brasileiros a entenderem seus direitos e deveres. Utilizando Inteligência Artificial, ele traduz a complexidade da CLT para uma linguagem acessível e prática.



## 🚀 Tecnologias Utilizadas

Este projeto foi construído utilizando:

* **[Streamlit](https://streamlit.io/):** Um framework potente em Python que transforma scripts de dados em interfaces web compartilháveis em minutos. É ele que cuida de toda a interface visual (botões, barra lateral e chat).
* **[Groq Cloud](https://groq.com/):** Uma plataforma de inferência de IA ultra-rápida. Utilizamos a biblioteca da Groq para acessar Modelos de Linguagem de Grande Escala (LLMs) que processam as perguntas e geram as respostas baseadas na lei.
* **Python:** A linguagem base para toda a lógica de integração.

## 🛠️ Como Funciona a Integração

### Streamlit (A Interface)
O Streamlit gerencia o **Session State** (estado da sessão), o que permite que o chat "lembre" das perguntas anteriores durante a conversa. Ele também facilita a entrada de dados sensíveis, como a API Key, através de campos de texto mascarados (`type="password"`).

### Groq (O Cérebro)
Quando você faz uma pergunta, o código envia um **System Prompt** (instruções mestre) junto com a sua dúvida para os servidores da Groq. A Groq processa isso em milissegundos e devolve uma resposta estruturada com referências legais.

## 📋 Pré-requisitos

Antes de começar, você precisará de:
1.  Python instalado (versão 3.8 ou superior).
2.  Uma **API Key da Groq**. Você pode gerar uma gratuitamente em [Groq Cloud Console](https://console.groq.com/keys).

## 🔧 Instalação e Execução

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/Maria-laura-cruvinel/LaborIA.git](https://github.com/Maria-laura-cruvinel/LaborIA.git)
   cd LaborIA

**Instale as dependências:**

```bash
pip install -r requirements.txt
```
**Execute a aplicação:**

```bash
python -m streamlit run AssistenteCLT.py
```
## 📖 Como Usar
Ao abrir o link local gerado pelo Streamlit, vá até a barra lateral esquerda.

Insira sua Groq API Key.

No campo de chat na parte inferior, digite sua dúvida (ex: "Como funciona o aviso prévio trabalhado?").

A IA responderá com a explicação legal, o artigo da CLT correspondente e os passos práticos que você deve tomar.
