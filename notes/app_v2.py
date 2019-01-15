from flask import render_template
from flask import Flask,request
import redis

app = Flask(__name__)

r = redis.Redis(host='redis-service', port=6379, db=0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/action_page',methods=["POST"])
def save_form():
    name = request.form.get('name', "None")
    desc = request.form.get('description', "None")
    r.lpush(name,desc)
    ret = "<html><h1>Data saved</h1><br><br><h2>Name:{}</h2><br><br><h2>Description:{}</h2></html>".format(name,desc)
    ret += '''<form action="/">
            <button>Back</button>
            </form>'''
    return ret

@app.route("/get_notes",methods=["POST","GET"])
def get_notes():
    name = request.form.get('name', "None")
    rr = r.lindex(name,0)
    print(rr)
    ll = r.llen(name)
    if not rr:
        return "<html><h1>There is no ID:{} in the database!</h1></html>".format(name)
    elif ll == 0:
        return "<html><h1>No records for the ID:{} in the database.</h1></html>".format(name)
    else:
        ret = "<html><h1>Your notes</h1><br><h2>ID:{}</h2><br>".format(name)
        for i in range(ll):
            ret += "<h3>Note-{}:</h3>".format(i+1)
            ret += "<h4>{}</h4><br>".format(r.lindex(name,i).decode("utf-8") )
        ret += "</html>"
    ret += '''<form action="/">
            <button>Back</button>
            </form>'''
    return ret

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5050)
