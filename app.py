# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, request, url_for

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return render_template('form_submit.html')

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is 
# accepting: POST requests in this case
@app.route('/hello/', methods=['POST'])
def hello():
    #name=request.form['yourname']
    #email=request.form['youremail']
    #food=request.form['food']
    #medical=request.form['medical']
    #housing=request.form['housing']
    #recreation=request.form['recreation']
    #apparel=request.form['apparel']
    #education=request.form['education']
    #transport=request.form['transport']
    #other=request.form['other']
    #a=array(food,medical,housing,recreation,apparel,transport,other)
    #cpi=mycpi(a)
    #print cpi
    print "1"
    
def mycpi(arr):
    for element in arr:
      cat+=element
      
    cpi=cat/8
    return cpi

# Run the app :)
if __name__ == '__main__':
  app.run()
