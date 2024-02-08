
import string
import sys

import pandas as pd

excel_path = "cards.xlsx"
server_out_path = "../FusionServer/Data/CardsServer.csv"
client_out_path = "../FusionClient/Data/CardsClient.csv"
shared_out_path = "shared/CardsData.csv"

START_INDEX : int = 2

serverKeys = ["name", "power", "toughness", "elements", "abilities"]
clientKeys = ["name", "art_file"]

if __name__ == '__main__':
    if len(sys.argv) != 1 and len(sys.argv) != 4:
        print("Usage: ./main.py")
        print("Run with parameters: ./main.py <excel_path> <server_out_path> <client_out_path>")
        sys.exit(1)
    
    df = pd.read_excel(excel_path, keep_default_na=False)
    keys = df.columns.values.flatten().tolist()
    
    ###############################################################################
    dfShared = df.copy()
    dfShared.to_csv(shared_out_path, header=True, index=False, lineterminator='\n')
    print("Saving shared data to " + shared_out_path)
    
    """
    ###############################################################################
    
    dfServer = df.copy()
    unusedServerKeys = [k for k in keys if k not in serverKeys]
    dfServer = dfServer.drop(unusedServerKeys, axis=1)
    dfServer.to_csv(server_out_path, header=True, index=False, lineterminator='\n')
    print("Saving server data to " + server_out_path)
    
    ###############################################################################
    
    dfClient = df.copy()
    unusedClientKeys = [k for k in keys if k not in clientKeys]
    dfClient = dfClient.drop(unusedClientKeys, axis=1)
    dfClient.to_csv(client_out_path, header=True, index=False, lineterminator='\n')
    print("Saving client data to " + client_out_path)
    """
