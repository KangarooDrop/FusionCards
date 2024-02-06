
import string
import sys

import pandas as pd

excel_path = "cards.xlsx"
server_out_path = "CardsServer.csv"
client_out_path = "CardsClient.csv"

START_INDEX : int = 2

serverKeys = ["name", "power", "toughness", "abilities"]
clientKeys = ["name", "art_file"]

if __name__ == '__main__':
    if len(sys.argv) != 1 and len(sys.argv) != 4:
        print("Usage: ./main.py")
        print("Run with parameters: ./main.py <excel_path> <server_out_path> <client_out_path>")
        sys.exit(1)
    
    df = pd.read_excel(excel_path, keep_default_na=False)
    #df = pd.read_excel(excel_path)
    
    numRows : int = len(df.index)
    numColumns : int = len(df.iloc[0])
    keys = df.columns.values.flatten().tolist()
    
    ###############################################################################
    
    dfServer = df.copy()
    unusedServerKeys = [k for k in keys if k not in serverKeys]
    dfServer = dfServer.drop(unusedServerKeys, axis=1)
    dfServer.to_csv(server_out_path, header=False, index=False)
    print("Saving server data to " + server_out_path)
    
    ###############################################################################
    
    dfClient = df.copy()
    unusedClientKeys = [k for k in keys if k not in clientKeys]
    dfClient = dfClient.drop(unusedClientKeys, axis=1)
    dfClient.to_csv(client_out_path, header=False, index=False)
    print("Saving client data to " + client_out_path)
