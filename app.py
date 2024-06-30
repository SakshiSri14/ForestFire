from flask import Flask,render_template
# It creates an instance of the flask class which
# will be wsgi

app=Flask(__name__)

# basic route/homepage

@app.route("/")
def welcome():
    return "<html><H1>Welcome to this page.</H1><html>"

@app.route("/index")
def index():
    return render_template('index.html')
# redirecting to index html page instead of writing it here itself
if __name__=="__main__":
    app.run(debug = True)
    # debug true will help us not restart the server everytime
    # and just save the document
    
    
    