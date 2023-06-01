from flask import Flask, request, render_template
from serpapi import GoogleSearch
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query') or request.get_json().get('query')

    params = {
        "q": query,
        "api_key": "26cae757a5397b62f66b1d841a658677f8775000ea07c00ecfabe651db7e09e0",
    }

    search = GoogleSearch(params)
    results = search.get_dict().get("organic_results")

    if results:
        # Save to JSON file
        with open('results.json', 'w') as json_file:
            json.dump(results, json_file)
        
        json_results = json.dumps(results)
        return "Výsledky vyhledávání: " + json_results
    else:
        return "Nebyly nalezeny žádné výsledky vyhledávání."

if __name__ == '__main__':
    app.run(debug=True)
