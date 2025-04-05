import os
import zipfile
import pandas as pd
import pdfplumber

MEU_NOME = "PEDRO JOSE CARDOSO"
ANEXO1_PDF = "Anexo_I.pdf"
CSV_NAME = "Rol_Procedimentos.csv"
ZIP_OUTPUT = f"TESTE {MEU_NOME}.zip"

ABREVIACOES = {
    'OD': 'Odontológico',
    'AMB': 'Ambulatorial',
    'HCO': 'Hospitalar com obstetrícia',
    'HSO': 'Hospitalar sem obstetrícia',
    'REF': 'Plano referência',
    'PAC': 'Procedimento de alta complexidade',
    'DUT': 'Diretriz de utilização'
}

def extrair_tabelas(pdf_path):
    try:
        print("Extraindo tabelas do PDF...")
        all_tables = []
        
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                tables = page.extract_tables()
                for table in tables:
                    df = pd.DataFrame(table[1:], columns=table[0])
                    all_tables.append(df)
        
        return pd.concat(all_tables, ignore_index=True)
    except Exception as e:
        print(f"Erro ao extrair tabelas: {e}")
        return None

def processar_dados(df):
    print("Processando dados...")
    for col in df.columns:
        if col in ABREVIACOES:
            df[col] = df[col].replace(ABREVIACOES)
    return df.dropna(how='all')

def salvar_e_compactar(df):
    try:
        df.to_csv(CSV_NAME, index=False, encoding='utf-8-sig')
        with zipfile.ZipFile(ZIP_OUTPUT, 'w') as zipefile:
            zipfile.write(CSV_NAME)
        os.remove(CSV_NAME)
        print(f"Arquivo {ZIP_OUTPUT} criado com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar: {e}")

if __name__ == "__main__":
    if not os.path.exists(ANEXO1_PDF):
        print("Execute primeiro o Teste 1 para baixar o PDF")
    else:
        df = extrair_tabelas(ANEXO1_PDF)
        if df is not None:
            df = processar_dados(df)
            salvar_e_compactar(df)