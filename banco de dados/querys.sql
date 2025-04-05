--Criar tabela Operadoras

CREATE TABLE operadoras (
    registro_ans VARCHAR(20) PRIMARY KEY,
    cnpj VARCHAR(20),
    razao_social VARCHAR(255) NOT NULL,
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    cidade VARCHAR(100),
    uf CHAR(2),
    cep VARCHAR(10),
    data_registro_ans DATE
);
_________________________________________

--Criar tabela Demonstração contábeis

CREATE TABLE demonstracoes_contabeis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    registro_ans VARCHAR(20),
    data DATE NOT NULL,
    codigo_conta VARCHAR(50),
    descricao_conta VARCHAR(255),
    valor DECIMAL(15,2),
    FOREIGN KEY (registro_ans) REFERENCES operadoras(registro_ans)
);
_________________________________________

--Importar Relatorio_cadop.csv

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 9.2/Uploads/Relatorio_cadop.csv'
INTO TABLE operadoras
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
_________________________________________

--Importar dados Contábeis (alterar nome do csv para cada trimestre)

LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 9.2/Uploads/1T2023.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY '|'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(data, registro_ans, codigo_conta, descricao_conta, @valor)
SET valor = NULLIF(@valor, '');
_________________________________________

--Query - TOP 10 operadoras ultimo trimestre

SELECT 
    o.razao_social,
    o.uf,
    SUM(d.valor) AS total_despesas
FROM 
    demonstracoes_contabeis d
JOIN 
    operadoras o ON d.registro_ans = o.registro_ans
WHERE 
    d.descricao_conta LIKE '%EVENTOS/%SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
    AND d.data >= DATE_SUB((SELECT MAX(data) FROM demonstracoes_contabeis), INTERVAL 3 MONTH)
GROUP BY 
    o.razao_social, o.uf
ORDER BY 
    total_despesas DESC
LIMIT 10;
_________________________________________

--Query - TOP Operadoras ultimo ano
SELECT 
    o.razao_social,
    o.uf,
    SUM(d.valor) AS total_despesas_anual
FROM 
    demonstracoes_contabeis d
JOIN 
    operadoras o ON d.registro_ans = o.registro_ans
WHERE 
    d.descricao_conta LIKE '%EVENTOS/%SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
    AND d.data >= DATE_SUB((SELECT MAX(data) FROM demonstracoes_contabeis), INTERVAL 1 YEAR)
GROUP BY 
    o.razao_social, o.uf
ORDER BY 
    total_despesas_anual DESC
LIMIT 10;