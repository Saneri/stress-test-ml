import joblib

model = joblib.load('pkl/model.pkl')
cv = joblib.load('pkl/cv.pkl')

def analyzeStress(wordList):
    results = model.predict(cv.transform(wordList).toarray())
    resultsAsInt = [int(x) for x in results]
    return resultsAsInt