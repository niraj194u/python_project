import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

# Load and process the data
data_url = "D:/BigData/src/GDP.csv"
gapminder = pd.read_csv(data_url)

# Define columns and rename accordingly
dfcolumns = [
    'continent', 'country', 'gdpPercap_1952', 'gdpPercap_1957',
    'gdpPercap_1962', 'gdpPercap_1967', 'gdpPercap_1972', 'gdpPercap_1977',
    'gdpPercap_1982', 'gdpPercap_1987', 'gdpPercap_1992', 'gdpPercap_1997',
    'gdpPercap_2002', 'gdpPercap_2007', 'lifeExp_1952', 'lifeExp_1957',
    'lifeExp_1962', 'lifeExp_1967', 'lifeExp_1972', 'lifeExp_1977',
    'lifeExp_1982', 'lifeExp_1987', 'lifeExp_1992', 'lifeExp_1997',
    'lifeExp_2002', 'lifeExp_2007', 'pop_1952', 'pop_1957', 'pop_1962',
    'pop_1967', 'pop_1972', 'pop_1977'
]
gapminder.columns = dfcolumns

# Extract and tidy the GDP data
gdpPercap = gapminder.loc[:, gapminder.columns.str.contains('^gdp|^c')]
gdpPercap_tidy = gdpPercap.melt(id_vars=['continent', 'country'], var_name='year', value_name='gdpPercap')

# Function to clean year values
def keep_year(text):
    return ''.join([char for char in text if char.isdigit()])

gdpPercap_tidy['year'] = gdpPercap_tidy['year'].apply(keep_year)

# Extract and tidy the life expectancy data
lifeExp = gapminder.loc[:, gapminder.columns.str.contains('^life|^c')]
lifeExp_tidy = lifeExp.melt(id_vars=['continent', 'country'], var_name='year', value_name='lifeExp')
lifeExp_tidy['year'] = lifeExp_tidy['year'].apply(keep_year)
lifeExp_tidy['year'] = pd.to_numeric(lifeExp_tidy['year'])

# Extract and tidy the population data
pop = gapminder.loc[:, gapminder.columns.str.contains('^pop|^c')]
pop_tidy = pop.melt(id_vars=['continent', 'country'], var_name='year', value_name='pop')
pop_tidy['year'] = pop_tidy['year'].apply(keep_year)
pop_tidy['year'] = pd.to_numeric(pop_tidy['year'])

# Combine the tidy dataframes
gapminder_final = pd.concat([gdpPercap_tidy, lifeExp_tidy, pop_tidy], sort=True, axis=1)
gapminder_final = gapminder_final.T.drop_duplicates().T  # Remove duplicate columns

# API endpoint to return the processed data
@app.route('/api/gapminder', methods=['GET'])
def get_gapminder_data():
    result = gapminder_final.to_dict(orient='records')
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
