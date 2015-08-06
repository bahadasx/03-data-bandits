from flask import Flask, render_template, request, url_for
import os

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
    arr = [food,housing,apparel,education,transport,medical,recreation,other]
    floatarr = [float(i) for i in arr]
    mycpivalue=compute_cpi(floatarr)
    return render_template('form_submit.html', food=food, medical=medical, housing=housing, recreation=recreation,
    apparel=apparel, education=education, transport=transport, other=other, mycpi=mycpivalue)

def compute_cpi(values):
    component_indexes = {'food':246.245,\
    'apparel': 124.954,\
    'housing':238.568,\
    'edu': 137.425,\
    'transport': 208.012,\
    'medical_care': 446.271,\
    'recreation': 116.395,\
    'other': 415.022
    }
    wgted_sum = (values[0] * component_indexes['food']/100 + \
        values[1] * component_indexes['housing']/100 + \
        values[2] * component_indexes['apparel']/100 + \
        values[3] * component_indexes['edu']/100 + \
        values[4] * component_indexes['transport']/100 + \
        values[5] * component_indexes['medical_care']/100 + \
        values[6] * component_indexes['recreation']/100 + \
        values[7] * component_indexes['other']/100)
    inflation = wgted_sum - 1
    inflation *= 100
    return inflation

if __name__ == '__main__':
  port = int(os.environ.get('PORT',5000))
  app.run(host='0.0.0.0', port=port)
