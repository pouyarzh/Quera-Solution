import pandas as pd
import csv

class csvAnalytics:

    def __int__(self):
        pass

    def read_csv_with_pandas(self,path):
        df = pd.read_csv(path)
        df = pd.DataFrame(df)
        return df

    def count_dataframe_row(self,dataframe):
        df = pd.DataFrame(dataframe)
        rows = len(df.axes[0])
        return rows

    def count_dataframe_column(self,dataframe):
        df = pd.DataFrame(dataframe)
        column = len(df.axes[1])
        return column

    def value_of_sepecific_column(self,df,columnName):
        df = pd.DataFrame(df)
        df = df[columnName]
        return df