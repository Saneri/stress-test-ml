import joblib

model = joblib.load('model.pkl')
cv = joblib.load('cv.pkl')

data = cv.transform(["I am sad"]).toarray()



def predict(input_string):
    return model.predict(cv.transform([input_string]).toarray())[0]

print(predict("I hate the new PM so much nhghghghg"))