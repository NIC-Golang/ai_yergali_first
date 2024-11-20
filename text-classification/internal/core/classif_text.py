from transformers import pipeline

class ClassifyText:
    def __init__(self, repo, model_name: str = "facebook/bart-large-mnli"):
        self.repo = repo
        self.classifier = pipeline("zero-shot-classification", model=model_name)

    def execute(self, user_input: str):
        tags = self.repo.get_tags()
        
        result = self.classifier(user_input, candidate_labels=tags)
        return result