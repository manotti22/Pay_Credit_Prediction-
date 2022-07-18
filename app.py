from flask import Flask 

app=Flask(__name__)

@app.route("/",methods=['GET','post'])
def index():
    return 'CD CI PIPLINE IS STARTED'

if __name__=='__main__':
    app.run(debug=True)

