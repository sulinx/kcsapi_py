from flask import Flask,request,make_response,render_template,abort
from flask_sqlalchemy import SQLAlchemy
from svdata import *
import json
from random import randrange
from time import time
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/kancolle'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Userdata(db.Model):
    uid = db.Column(db.String(32), primary_key=True)
    api_material = db.Column(db.Text)
    api_deck_port = db.Column(db.Text)
    api_ndock = db.Column(db.Text)
    api_ship = db.Column(db.Text, unique=True)
    api_basic = db.Column(db.Text)
    api_log = db.Column(db.Text)
    api_p_bgm_id = db.Column(db.Integer, unique=True)
    api_kdock = db.Column(db.Text)
    shipnum = db.Column(db.Integer, unique=True)
    slot_item = db.Column(db.Text, unique=True)
    slotnum = db.Column(db.Integer, unique=True)

    def __init__(self, username):
        self.uid = username

    def __repr__(self):
        return '<User %r>' % self.uid


class Furniture(db.Model):
    api_id = db.Column(db.Integer, primary_key=True)
    api_type = db.Column(db.Integer, unique=True)
    api_no = db.Column(db.Integer, unique=True)
    api_title  = db.Column(db.Text)
    api_description = db.Column(db.Text)
    api_rarity = db.Column(db.Integer, unique=True)
    api_price = db.Column(db.Integer, unique=True)
    api_saleflg = db.Column(db.Integer, unique=True)
    api_season = db.Column(db.Integer, unique=True)

    def __init__(self, api_id):
        self.api_id = api_id

    def __repr__(self):
        return '<User %r>' % self.api_title

class Slotitem(db.Model):
    api_id = db.Column(db.Integer, primary_key=True)
    api_sortno = db.Column(db.Integer, unique=True)
    api_name = db.Column(db.Integer, unique=True)
    api_type = db.Column(db.Integer, unique=True)
    api_taik = db.Column(db.Integer, unique=True)
    api_souk = db.Column(db.Integer, unique=True)
    api_houg = db.Column(db.Integer, unique=True)
    api_raig = db.Column(db.Integer, unique=True)
    api_soku = db.Column(db.Integer, unique=True)
    api_baku = db.Column(db.Integer, unique=True)
    api_tyku = db.Column(db.Integer, unique=True)
    api_tais = db.Column(db.Integer, unique=True)
    api_atap = db.Column(db.Integer, unique=True)
    api_houm = db.Column(db.Integer, unique=True)
    api_raim = db.Column(db.Integer, unique=True)
    api_houk = db.Column(db.Integer, unique=True)
    api_raik = db.Column(db.Integer, unique=True)
    api_bakk = db.Column(db.Integer, unique=True)
    api_saku = db.Column(db.Integer, unique=True)
    api_sakb = db.Column(db.Integer, unique=True)
    api_luck = db.Column(db.Integer, unique=True)
    api_leng = db.Column(db.Integer, unique=True)
    api_rare = db.Column(db.Integer, unique=True)
    api_broken = db.Column(db.Text)
    api_info = db.Column(db.Text)
    api_usebull = db.Column(db.Integer, unique=True)


    def __init__(self, api_id):
        self.api_id = api_id

    def __repr__(self):
        return '<User %r>' % self.api_name


class Shipdata(db.Model):
    api_id = db.Column(db.Integer, primary_key=True)
    api_sortno = db.Column(db.Integer, unique=True)
    api_name = db.Column(db.Text)
    api_yomi = db.Column(db.Text)
    api_stype = db.Column(db.Integer, unique=True)
    api_afterlv = db.Column(db.Integer, unique=True)
    api_aftershipid = db.Column(db.Integer, unique=True)
    api_taik = db.Column(db.Text)
    api_souk = db.Column(db.Text)
    api_houg = db.Column(db.Text)
    api_raig = db.Column(db.Text)
    api_tyku = db.Column(db.Text)
    api_luck = db.Column(db.Text)
    api_soku = db.Column(db.Integer, unique=True)
    api_leng = db.Column(db.Integer, unique=True)
    api_slot_num = db.Column(db.Integer, unique=True)
    api_maxeq = db.Column(db.Text)
    api_buildtime = db.Column(db.Integer, unique=True)
    api_broken = db.Column(db.Text)
    api_powup = db.Column(db.Text)
    api_backs = db.Column(db.Integer, unique=True)
    api_getmes = db.Column(db.Text)
    api_afterfuel = db.Column(db.Integer, unique=True)
    api_afterbull = db.Column(db.Integer, unique=True)
    api_fuel_max = db.Column(db.Integer, unique=True)
    api_bull_max = db.Column(db.Integer, unique=True)
    api_voicef = db.Column(db.Integer, unique=True)

    def __init__(self, api_id):
        self.api_id = api_id

    def __repr__(self):
        return '<User %r>' % self.api_name


def get_slotitem(user,fuel=10, bullet=10, steel=10, alum=10):
    api_id = user.slotnum + 1
    new_slotitem = json.loads(
        '{"api_create_flag":1,"api_shizai_flag":1,"api_slot_item":{"api_id":43,"api_slotitem_id":44},"api_material":[99999,99999,99999,99999,999,999,999,999],"api_type3":15,"api_unsetslot":[10,43]}')
    new_slotitem['api_slot_item']['api_id'] = api_id
    slot_id = randrange(1, 138)
    api_type3 = json.loads(Slotitem.query.filter_by(api_id=slot_id).first().api_type)[2]
    new_slotitem['api_slot_item']['api_slotitem_id'] = slot_id
    new_slotitem['api_type3'] = api_type3
    data = json.loads('{"api_id":10,"api_slotitem_id":56,"api_locked":0,"api_level":0,"api_equipped":0}')
    data['api_id'] = api_id
    data['api_slotitem_id'] = slot_id
    slot_item = json.loads(user.slot_item)
    slot_item.append(data)
    user.slot_item = json.dumps(slot_item)
    db.session.commit()
    return json.dumps(new_slotitem)


def furniture_change(user, fur_list=["35", "71", "118", "101", "160", "189"]):
    if '' not in fur_list:
        fur_list = [request.form['api_floor'], request.form['api_wallpaper'], request.form['api_wallhanging'],
                request.form['api_window'], request.form['api_shelf'], request.form['api_desk']]
    else:
        fur_list = ["35", "71", "118", "101", "160", "189"]
    api_basic = json.loads(user.api_basic)
    api_basic['api_furniture'] = fur_list
    user.api_basic = json.dumps(api_basic)
    db.session.commit()
    return 'svdata={"api_result":1,"api_result_msg":"\u6210\u529f"}'


def creatship(user, fuel=30, bullet=30, steel=30, alum=30, large_flag=0, zicai=1, quick_flag=0, kdock_id=1):
    shipnum = int(user.slotnum) + 1
    if large_flag == '1':
        if zicai == '1':
            pool = Shipdata.query.filter(Shipdata.api_backs > 4, Shipdata.api_backs < 8,
                                         Shipdata.api_afterlv != 0).all()
            rand = pool[randrange(len(pool))]
        elif zicai == '20':
            pool = Shipdata.query.filter(Shipdata.api_backs > 5, Shipdata.api_backs < 8,
                                         Shipdata.api_afterlv != 0).all()
            rand = pool[randrange(len(pool))]
        elif zicai == '100':
            pool = Shipdata.query.filter(Shipdata.api_backs > 6, Shipdata.api_backs < 8,
                                         Shipdata.api_afterlv != 0).all()
            rand = pool[randrange(len(pool))]
    elif large_flag == '0':
        pool = Shipdata.query.filter(Shipdata.api_backs > 0, Shipdata.api_backs < 6,
                                     Shipdata.api_afterlv != 0).all()
        rand = pool[randrange(len(pool))]

    # 建造渠
    #print(rand.api_name)
    buildtime = rand.api_buildtime
    comptime = datetime.now().timestamp() + buildtime * 60
    date = datetime.fromtimestamp(comptime).strftime('%Y-%m-%d %H:%M:%S')
    kdock = json.loads(user.api_kdock)
    kdock[int(kdock_id) - 1]['api_created_ship_id'] = rand.api_id
    kdock[int(kdock_id) - 1]['api_state'] = 2
    kdock[int(kdock_id) - 1]['api_complete_time'] = int(comptime) * 1000
    kdock[int(kdock_id) - 1]['api_complete_time_str'] = date
    kdock[int(kdock_id) - 1]['api_item1'] = fuel
    kdock[int(kdock_id) - 1]['api_item2'] = bullet
    kdock[int(kdock_id) - 1]['api_item3'] = steel
    kdock[int(kdock_id) - 1]['api_item4'] = alum
    kdock[int(kdock_id) - 1]['api_item5'] = zicai
    user.api_kdock = json.dumps(kdock)
    db.session.commit()
    return 'svdata={"api_result":1,"api_result_msg":"\u6210\u529f"}'

@app.route('/api_start2',methods=['GET', 'POST'])
def start():
    if request.form['api_token']:
        resp = make_response(svdata, 200)
        resp.headers['Content-Type'] = 'text/html'
        return resp
    else:
        abort(404)


@app.route('/api_get_member/<funcm>',methods=['GET', 'POST'])
def api_get_member(funcm):
    if request.form['api_token']:
        uid = request.form['api_token']
        user = Userdata.query.filter_by(uid=uid).first()
        # 提督信息
        if funcm=='basic':
            req = dict(api_result=1,api_result_msg='成功',api_data=json.loads(user.api_basic))
            jso ='svdata=' + json.dumps(req)
            resp = make_response(jso, 200)
            resp.headers['Content-Type'] = 'text/html'
            return resp
        #家具
        if funcm == 'furniture':
            furnitures = Furniture.query.all()
            api_data = []
            for fur in furnitures:
                 api_data.append(dict(api_member_id=19053956,api_id=int(fur.api_id),api_furniture_type = int(fur.api_type),api_furniture_no = int(fur.api_no),api_furniture_id = int(fur.api_id)))
            req = dict(api_result=1, api_result_msg='成功',api_data=api_data)
            jso = 'svdata=' + json.dumps(req)
            resp = make_response(jso, 200)
            resp.headers['Content-Type'] = 'text/html'
            return resp
        #建造渠
        if funcm == 'kdock':
            req = dict(api_result=1, api_result_msg='成功', api_data=json.loads(user.api_kdock))
            jso = 'svdata=' + json.dumps(req)
            resp = make_response(jso, 200)
            resp.headers['Content-Type'] = 'text/html'
            return resp
        #资源
        if funcm == 'material':
            req = dict(api_result=1, api_result_msg='成功', api_data=json.loads(user.api_material))
            jso = 'svdata=' + json.dumps(req)
            resp = make_response(jso, 200)
            resp.headers['Content-Type'] = 'text/html'
            return resp
        #战绩
        if funcm == 'record':
            res = 'svdata={"api_result":1,"api_result_msg":"\u6210\u529f","api_data":{"api_member_id":19053956,"api_nickname":"DMM噎屎了","api_nickname_id":"132175244","api_cmt":"","api_cmt_id":"","api_photo_url":"","api_level":97,"api_rank":1,"api_experience":[842798,851500],"api_war":{"api_win":"55710","api_lose":"10","api_rate":"0.99"},"api_mission":{"api_count":"2464","api_success":"2451","api_rate":"99.47"},"api_practice":{"api_win":"4500","api_lose":"10","api_rate":"99.99"},"api_friend":0,"api_deck":4,"api_kdoc":4,"api_ndoc":4,"api_ship":[130,230],"api_slotitem":[504,2048],"api_furniture":500,"api_complate":["0.0","0.0"],"api_large_dock":1,"api_material_max":100000}}'
            return res
        #舰娘改造
        if funcm == 'ship3':
            pass
        #装备
        if funcm == 'slot_item':
            req = dict(api_result=1, api_result_msg='成功', api_data=json.loads(user.slot_item))
            jso = 'svdata=' + json.dumps(req)
            resp = make_response(jso, 200)
            resp.headers['Content-Type'] = 'text/html'
            return resp
        #库存装备
        if funcm == 'unsetslot':
            pass
        #氪金物
        if funcm == 'useitem':
            res = 'svdata={"api_result":1,"api_result_msg":"\u6210\u529f","api_data":[{"api_member_id":19053956,"api_id":10,"api_value":9,"api_usetype":4,"api_category":6,"api_name":"\u5bb6\u5177\u7bb1\uff08\u5c0f\uff09","api_description":["",""],"api_price":0,"api_count":9},{"api_member_id":19053956,"api_id":11,"api_value":3,"api_usetype":4,"api_category":6,"api_name":"\u5bb6\u5177\u7bb1\uff08\u4e2d\uff09","api_description":["",""],"api_price":0,"api_count":3},{"api_member_id":19053956,"api_id":12,"api_value":1,"api_usetype":4,"api_category":6,"api_name":"\u5bb6\u5177\u7bb1\uff08\u5927\uff09","api_description":["",""],"api_price":0,"api_count":1},{"api_member_id":19053956,"api_id":54,"api_value":4,"api_usetype":0,"api_category":0,"api_name":"\u7d66\u7ce7\u8266\u300c\u9593\u5bae\u300d","api_description":["",""],"api_price":0,"api_count":4},{"api_member_id":19053956,"api_id":57,"api_value":2,"api_usetype":4,"api_category":0,"api_name":"\u52f2\u7ae0","api_description":["",""],"api_price":0,"api_count":2},{"api_member_id":19053956,"api_id":50,"api_value":10,"api_usetype":0,"api_category":0,"api_name":"\u5fdc\u6025\u4fee\u7406\u8981\u54e1","api_description":["",""],"api_price":0,"api_count":10}]}'
            return res
    else:
        abort(404)
#api_port
@app.route('/api_port/port',methods=['GET', 'POST'])
def api_port():
    if request.form['api_token']:
        uid = request.form['api_token']
        user = Userdata.query.filter_by(uid=uid).first()
        data = dice(api_material=json.loads(user.api_material),api_deck_port=json.loads(user.api_deck_port),api_ndock=json.loads(user.api_ndock),api_ship=json.loads(user.api_ship),api_basic=json.loads(user.api_basic),api_log=json.loads(user.api_log),api_p_bgm_id=json.loads(user.api_p_bgm_id))
        req = dict(api_result=1, api_result_msg='成功', api_data=data)
        jso = 'svdata=' + json.dumps(req)
        resp = make_response(jso, 200)
        resp.headers['Content-Type'] = 'text/html'
        return resp
@app.route('/api_req_furniture/change',methods=[ 'POST'])
def api_req_furniture():
    if request.form['api_token']:
        uid = request.form['api_token']
        user = Userdata.query.filter_by(uid=uid).first()
        return furniture_change(user,[request.form['api_floor'],request.form['api_wallpaper'],request.form['api_wallhanging'],request.form['api_window'],request.form['api_shelf'],request.form['api_desk']])
        
@app.route('/api_req_hensei/change',methods=[ 'POST'])
def api_req_hensei():
    pass
@app.route('/api_req_kaisou/slotset',methods=[ 'POST'])
def api_req_kaisou():
    pass
@app.route('/api_req_kousyou/<funck>',methods=[ 'POST'])
def api_req_kousyou(funck):
    if request.form['api_token']:
        uid = request.form['api_token']
        user = Userdata.query.filter_by(uid=uid).first()
        #装备开发
        if funck == 'createitem':
            fuel = request.form['api_item1']
            bullet = request.form['api_item2']
            steel = request.form['api_item3']
            alum = request.form['api_item4']
            return 'svdata=' + get_slotitem(user,fuel,bullet,steel,alum)
        #建造
        if funck == 'createship':
            fuel = request.form['api_item1']
            bullet = request.form['api_item2']
            steel = request.form['api_item3']
            alum = request.form['api_item4']
            zicai = request.form['api_item5']
            large_flag = request.form['api_large_flag']
            quick_flag = request.form['api_highspeed']
            kdock_id = request.form['api_kdock_id']
        return creatship(user,fuel,bullet,steel,alum,large_flag,quick_flag,kdock_id)
        #建造加速
        if funck == 'createship_speedchange':
            pass

        if funck == 'destroyitem2':
            pass
        if funck == 'destroyship':
            pass
        if funck == 'getnum':
            pass
        #获得舰娘
        if funck == 'getship':
            def getship():
                new_ship = json.loads(
                    '{"api_id":2853,"api_sortno":73,"api_ship_id":36,"api_lv":1,"api_exp":[0,100,0],"api_nowhp":15,"api_maxhp":15,"api_leng":1,"api_slot":[-1,-1,-1,-1,-1],"api_onslot":[0,0,0,0,0],"api_kyouka":[0,0,0,0,0],"api_backs":1,"api_fuel":15,"api_bull":20,"api_slotnum":2,"api_ndock_time":0,"api_ndock_item":[0,0],"api_srate":0,"api_cond":40,"api_karyoku":[12,29],"api_raisou":[27,69],"api_taiku":[14,39],"api_soukou":[6,19],"api_kaihi":[42,79],"api_taisen":[20,49],"api_sakuteki":[5,19],"api_lucky":[10,49],"api_locked":0,"api_locked_equip":0}')
                new_ship['api_id'] = shipnum
                new_ship['api_ship_id'] = rand.api_id
                new_ship['api_sortno'] = rand.api_sortno


@app.route('/api_req_member/<funm1>',methods=[ 'POST'])
def api_req_member(funcm1):
    if request.form['api_token']:
        uid = request.form['api_token']
        user = Userdata.query.filter_by(uid=uid).first()
        if funcm1 == 'get_incentive':
            return 'svdata={"api_result":1,"api_result_msg":"\u6210\u529f","api_data":{"api_count":0}}'
        # 任务列表
        if funcm1 == 'questlist':
            pass
        #舰队更名
        if funcm1 == 'updatedeckname':
            # 页数
            api_deck_id = request.form['api_deck_id'] -1
            api_name = request.form['api_name']
            api_deck_port = json.loads(user.api_deck_port)
            api_deck_port[api_deck_id]['api_name'] = api_name
            api_deck_port[api_deck_id]['api_name_id'] = 157269026
            user.api_deck_port = json.dumps(api_deck_port)
            db.session.commit()
            return 'svdata={"api_result":1,"api_result_msg":"\u6210\u529f"}'

#秃子榜
@app.route('/api_req_ranking/getlist',methods=[ 'POST'])
def api_req_ranking():
    svdata = 'svdata={"api_result":1,"api_result_msg":"\u6210\u529f","api_data":{"api_count":10,"api_page_count":1,"api_disp_page":1,"api_list":[{"api_no":1,"api_member_id":19053956,"api_level":97,"api_rank":1,"api_nickname":"DMM噎屎了","api_experience":813259,"api_comment":"","api_rate":227,"api_flag":0,"api_medals":1,"api_nickname_id":"132175244","api_comment_id":"TEST"}]}}'
    return svdata

if __name__ == '__main__':
    app.run()




