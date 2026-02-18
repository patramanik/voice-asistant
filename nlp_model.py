import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

class NLPModel:
    def __init__(self, intent_file):
        self.vectorizer = TfidfVectorizer()
        self.model = LogisticRegression()
        self.load_and_train(intent_file)

    def load_and_train(self, file):
        data = json.load(open(file))
        X, y = [], []

        for intent in data["intents"]:
            for ex in intent["examples"]:
                X.append(ex.lower())
                y.append(intent["intent"])

        X_vec = self.vectorizer.fit_transform(X)
        self.model.fit(X_vec, y)

    def predict_intent(self, text):
        vec = self.vectorizer.transform([text.lower()])
        return self.model.predict(vec)[0]
