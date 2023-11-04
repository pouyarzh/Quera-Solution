import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB


#Reading CSV files
df=pd.read_csv('C:\\Users\\p.rezaieh\\PycharmProjects\\MainPythonProject\\QueraProblemSet\\QueraStartDate\\EkteshafBimeie\\DataSet\\train.csv')

#Encoding the strings to Numericals
Numerics=LabelEncoder()

inputs=df.drop(['TravelInsurance','Customer Id'],axis='columns')
target=df['TravelInsurance']

print(target)

#Creating the new dataframe
inputs['Age_n']=Numerics.fit_transform(inputs['Age'])
inputs['Employment Type_n']=Numerics.fit_transform(inputs['Employment Type'])
inputs['GraduateOrNot_n']=Numerics.fit_transform(inputs['GraduateOrNot'])
inputs['AnnualIncome_n']=Numerics.fit_transform(inputs['AnnualIncome'])
inputs['FamilyMembers_n']=Numerics.fit_transform(inputs['FamilyMembers'])
inputs['ChronicDiseases_n']=Numerics.fit_transform(inputs['ChronicDiseases'])
inputs['FrequentFlyer_n']=Numerics.fit_transform(inputs['FrequentFlyer'])
inputs['EverTravelledAbroad_n']=Numerics.fit_transform(inputs['EverTravelledAbroad'])

print(inputs)

inputs_n=inputs.drop(['Age','Employment Type','GraduateOrNot','AnnualIncome','FamilyMembers','ChronicDiseases','FrequentFlyer','EverTravelledAbroad'],axis='columns')

Classifier=GaussianNB()
Classifier.fit(inputs_n,target)

GaussianNB()

Classifier.score(inputs_n,target)

print(Classifier.predict([[0,0,0,1]]))






