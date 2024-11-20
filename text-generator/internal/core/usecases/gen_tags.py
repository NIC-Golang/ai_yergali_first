from transformers import T5ForConditionalGeneration, T5Tokenizer
from internal.core.interfaces.tag_repository import TagRepositoryInterface

class GenerateTags:
    def __init__(self, model_name: str = 'google/mt5-small', repo: TagRepositoryInterface = None):
        self.model = T5ForConditionalGeneration.from_pretrained(model_name)
        self.tokenizer = T5Tokenizer.from_pretrained(model_name)
        self.repo = repo

    def execute(self, book_id: int, review_text: str):
        input_text = f"generate tags: {review_text}"
        inputs = self.tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True)

        outputs = self.model.generate(
            inputs['input_ids'], max_length=50, num_beams=5, 
            num_return_sequences=5, early_stopping=True
        )
        tags = [self.tokenizer.decode(output, skip_special_tokens=True) for output in outputs]

        self.repo.save_tags(book_id, tags)
        return tags