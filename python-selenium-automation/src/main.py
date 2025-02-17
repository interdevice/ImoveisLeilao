import os
import pandas as pd
from automation.scraper import Scraper
from data.process_data import create_dataframe
from utils.helpers import load_env

def main():
   # Carregar variáveis de ambiente
    load_env()

    # Definir o caminho de download
    download_path = os.path.join('C:\\Users\\lhmaria1\\OneDrive - Stefanini\\Documents\\Caixa\\Imoveis\\python-selenium-automation\\src\\utils\\downloads')

    # Criar a pasta de download se não existir
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # Definir o caminho do arquivo CSV
    file_path = os.path.join(download_path, 'Lista_imoveis_SP.csv')
    output_file_path = os.path.join(download_path, 'verificacao.xlsx')

    # Apagar os arquivos existentes, se houver
    if os.path.exists(file_path):
        os.remove(file_path)
    if os.path.exists(output_file_path):
        os.remove(output_file_path)

    # Criar uma instância do Scraper
    scraper = Scraper(download_path)

    # Verificar se o arquivo já existe
    if not os.path.exists(file_path):
        # Baixar o arquivo Excel
        scraper.download_file()

    # Processar os dados e criar um DataFrame
    df = scraper.extract_data(file_path)

    # Aplicar trim na coluna 'Cidade'
    df['Cidade'] = df['Cidade'].str.strip()

    # Converter valores monetários para float
    df['Valor de avaliação'] = df['Valor de avaliação'].str.replace('.', '').str.replace(',', '.').astype(float)

     # Aplicar filtro no DataFrame
    cidades_desejadas = ['COTIA', 'DIADEMA', 'FERRAZ DE VASCONCELOS', 'FRANCISCO MORATO', 'GUARUJA', 'GUARULHOS', 'ITAPECERICA DA SERRA', 'ITAQUAQUECETUBA', 'JUNDIAI', 'MAIRINQUE', 'MAUA', 'MOGI DAS CRUZES', 'OSASCO', 'POA', 'PRAIA GRANDE', 'RIBEIRAO PIRES', 'SANTO ANDRE', 'SANTOS', 'SAO BERNARDO DO CAMPO', 'SAO CAETANO DO SUL', 'SAO PAULO', 'SAO VICENTE', 'SUZANO', 'TABOAO DA SERRA', 'VINHEDO']
    df_filtrado = df[(df['Cidade'].isin(cidades_desejadas)) & (df['Descrição'].str.contains('casa|apartamento', case=False, na=False)) & (df['Valor de avaliação'] <= 300000.00)]

    # Abrir os links no navegador
    scraper.open_links(df_filtrado['Link de acesso'])

    # Salvar o DataFrame em um arquivo Excel
    df_filtrado.to_excel(output_file_path, index=False)

    print(f"Arquivo Excel salvo em: {output_file_path}")

if __name__ == "__main__":
    main()