# Projeto de Automação com Selenium e Pandas

Este projeto tem como objetivo automatizar o download de um arquivo Excel a partir do site da Caixa Econômica Federal e processar os dados contidos nesse arquivo utilizando a biblioteca Pandas.

## Estrutura do Projeto

```
python-selenium-automation
├── src
│   ├── main.py               # Ponto de entrada da aplicação
│   ├── automation
│   │   └── scraper.py        # Classe para automação do download e extração de dados
│   ├── data
│   │   └── process_data.py    # Função para criar DataFrame a partir do arquivo Excel
│   └── utils
│       └── helpers.py        # Funções auxiliares
├── requirements.txt           # Dependências do projeto
├── .env                       # Variáveis de ambiente
└── README.md                  # Documentação do projeto
```

## Instalação

1. Clone o repositório:
   ```
   git clone <URL_DO_REPOSITORIO>
   cd python-selenium-automation
   ```

2. Crie um ambiente virtual e ative-o:
   ```
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate     # Para Windows
   ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

## Uso

1. Configure as variáveis de ambiente no arquivo `.env` conforme necessário.
2. Execute o script principal:
   ```
   python src/main.py
   ```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.