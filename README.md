
Projeto de Teste de Nivelamento - Estágio
📝 Descrição do Projeto
Este repositório contém minha solução para o teste técnico de estágio, composto por 4 tarefas principais:

Teste 1 - Web Scraping (Coleta de PDFs do site da ANS com Python)
Teste 2 - Transformação de Dados (Extrair tabelas de PDF para CSV e substituir abreviações)
Teste 3 - Banco de Dados (Importar dados CSV para MySQL e criar queries analíticas)
Teste 4 - API e Interface Web (Backend em Flask + Frontend em Vue.js para busca de operadoras)

🛠️ Tecnologias Utilizadas
Tarefa	Tecnologias
Teste 1 - Web Scraping  |   Python + compactação ZIP
Teste 2 - Transformação de Dados    |	Python + tratamento de CSV
Teste 3 - Banco de Dados	|   MySQL (criação de tabelas, importação CSV e queries analíticas)
Teste 4 - API	|   Python, Vue.js e Axios

🔍 Detalhes das Tarefas
✅ Teste 1 - Web Scraping
-Script Python que acessa o site da ANS e faz download dos Anexos I e II em PDF.
-Compacta os arquivos em um ZIP para facilitar o armazenamento.

✅ Teste 2 - Transformação de Dados
-Extrai a tabela "Rol de Procedimentos e Eventos em Saúde" do PDF (Anexo I).
-Salva os dados em CSV com estruturação adequada.
-Substitui abreviações (OD → Odontológico, AMB → Ambulatorial...) conforme legenda.
-Compacta o CSV final em Teste_[Nome].zip.

⚠️ Teste 3 - Banco de Dados (Desafio Enfrentado)
-Baixar os dados cadastrais das operadoras ativas e demonstrações contábeis.
-Cria tabelas no MySQL e importa os dados.
-Desenvolve queries para identificar as 10 operadoras com maiores despesas hospitalares.
-Dificuldade: Pouca familiaridade com MySQL (mais experiência com SQL Server).

✅ Teste 4 - API e Frontend
🔹Backend (Flask - Python)
-Rota /api/operadoras → Busca textual nos dados das operadoras.
-Integração com CSV → Processamento eficiente usando Pandas.

🔹 Frontend (Vue.js)
-Campo de busca em tempo real → Exibe resultados dinamicamente.
-Responsivo → Funciona em desktop e mobile.

🚀 Como Executar (Teste 4 - API + Frontend)
🔹Passo a Passo
1️⃣ Backend (API)
-Abra o terminal e digite
cd teste-4-api/backend  
pip install -r requirements.txt  
python app.py   //Servidor roda em http://localhost:5000  

2️⃣ Frontend (Vue.js)
Abra o terminal e digite
cd teste-4-api/frontend  
npm install  
npm run dev  //Acesse http://localhost:5173 

📌 Observações Finais
Testes 1 e 2: Scripts completos para web scraping e transformação de dados.
Teste 3 (MySQL): Tive dificuldades, mas mantive os scripts para demonstração.
Teste 4 (API + Frontend): Foco principal, com solução funcional e bem documentada.

🔗 Link do Repositório: GitHub - https://github.com/pedrojoscard/teste-nivelamento

Agradeço pela oportunidade! 🚀