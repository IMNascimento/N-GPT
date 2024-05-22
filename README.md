<h1 align="center">
  <br>
  <a href="#"><img src="https://github.com/IMNascimento/DVR/assets/28989407/84028706-5a9e-4d00-af2c-2935e5604035" alt="Nascimento" width="200"></a>
  <br>
  N-GPT Project
  <br>
</h1>
Bem-vindo ao Projeto N-GPT! Este projeto é um aplicativo de bate-papo desenvolvido com Streamlit que integra os modelos GPT da OpenAI para IA conversacional, para personalização e pre treino se necessario do modelo, para um assistente customizável. O projeto está estruturado para ser modular, escalável e fácil de estender.

## Table of Contents

- [Features](#features)
- [Estrutura do projeto](#project-structure)
- [Instalação](#installation)
- [Uso](#usage)
- [Testes](#testing)
- [Configuração](#configuration)
- [Contribuindo](#contributing)
- [Licença](#license)

## Features

- Converse com os modelos GPT-3.5 e GPT-4.
- Salvar e carregar conversas.
- Configure chaves de API via `.env` ou configurações do usuário.
- Estrutura de código modular para fácil manutenção e extensão.
- Testes automatizados para garantir qualidade e funcionalidade do código.

## Estrutura do projeto

project_root/
│
├── .env
├── src/
│ ├── gpt.py
│ ├── ngpt.py
│ └── file_manager.py
├── messages/
├── setup/
│ └── api_key (optional)
└── tests/
├── test_file_manager.py
├── test_openai_api.py
└── init.py


- **src/**: Contém o código principal do aplicativo.
- **messages/**: Diretório para armazenar logs de conversas.
- **setup/**: Diretório para configurações específicas do usuário.
- **tests/**: Contém testes de unidade para o aplicativo.

## Instalação

1. Clonar o repositório:
    ```bash
    git clone https://github.com/IMNascimento/N-GPT.git
    cd N-GPT
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Instale os pacotes necessários:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure seu arquivo `.env` na raiz do projeto:
    ```
    API_KEY=your_openai_api_key
    ```

## Uso

Para executar o aplicativo:
```bash
streamlit run src/ngpt.py
``` 

Isso iniciará o servidor Streamlit e abrirá o aplicativo em seu navegador padrão.

## Testes
Para executar os testes, use o seguinte comando:

```bash
python -m unittest discover -s tests
```

Isso descobrirá e executará todos os testes de unidade no diretório de testes.

## Configuração
Você pode configurar sua chave de API de duas maneiras:

<strong>Variáveis de ambiente:</strong> Defina API_KEY em seu arquivo .env localizado na raiz do projeto.
<strong>Configurações do usuário:</strong> adicione ou altere a chave API por meio da guia de configurações na IU do aplicativo.

## Contribuindo
Aceitamos contribuições! Por favor, leia nosso CONTRIBUTING.md para obter orientações sobre como contribuir para este projeto.

## Licença
Este projeto está licenciado sob a licença GPL3. Consulte o arquivo LICENSE para obter mais detalhes.

