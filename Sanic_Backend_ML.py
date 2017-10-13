from sanic import Sanic
from sanic.response import html,text
import pickle,re

app = Sanic()
@app.route("/")
async def test(request):
    temp = open('templates/ml.html').read()
    return html(temp)

@app.route('/submit',methods=['POST'])
async def post_handler(request):
    s = request.body
    s = s.decode('utf-8')
    a = re.findall('([A-Za-z]+)',s)
    z  = " ".join(a)
    pkl = open('mlmodel.pickle', 'rb')
    clf = pickle.load(pkl)   
    vec = open('vectorizer.pickle', 'rb')
    tf_vect = pickle.load(vec)   
    X_test_tf = tf_vect.transform([z])
    y_predict = clf.predict(X_test_tf)
    if y_predict == 'truth':
        #msg = 'The review is a true one!'
        #t1 = open('templates/message.html').read()
        #return html(t1,msg=msg)
        return html('The review is a true one!')
    if y_predict == 'deceptive':
        # msg = 'The review is a deceptive one!'
        # t2 = open('templates/message.html').read()
        # return html(t2,msg=msg)
        return html('The review is a deceptive one!')


if __name__ == "__main__":
    app.run()
