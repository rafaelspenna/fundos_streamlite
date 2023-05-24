import zipfile
import os
import pandas as pd
import time
import pyarrow.feather as feather

downloaded_path = '/home/rafael/virtual_enviroments/streamlit_funds/downloads'
csv_path = '/home/rafael/virtual_enviroments/streamlit_funds/csv_files'
merged_path = '/home/rafael/virtual_enviroments/streamlit_funds/csv_files/merged/merged.csv' 
start_time = time.time()

def unzip_all_files(downloaded_path: str, output_path: str) -> None:
    for file in os.listdir(downloaded_path):
        if file.endswith('.zip'):
            file_path = os.path.join(downloaded_path, file)
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(output_path)

def merge_csv_to_feather(csv_files_path: str):
    data_frames = []
    columns_to_read = ['CNPJ_FUNDO', 'DT_COMPTC', 'VL_TOTAL', 'VL_QUOTA', 'VL_PATRIM_LIQ', 'CAPTC_DIA', 'RESG_DIA', 'NR_COTST'] 
    dtypes = {'CNPJ_FUNDO': 'str', 'DT_COMPTC': 'object', 'VL_TOTAL': 'float', 'VL_QUOTA': 'float',
               'VL_PATRIM_LIQ': 'float', 'CAPTC_DIA': 'float', 'RESG_DIA': 'float', 'NR_COTST': 'Int64'}
    
    # Convert CSV files to Feather format
    for file in os.listdir(csv_files_path):
        if file.endswith('.csv'):
            file_path = os.path.join(csv_files_path, file)
            df = pd.read_csv(file_path, sep=';', usecols=columns_to_read, dtype=dtypes,
                             na_values='0', parse_dates=['DT_COMPTC'])
            feather_path = os.path.splitext(file_path)[0] + '.feather'
            feather.write_feather(df, feather_path)
            data_frames.append(feather_path)

#def merge_all_csv(csv_files_path: str, merged_path: str) -> None:
#    data_frames = []
#    columns_to_read = ['CNPJ_FUNDO', 'DT_COMPTC', 'VL_TOTAL', 'VL_QUOTA', 'VL_PATRIM_LIQ', 'CAPTC_DIA', 'RESG_DIA', 'NR_COTST'] 
#    dtypes = {'CNPJ_FUNDO': 'str', 'DT_COMPTC': 'object', 'VL_TOTAL': 'float', 'VL_QUOTA': 'float',
#               'VL_PATRIM_LIQ': 'float', 'CAPTC_DIA': 'float', 'RESG_DIA': 'float', 'NR_COTST': 'Int64'}
#    for file in os.listdir(csv_files_path):
#        if file.endswith('.csv'):
#            file_path = os.path.join(csv_files_path, file)
#            df = pd.read_csv(file_path, sep=';', usecols=columns_to_read, dtype=dtypes, 
#                             na_values='0', parse_dates=['DT_COMPTC'])
#            data_frames.append(df)
#    csv_data = pd.concat(data_frames, ignore_index=True)
#    csv_data.to_csv(merged_path, index=False)

#unzip_all_files(downloaded_path, csv_path)
merge_csv_to_feather(csv_path)
#merge_all_csv(csv_path, merged_path)
print("--- %s seconds ---" % (time.time() - start_time))