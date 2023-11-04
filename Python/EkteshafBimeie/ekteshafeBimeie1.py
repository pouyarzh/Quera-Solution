from MainPythonProject.QueraProblemSet.QueraStartDate.PublicClasses.csvAnalytics import csvAnalytics

path = 'C:\\Users\\p.rezaieh\\PycharmProjects\\MainPythonProject\\QueraProblemSet\\QueraStartDate\\EkteshafBimeie\\DataSet\\train.csv'



if __name__ == "__main__":
    csv_Reader = csvAnalytics()
    df = csv_Reader.read_csv_with_pandas(path)

    print(csv_Reader.count_dataframe_row(df))
    print(csv_Reader.count_dataframe_column(df))

    print(df['AnnualIncome'].sum()/csv_Reader.count_dataframe_row(df))

    df_EverTravelledAbroad = df.loc[
        (df['EverTravelledAbroad'] == 'Yes')]
    print(csv_Reader.count_dataframe_row(df_EverTravelledAbroad))

    df_Goverment_Sectore = df.loc[(df['Employment Type'] == 'Government Sector')]
    count_Goverment_sector = csv_Reader.count_dataframe_row(df_Goverment_Sectore)

    df_Private_Sector = df.loc[(df['Employment Type'] == 'Private Sector/Self Employed')]
    count_Private_Sector = csv_Reader.count_dataframe_row(df_Private_Sector)

    if(count_Private_Sector > count_Goverment_sector):
        print('Private Sector/Self Employed ', (count_Private_Sector/1590)*100)
    elif(count_Private_Sector < count_Goverment_sector):
        print('Government Sector ', (count_Goverment_sector/1590)*100)

    df_Q5 = df.loc[((df['TravelInsurance'] == 'Yes') & (df['ChronicDiseases'] == 1))]
    df_Q5_1 = df.loc[(df['ChronicDiseases'] == 1)]

    print(csv_Reader.count_dataframe_row(df_Q5) / csv_Reader.count_dataframe_row(df_Q5_1))