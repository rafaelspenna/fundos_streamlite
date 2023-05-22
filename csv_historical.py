import zipfile
import os
import pandas as pd

downloaded_path = '/home/rafael/virtual_enviroments/streamlit_funds/downloads'
csv_path = '/home/rafael/virtual_enviroments/streamlit_funds/csv_files'
merged_path = '/home/rafael/virtual_enviroments/streamlit_funds/csv_files/merged/merged.csv' 

def unzip_all_files(downloaded_path: str, output_path: str) -> None:
    for file in os.listdir(downloaded_path):
        if file.endswith('.zip'):
            file_path = os.path.join(downloaded_path, file)
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(output_path)

def merge_all_csv(csv_files_path: str, merged_path: str) -> None:
    csv_data = pd.DataFrame()
    for file in os.listdir(csv_files_path):
        if file.endswith('.csv'):
            file_path = os.path.join(csv_files_path, file)
            df = pd.read_csv(file_path, sep=';')
            csv_data = pd.concat([csv_data, df])
    
    csv_data.to_csv(merged_path)

#unzip_all_files(downloaded_path, csv_path)
merge_all_csv(csv_path, merged_path)