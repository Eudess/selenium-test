import os
import pandas as pd

def remove_file(dir_csv):
    """
    Esta é uma função que remove arquivos csv.

    Argumentos:
    parametro1: Caminho da pasta csv.

    Retorna:
    None.
    """
    files = os.listdir(dir_csv)
    for csv_file in files:
        if csv_file.endswith(".csv"):
            file_path = os.path.join(dir_csv, csv_file)
            os.remove(file_path)

def obesity_data():
    project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
    dir_csv = os.path.join(project_dir, "csv")
    dir_result = os.path.join(project_dir, "result")

    national_csv = [os.path.join(dir_csv, csv_file) for csv_file in os.listdir(dir_csv) if csv_file.endswith(".csv") and "LakeCounty" in csv_file][0]
    california_csv = [os.path.join(dir_csv, csv_file) for csv_file in os.listdir(dir_csv) if csv_file.endswith(".csv") and "california" in csv_file][0]


    df_national = pd.read_csv(national_csv, sep=",")
    df_california = pd.read_csv(california_csv, sep=",")

    filter_california_df = df_national[df_national["NAME"] == "California"]

    california_obesity = filter_california_df["Obesity"].values[0]
    df_california[" California Obesity Rate"] = california_obesity

    category = df_california[df_california["Category"] == "All "]

    if not os.path.exists(dir_result):
        os.makedirs(dir_result)
    
    df_california.to_excel(f"{dir_result}/california_obesity.xlsx", index=False)
    category.to_excel(f"{dir_result}/category_california_obesity.xlsx", index=False)

    # remove_file(dir_csv)