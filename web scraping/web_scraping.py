import requests
import zipfile
import os

anexo1_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
anexo2_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"

anexo1_nome = "Anexo_I.pdf"
anexo2_nome = "Anexo_II.pdf"

try:
    print(f"Baixando o pdf {anexo1_nome}...")
    resposta1 = requests.get(anexo1_url)
    with open(anexo1_nome, 'wb') as f:
        f.write(resposta1.content)

    print(f"Baixando o pdf {anexo2_nome}...")
    resposta2 = requests.get(anexo2_url)
    with open(anexo2_nome, 'wb') as f:
        f.write(resposta2.content)

    with zipfile.ZipFile('Anexos - Web Scraping.zip', 'w') as zipf:
        zipf.write(anexo1_nome)
        zipf.write(anexo2_nome)
    
    print("\nOs arquivos foram enviados para o 'Anexos - Web Scraping.zip'")

except Exception as e:
    print(f"Ocorreu um erro: {e}")