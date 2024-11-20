from flask import Flask, request, jsonify
from internal.infrastructure.database.mongo_repository import MongoTagRepository
from internal.core.usecases.generate_tags import GenerateTags

app = Flask(__name__)

# Настройки MongoDB
MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "book_tags_db"
COLLECTION_NAME = "tags"
repo = MongoTagRepository(MONGO_URI, DB_NAME, COLLECTION_NAME)

# Логика
generator = GenerateTags(repo=repo)

@app.route("/generate_tags", methods=["POST"])
def generate_tags():
    data = request.json
    book_id = data["book_id"]
    review_text = data["review_text"]
    num_tags = data.get("num_tags", 5)
    
    tags = generator.execute(book_id, review_text, num_tags)
    return jsonify({"book_id": book_id, "tags": tags})

if __name__ == "__main__":
    app.run(port=5001, debug=True)