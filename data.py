from settings import *

df=pd.read_csv('datasets/hbo_dataset.csv')
interest1=df.columns
print(interest1, df.tail())