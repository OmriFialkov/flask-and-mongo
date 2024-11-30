from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection (update with your MongoDB host and credentials if needed)
client = MongoClient("mongodb://172.17.0.3:27017/")  # Replace with your MongoDB connection string
db = client['my_database']  # Replace with your database name
collection = db['my_collection']  # Replace with your collection name

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Greeting route
@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"

# About route
@app.route('/about')
def about():
    return "This is a Flask web application with enhanced styling."

# Add data route (POST method)
@app.route('/add', methods=['POST'])
def add_data():
    data = request.json  # Expecting JSON input
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Insert data into the MongoDB collection
    result = collection.insert_one(data)
    return jsonify({"message": "Data added", "id": str(result.inserted_id)}), 201

# Retrieve all data route (GET method)
@app.route('/data', methods=['GET'])
def get_data():
    # Retrieve all documents from the MongoDB collection
    data = list(collection.find({}, {"_id": 0}))  # Exclude the `_id` field for cleaner output
    return jsonify(data), 200

# Retrieve specific data based on a query (GET method)
@app.route('/find', methods=['GET'])
def find_data():
    query_params = request.args.to_dict()  # Convert query parameters to a dictionary
    if not query_params:
        return jsonify({"error": "No query parameters provided"}), 400

    # Use MongoDB's case-insensitive search if needed
    results = list(collection.find(query_params, {"_id": 0}))
    if not results:
        return jsonify({"message": "No matching documents found"}), 404

    return jsonify(results), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
