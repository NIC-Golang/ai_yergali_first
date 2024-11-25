from transformers import pipeline
from internal.db.db_connect import get_db_connection

classifier = pipeline("zero-shot-classification")

def classify_text(text):
    # Получаем все теги из базы данных
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT tag_name FROM tags")
    tags = [row[0] for row in cursor.fetchall()]
    cursor.close()
    connection.close()

    # Классифицируем текст по тегам
    result = classifier(text, candidate_labels=tags)
    print(result)
    return result