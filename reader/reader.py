import logging
import pandas as pd
from collections import defaultdict
import math

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Reader:
    def read(argument: str):
        pass

class ReaderCSV(Reader):
    def process_first_block(self, dict_u, row, id, id_for_new_query):
        id = row[4]
        if math.isnan(float(id)) and str(row[6]) != 'nan':
            id = str(id_for_new_query)
            id_for_new_query += 1
        dict_u[id].append(row)
        return id, id_for_new_query

    def dataframe_to_dict(self, df):
        dict_u = defaultdict(list)
        id_for_new_query = 1
        flag_start_block = True
        id = 0
        count = 0
        for index, row in df.iterrows():
            count +=1
            if flag_start_block == True:
                id, id_for_new_query = self.process_first_block(dict_u, row, id, id_for_new_query)
                flag_start_block = False
            else:
                if row.isna().all() == True:
                    flag_start_block = True
                else:
                    dict_u[id].append(row)
                    flag_start_block = False
        print(count)
        return dict_u
        
    def read(self, file_path):
        logger.info("Reading file")
        df = pd.read_csv(file_path, sep='\t')
        return self.dataframe_to_dict(df)