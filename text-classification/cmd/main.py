from flask import Flask, request, jsonify
from internal.core.classif_text import classify_text
from internal.db.db_connect import get_db_connection
app = Flask(__name__)

classifier = classify_text(repo=get_db_connection)

@app.route("/classify_text", methods=["POST"])
def classify_text():
    data = request.json
    user_input = data["user_input"]
    book_id = data["book_id"]
    
    result = classifier.execute(user_input, book_id)
    return jsonify(result)

if __name__ == "__main__":
    app.run(port=5002, debug=True)