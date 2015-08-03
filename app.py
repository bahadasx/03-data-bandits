from flask import Flask, render_template, request, url_for

app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return render_template('form_submit.html')

@app.route('/hello/', methods=['POST'])
def hello():
    food=request.form['food']
    medical=request.form['medical']
    housing=request.form['housing']
    recreation=request.form['recreation']
    apparel=request.form['apparel']
    education=request.form['education']
    transport=request.form['transport']
    other=request.form['other']
    arr = [food,medical,housing,recreation,apparel,education,transport,other]
    mycpivalue=mycpi(arr)
    return render_template('form_submit.html', food=food, medical=medical, housing=housing, recreation=recreation,
    apparel=apparel, education=education, transport=transport, other=other, mycpi=mycpivalue)

def mycpi(values):
    #return sum(int(i) for i in values) / 8
    return sum(float(i) for i in values) / 8
if __name__ == '__main__':
  app.run()

