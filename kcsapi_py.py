from flask import Flask,request,make_response,render_template
from svdata import *

app = Flask(__name__)


@app.route('/api_start2',methods=[ 'POST'])
def start():
    if request.form[api_token]:
        resp = make_response(svdata, 200)
        resp.headers['Content-Type'] = 'application/json;charset=utf-8'
        return resp
    else:
        abort(401)


@app.route('/api_get_member/<funcm>',methods=[ 'POST'])
def api_get_member(funcm):
    pass
@app.route('/api_port/port',methods=[ 'POST'])
def api_port():
    pass
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
