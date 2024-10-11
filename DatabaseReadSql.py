import pandas as pd
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus


username = 'consultants'
password = 'WelcomeItc@2022'
host = '18.132.73.146'
port = '5432'
database = 'testdb'


encoded_password = quote_plus(password)

connection_string = f'postgresql+psycopg2://{username}:{encoded_password}@{host}:{port}/{database}'


engine = create_engine(connection_string)

i = pd.read_csv("D:\BigData\src\GDP.csv")


i.to_sql('gdp', con=engine, if_exists='replace', index=False)


print(i)
