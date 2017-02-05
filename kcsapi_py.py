from flask import Flask,request,make_response,render_template,abort
from flask_sqlalchemy import SQLAlchemy
from svdata import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/kancolle'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Userdata(db.Model):
    uid = db.Column(db.String(32), primary_key=True)
    api_material = db.Column(db.Text, unique=True)
    api_deck_port = db.Column(db.Text, unique=True)
    api_ndock = db.Column(db.Text, unique=True)
    api_ship = db.Column(db.Text, unique=True)
    api_basic = db.Column(db.Text, unique=True)
    api_log = db.Column(db.Text, unique=True)
    api_p_bgm_id = db.Column(db.Integer, unique=True)
    api_kdock = db.Column(db.Text, unique=True)
    shipnum = db.Column(db.Integer, unique=True)
    slot_item = db.Column(db.Text, unique=True)
    slotnum = db.Column(db.Integer, unique=True)

    def __init__(self, username, email):
        self.uid = username

    def __repr__(self):
        return '<User %r>' % self.uid

@app.route('/api_start2',methods=['GET', 'POST'])
def start():
    if request.form['api_token']:
        resp = make_response(svdata, 200)
        resp.headers['Content-Type'] = 'application/json;charset=utf-8'
        return resp
    else:
        abort(404)


@app.route('/api_get_member/<funcm>',methods=['GET', 'POST'])
def api_get_member(funcm):
    if request.form['api_token']:
        resp = make_response(svdata, 200)
        resp.headers['Content-Type'] = 'application/json;charset=utf-8'
        return resp
    else:
        abort(404)
@app.route('/api_port/port',methods=['GET', 'POST'])
def api_port():
    a= Userdata.query.all()
    lis = ''
    for user in a:
        lis = lis + '<div>' + user.uid + '</div>'
    return lis
@app.route('/api_req_furniture/<funcf>',methods=[ 'POST'])
def api_req_furniture(funcf):
    pass
@app.route('/api_req_hensei/change',methods=[ 'POST'])
def api_req_hensei():
    pass
@app.route('/api_req_kaisou/slotset',methods=[ 'POST'])
def api_req_kaisou():
    pass
@app.route('/api_req_kousyou/<funck>',methods=[ 'POST'])
def api_req_kousyou(funck):
    pass
@app.route('/api_req_member/<funm1>',methods=[ 'POST'])
def api_req_member(funcm1):
    pass
@app.route('/api_req_ranking/getlist',methods=[ 'POST'])
def api_req_ranking():
    pass

if __name__ == '__main__':
    app.run()
