bi_agrocredi/
│
├── assets/                # Arquivos estáticos (CSS, imagens, favicon)
│   └── style.css
│
├── pages/                 # Páginas individuais do Dash
│   ├── home.py
│   ├── monitoramento_rpa.py
│   └── share_mercado.py
│
├── components/            # Componentes reutilizáveis (cards, filtros, menus)
│   ├── sidebar.py
│   └── cards.py
│
├── utils/                 # Funções auxiliares, gráficos, ETL, etc.
│   ├── graphs.py
│   └── data.py
│
├── data/          # <<<< Pasta para conexão, queries e tratamento de dados
│   ├── connection.py      # Conexão com o banco de dados
│   ├── queries.py         # SQLs organizadas
│   └── transform.py       # Funções de tratamento, limpeza, transformação
│
├── app.py                 # Inicialização do app Dash
├── index.py               # Roteamento principal entre páginas
├── requirements.txt       # Dependências do projeto
└── README.md              # Descrição do projeto
