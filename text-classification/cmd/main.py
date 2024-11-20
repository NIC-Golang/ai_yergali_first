from flask import Flask, request, jsonify
from internal.infrastructure.database.mongo_repository import MongoTagRepository
from internal.core.usecases.classify_text import ClassifyText

app = Flask(__name__)

# Настройки MongoDB
MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "book_tags_db"
COLLECTION_NAME = "tags"
repo = MongoTagRepository(MONGO_URI, DB_NAME, COLLECTION_NAME)

# Логика
classifier = ClassifyText(repo=repo)

@app.route("/classify_text", methods=["POST"])
def classify_text():
    data = request.json
    user_input = data["user_input"]
    book_id = data["book_id"]
    
    result = classifier.execute(user_input, book_id)
    return jsonify(result)

if __name__ == "__main__":
    app.run(port=5002, debug=True)