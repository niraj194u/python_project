from flask import Flask, jsonify, request
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd
from urllib.parse import quote_plus

# Database credentials
username = 'consultants'
password = 'WelcomeItc@2022'
host = '18.132.73.146'
port = '5432'
database = 'testdb'

# Encode password for URL
encoded_password = quote_plus(password)
connection_string = f'postgresql+psycopg2://{username}:{encoded_password}@{host}:{port}/{database}'

# Initialize Flask app and SQLAlchemy engine
app = Flask(__name__)
engine = create_engine(connection_string)

# Define a route to upload CSV data to the 'gdp' table
@app.route('/upload', methods=['POST'])
def upload_csv():
    try:
        # Load CSV data
        csv_data = pd.read_csv("D:/BigData/src/GDP.csv")
        
        # Insert data into the 'gdp' table
        csv_data.to_sql('gdp', con=engine, if_exists='replace', index=False)
        
        return jsonify({"message": "Data uploaded successfully"}), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

# Define a route to fetch all data from the 'gdp' table
@app.route('/gdp', methods=['GET'])
def get_all_data():
    try:
        query = "SELECT * FROM gdp"
        data = pd.read_sql(query, con=engine)
        return jsonify(data.to_dict(orient="records")), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

# Define a route to get data by ID
@app.route('/gdp/data', methods=['GET'])
def get_data_by_id():
    try:
        query = f"SELECT * FROM gdp "
        data = pd.read_sql(query, con=engine)
        
        if data.empty:
            return jsonify({"error": "Data not found"}), 404

        return jsonify(data.to_dict(orient="records")), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

# Define a route to update data by ID
@app.route('/gdp/data1', methods=['PUT'])
def update_data():
    try:
        data = request.get_json()
        set_clause = ", ".join([f"{key} = '{value}'" for key, value in data.items()])
        query = text(f"UPDATE gdp SET {set_clause} ")
        
        with engine.connect() as conn:
            result = conn.execute(query, )
        
        if result.rowcount == 0:
            return jsonify({"error": "Data not found"}), 404

        return jsonify({"message": "Data updated successfully"}), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

# Define a route to delete data by ID
@app.route('/gdp/<int:id>', methods=['DELETE'])
def delete_data(id):
    try:
        query = text("DELETE FROM gdp WHERE id = :id")
        
        with engine.connect() as conn:
            result = conn.execute(query, {"id": id})
        
        if result.rowcount == 0:
            return jsonify({"error": "Data not found"}), 404

        return jsonify({"message": "Data deleted successfully"}), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
