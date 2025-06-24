from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

def train_nb(X_train, y_train):
    model = MultinomialNB()
    model.fit(X_train, y_train)
    return model

def train_logreg(X_train, y_train):
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    return model

def train_svm(X_train, y_train):
    model = SVC(probability=True)
    model.fit(X_train, y_train)
    return model

