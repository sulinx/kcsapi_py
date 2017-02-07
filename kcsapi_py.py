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
    fuel, bullet, steel, alum = map(int,[fuel, bullet, steel, alum])
    api_id = user.slotnum + 1
    user.slotnum = user.slotnum + 1
    new_slotitem = json.loads(
        '{"api_create_flag":1,"api_shizai_flag":1,"api_slot_item":{"api_id":43,"api_slotitem_id":44},"api_material":[10000,10000,10000,10000,10,10,10,10],"api_type3":15,"api_unsetslot":[10,43]}')
    slot_id = randrange(1, 138)
    api_type3 = json.loads(Slotitem.query.filter_by(api_id=slot_id).first().api_type)[2]
    new_slotitem['api_slot_item']['api_id'] = api_id
    new_slotitem['api_slot_item']['api_slotitem_id'] = int(slot_id)
    new_slotitem['api_type3'] = int(api_type3)
    new_slotitem['api_unsetslot'] = [api_id]
    data = json.loads('{"api_id":10,"api_slotitem_id":56,"api_locked":0,"api_level":0,"api_equipped":0}')
    data['api_id'] = api_id
    data['api_slotitem_id'] = int(slot_id)
    slot_item = json.loads(user.slot_item)
    slot_item.append(data)
    user.slot_item = json.dumps(slot_item)
    db.session.commit()
    return json.dumps(new_slotitem)


def furniture_change(user, fur_list=[1,38,72,102,133,164]):
    if '' in fur_list:
        fur_list = [1,38,72,102,133,164]
    fur_list = list(map(int,fur_list))
    api_basic = json.loads(user.api_basic)
    api_basic['api_furniture'] = fur_list
    user.api_basic = json.dumps(api_basic)
    db.session.commit()
    return r'svdata={"api_result":1,"api_result_msg":"\u6210\u529f"}'


def creatship(user, fuel=30, bullet=30, steel=30, alum=30,  zicai=1, large_flag=0, quick_flag=0, kdock_id=1):
    fuel, bullet, steel,alum ,zicai,large_flag,quick_flag,kdock_id = map(int, [fuel, bullet, steel,alum,zicai,large_flag,quick_flag,kdock_id])
    if large_flag == 1:
        if zicai == 1:
            pool = Shipdata.query.filter(Shipdata.api_backs > 4, Shipdata.api_backs < 8,
                                         Shipdata.api_afterlv != 0).all()
            rand = pool[randrange(len(pool))]
        elif zicai == 20:
            pool = Shipdata.query.filter(Shipdata.api_backs > 5, Shipdata.api_backs < 8,
                                         Shipdata.api_afterlv != 0).all()
            rand = pool[randrange(len(pool))]
        elif zicai == 100:
            pool = Shipdata.query.filter(Shipdata.api_backs > 6, Shipdata.api_backs < 8,
                                         Shipdata.api_afterlv != 0).all()
            rand = pool[randrange(len(pool))]
    elif large_flag == 0:
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
    if quick_flag == 1:
        quick_creat(user,kdock_id)
    return r'svdata={"api_result":1,"api_result_msg":"\u6210\u529f"}'


def quick_creat(user, kdock_id):
    kdock = json.loads(user.api_kdock)
    kdock_id = int(kdock_id) - 1
    kdock[kdock_id]['api_state'] = 3
    kdock[kdock_id]['api_complete_time'] = 0
    kdock[kdock_id]['api_complete_time_str'] = 0
    user.api_kdock = json.dumps(kdock)
    db.session.commit()
    return r'svdata={"api_result":1,"api_result_msg":"\u6210\u529f"}'


def destroyitem(user, slotitem_ids):
    slotitem_ids = slotitem_ids.split(',')
    data = json.loads(user.slot_item)
    lis = []
    res1 = [0, 0, 0, 0]
    for item in data:
        if str(item['api_id']) in slotitem_ids:
            res = json.loads(Slotitem.query.filter_by(api_id=item['api_slotitem_id']).first().api_broken)
            res1[0] = int(res[0]) + res1[0]
            res1[1] = int(res[1]) + res1[1]
            res1[2] = int(res[2]) + res1[2]
            res1[3] = int(res[3]) + res1[3]
            lis.append(item)
    for i in lis:
        data.remove(i)
    user.slotitem = json.dumps(data)
    db.session.commit()
    return r'svdata={"api_result":1,"api_result_msg":"\u6210\u529f","api_data":{"api_get_material":%s}}' % json.dumps(
        res1)


def destroyship(user, api_ship_id):
    data = json.loads(user.api_ship)
    for ship in data:
        if str(ship['api_id']) == api_ship_id:
            res = json.loads(Shipdata.query.filter_by(api_id=ship['api_ship_id']).first().api_broken)
            data.remove(ship)
            break
    user.api_ship = json.dumps(data)
    db.session.commit()
    return r'svdata={"api_result":1,"api_result_msg":"\u6210\u529f","api_data":{"api_material":[99999,99999,99999,99999]}}'


def getkship(user, api_kdock_id):
    shipnum = int(user.slotnum) + 1
    user.slotnum = shipnum
    api_kdock_id = int(api_kdock_id) - 1
    kdock = json.loads(user.api_kdock)
    data = json.loads(user.api_ship)
    new = Shipdata.query.filter_by(api_id=int(kdock[api_kdock_id]['api_created_ship_id'])).first()
    kdock[api_kdock_id]['api_state'] = 0
    kdock[api_kdock_id]['api_complete_time'] = 0
    kdock[api_kdock_id]['api_complete_time_str'] = 0
    kdock[api_kdock_id]['api_created_ship_id'] = 0
    kdock[api_kdock_id]['api_item1'] = 0
    kdock[api_kdock_id]['api_item2'] = 0
    kdock[api_kdock_id]['api_item3'] = 0
    kdock[api_kdock_id]['api_item4'] = 0
    kdock[api_kdock_id]['api_item5'] = 1
    user.api_kdock = json.dumps(kdock)
    new_ship = json.loads(
        '{"api_id":2853,"api_sortno":73,"api_ship_id":36,"api_lv":1,"api_exp":[0,100,0],"api_nowhp":15,"api_maxhp":15,"api_leng":1,"api_slot":[-1,-1,-1,-1,-1],"api_onslot":[0,0,0,0,0],"api_kyouka":[0,0,0,0,0],"api_backs":1,"api_fuel":15,"api_bull":20,"api_slotnum":2,"api_ndock_time":0,"api_ndock_item":[0,0],"api_srate":0,"api_cond":40,"api_karyoku":[12,29],"api_raisou":[27,69],"api_taiku":[14,39],"api_soukou":[6,19],"api_kaihi":[42,79],"api_taisen":[20,49],"api_sakuteki":[5,19],"api_lucky":[10,49],"api_locked":0,"api_locked_equip":0}')
    new_ship['api_id'] = shipnum
    new_ship['api_ship_id'] = int(new.api_id)
    new_ship['api_sortno'] = int(new.api_sortno)
    new_ship['api_nowhp'] = int(json.loads(new.api_taik)[0])
    new_ship['api_maxhp'] = int(json.loads(new.api_taik)[0])
    new_ship['api_leng'] = int(new.api_leng)
    new_ship['api_sonslot'] = json.loads(new.api_maxeq)
    new_ship['api_backs'] = int(new.api_backs)
    new_ship['api_fuel'] = int(new.api_fuel_max)
    new_ship['api_bull'] = int(new.api_fuel_max)
    new_ship['api_slotnum'] = int(new.api_slot_num)
    new_ship['api_karyoku'] = json.loads(new.api_houg)
    new_ship['api_raisou'] = json.loads(new.api_raig)
    new_ship['api_taiku'] = json.loads(new.api_tyku)
    new_ship['api_soukou'] = json.loads(new.api_souk)
    new_ship['api_taisen'] = [40, 99]
    new_ship['api_sakuteki'] = [40, 99]
    new_ship['api_kaihi'] = [50, 99]
    data.append(new_ship)
    user.api_ship = json.dumps(data)
    db.session.commit()
    resp = dict(api_result=1, api_result_msg='成功',
                api_data=dict(api_id=shipnum, api_ship_id=new_ship['api_ship_id'], api_kdock=kdock, api_ship=new_ship,
                              api_slotitem=None))
    resp = 'svdata=' + json.dumps(resp)
    #print(resp)
    return resp


def get_unsetslot(user):
    slotitems = json.loads(user.slot_item)
    unsetslots = json.loads(
        '{"api_slottype1":-1,"api_slottype2":-1,"api_slottype3":-1,"api_slottype4":-1,"api_slottype5":-1,"api_slottype6":-1,"api_slottype7":-1,"api_slottype8":-1,"api_slottype9":-1,"api_slottype10":-1,"api_slottype11":-1,"api_slottype12":-1,"api_slottype13":-1,"api_slottype14":-1,"api_slottype15":-1,"api_slottype16":-1,"api_slottype17":-1,"api_slottype18":-1,"api_slottype19":-1,"api_slottype20":-1,"api_slottype21":-1,"api_slottype22":-1,"api_slottype23":-1,"api_slottype24":-1,"api_slottype25":-1,"api_slottype26":-1,"api_slottype27":-1,"api_slottype28":-1,"api_slottype29":-1,"api_slottype30":-1,"api_slottype31":-1,"api_slottype32":-1,"api_slottype33":-1,"api_slottype34":-1,"api_slottype35":-1,"api_slottype36":-1,"api_slottype37":-1,"api_slottype38":-1,"api_slottype39":-1}')
    for slotitem in slotitems:
        if str(slotitem['api_equipped']) == '0':
            s_type = json.loads(Slotitem.query.filter_by(api_id=slotitem['api_slotitem_id']).first().api_type)[2]
            s_type = 'api_slottype' + str(s_type)
            if str(unsetslots[s_type]) == '-1':
                unsetslots[s_type] = [int(slotitem['api_id'])]
            else:
                unsetslots[s_type].append(int(slotitem['api_id']))

    return unsetslots


def hensei_change(user,api_ship_id,api_id,api_ship_idx): #舰队编成
    api_ship_id, api_id, api_ship_idx = map(int, [api_ship_id, api_id, api_ship_idx])
    api_id = api_id -1
    deck = json.loads(user.api_deck_port)
    to_shipid = deck[api_id]['api_ship'][api_ship_idx]
    idx2 = '1'
    for i in range(len(deck)):
        if api_ship_id in deck[i]['api_ship']:
            idx1 = i
            for j in (range(len(deck[i]['api_ship']))):
                if int(deck[i]['api_ship'][j]) == api_ship_id:
                    idx2 = j
                    break
    if api_ship_id != -1:
        if to_shipid == -1:
            deck[api_id]['api_ship'][api_ship_idx] = api_ship_id
            if idx2 != '1':
                print(idx2)
                deck[idx1]['api_ship'].pop(idx2)
                deck[idx1]['api_ship'].append(-1)
        elif to_shipid != -1:
            deck[idx1]['api_ship'][idx2] = to_shipid
            deck[api_id]['api_ship'][api_ship_idx] = api_ship_id
    elif api_ship_id == -1:
        deck[api_id]['api_ship'].pop(api_ship_idx)
        deck[api_id]['api_ship'].append(-1)
    print(deck)
    user.api_deck_port = json.dumps(deck)
    db.session.commit()
    return r'svdata={"api_result":1,"api_result_msg":"\u6210\u529f"}'


def ship3(user, api_shipid, **kw):
    ships = json.loads(user.api_ship)
    decks = json.loads(user.api_deck_port)
    for i in range(len(ships)):
        if ships[i]['api_id'] == int(api_shipid):
            idx = i
            break
    resp = dict(api_result=1, api_result_msg='成功', api_data=[dict(api_ship_data=[ships[idx]]), dict(api_deck_data=decks), dict(api_slot_data=get_unsetslot(user))])
    resp = json.dumps(resp)
    return resp

#换装备
def kaisou_slotset(user,api_item_id,ship_id,api_slot_idx):
    slotitems = json.loads(user.slot_item)
    ships = json.loads(user.api_ship)
    api_item_id,ship_id ,api_slot_idx=map(int,[api_item_id,ship_id,api_slot_idx])
    for i in range(len(ships)):
        if ships[i]['api_id'] == int(ship_id):
            idx1 = i
            break
    old_slotitem_id = ships[idx1]['api_slot'][int(api_slot_idx)]
    if str(old_slotitem_id) != '-1':  #原装备不为空
        for j in range(len(slotitems)):
            if slotitems[j]['api_id'] == int(old_slotitem_id):
                idx2 = j
                break
        if str(api_item_id) != '-1':
            for k in range(len(slotitems)):
                if slotitems[k]['api_id'] == int(api_item_id):
                    idx3 = k
                    break
            slotitems[idx3]['api_equipped'] = 0
        ships[idx1]['api_slot'][int(api_slot_idx)] = api_item_id
        slotitems[idx2]['api_equipped'] = 0
    elif str(old_slotitem_id) == '-1':  #原装备为空
        for k in range(len(slotitems)):
            if slotitems[k]['api_id'] == int(api_item_id):
                idx4 = k
                break
        ships[idx1]['api_slot'][int(api_slot_idx)] = api_item_id
        slotitems[idx4]['api_equipped'] = 1
    user.slot_item = json.dumps(slotitems)
    user.api_ship = json.dumps(ships)
    #print(ships[i]['api_slot'])
    #print(slotitems)
    db.session.commit()
    return r'svdata={"api_result":1,"api_result_msg":"\u6210\u529f"}'

@app.route('/kcsapi/api_start2',methods=['GET', 'POST'])
def start():
    if request.form['api_token']:
        resp = make_response(svdata, 200)
        resp.headers['Content-Type'] = 'text/html'
        return resp
    else:
        abort(404)


@app.route('/kcsapi/api_get_member/<funcm>',methods=['GET', 'POST'])
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
            res = r'{"api_result":1,"api_result_msg":"\u6210\u529f","api_data":{"api_member_id":19053956,"api_nickname":"DMM噎屎了","api_nickname_id":"132175244","api_cmt":"","api_cmt_id":"","api_photo_url":"","api_level":97,"api_rank":1,"api_experience":[842798,851500],"api_war":{"api_win":"55710","api_lose":"10","api_rate":"0.99"},"api_mission":{"api_count":"2464","api_success":"2451","api_rate":"99.47"},"api_practice":{"api_win":"4500","api_lose":"10","api_rate":"99.99"},"api_friend":0,"api_deck":4,"api_kdoc":4,"api_ndoc":4,"api_ship":[130,230],"api_slotitem":[504,2048],"api_furniture":500,"api_complate":["0.0","0.0"],"api_large_dock":1,"api_material_max":100000}}'
            return res
        #查询
        if funcm == 'ship3':
            shipid = request.form['api_shipid']
            return ship3(user,shipid)
        #装备
        if funcm == 'slot_item':
            req = dict(api_result=1, api_result_msg='成功', api_data=json.loads(user.slot_item))
            jso = 'svdata=' + json.dumps(req)
            resp = make_response(jso, 200)
            resp.headers['Content-Type'] = 'text/html'
            return resp
        #库存装备
        if funcm == 'unsetslot':
            resp = dict(api_result=1, api_result_msg='成功',
                        api_data=get_unsetslot(user))
            resp = json.dumps(resp)
            return 'svdata=' + resp
        #氪金物
        if funcm == 'payitem':
            res = r'svdata = {"api_result": 1, "api_result_msg": "\u6210\u529f", "api_data": null}'
            return res
        if funcm == 'useitem':
            res = r'svdata={"api_result":1,"api_result_msg":"\u6210\u529f","api_data":[{"api_member_id":19053956,"api_id":10,"api_value":9,"api_usetype":4,"api_category":6,"api_name":"\u5bb6\u5177\u7bb1\uff08\u5c0f\uff09","api_description":["",""],"api_price":0,"api_count":9},{"api_member_id":19053956,"api_id":11,"api_value":3,"api_usetype":4,"api_category":6,"api_name":"\u5bb6\u5177\u7bb1\uff08\u4e2d\uff09","api_description":["",""],"api_price":0,"api_count":3},{"api_member_id":19053956,"api_id":12,"api_value":1,"api_usetype":4,"api_category":6,"api_name":"\u5bb6\u5177\u7bb1\uff08\u5927\uff09","api_description":["",""],"api_price":0,"api_count":1},{"api_member_id":19053956,"api_id":54,"api_value":4,"api_usetype":0,"api_category":0,"api_name":"\u7d66\u7ce7\u8266\u300c\u9593\u5bae\u300d","api_description":["",""],"api_price":0,"api_count":4},{"api_member_id":19053956,"api_id":57,"api_value":2,"api_usetype":4,"api_category":0,"api_name":"\u52f2\u7ae0","api_description":["",""],"api_price":0,"api_count":2},{"api_member_id":19053956,"api_id":50,"api_value":10,"api_usetype":0,"api_category":0,"api_name":"\u5fdc\u6025\u4fee\u7406\u8981\u54e1","api_description":["",""],"api_price":0,"api_count":10}]}'
            return res
    else:
        abort(404)
#api_port
@app.route('/kcsapi/api_port/port',methods=['GET', 'POST'])
def api_port():
    if request.form['api_token']:
        uid = request.form['api_token']
        user = Userdata.query.filter_by(uid=uid).first()
        data = dict(api_material=json.loads(user.api_material),api_deck_port=json.loads(user.api_deck_port),api_ndock=json.loads(user.api_ndock),api_ship=json.loads(user.api_ship),api_basic=json.loads(user.api_basic),api_log=json.loads(user.api_log),api_p_bgm_id=user.api_p_bgm_id)
        req = dict(api_result=1, api_result_msg='成功', api_data=data)
        jso = 'svdata=' + json.dumps(req)
        resp = make_response(jso, 200)
        resp.headers['Content-Type'] = 'text/html'
        return resp
@app.route('/kcsapi/api_req_furniture/change',methods=[ 'POST'])
def api_req_furniture():
    if request.form['api_token']:
        uid = request.form['api_token']
        user = Userdata.query.filter_by(uid=uid).first()
        return furniture_change(user,[request.form['api_floor'],request.form['api_wallpaper'],request.form['api_window'],request.form['api_wallhanging'],request.form['api_shelf'],request.form['api_desk']])
        
@app.route('/kcsapi/api_req_hensei/change',methods=[ 'POST'])
def api_req_hensei():
    if request.form['api_token']:
        uid = request.form['api_token']
        user = Userdata.query.filter_by(uid=uid).first()
        api_ship_id = request.form['api_ship_id']
        api_id = request.form['api_id']
        api_ship_idx = request.form['api_ship_idx'] #页数
        return hensei_change(user,api_ship_id,api_id,api_ship_idx)

@app.route('/kcsapi/api_req_kaisou/<slot>',methods=[ 'POST'])
def api_req_kaisou(slot):
    if slot == 'slotset':
        if request.form['api_token']:
            uid = request.form['api_token']
            user = Userdata.query.filter_by(uid=uid).first()
            api_item_id = request.form['api_item_id']
            ship_id = request.form['api_id']
            api_slot_idx = request.form['api_slot_idx']
            return kaisou_slotset(user,api_item_id,ship_id,api_slot_idx)
        if slot == 'unsetslot_all':
            pass



@app.route('/kcsapi/api_req_kousyou/<funck>',methods=[ 'POST'])
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
            return creatship(user,fuel,bullet,steel,alum,zicai,large_flag,quick_flag,kdock_id)
        #建造加速
        if funck == 'createship_speedchange':
            return quick_creat(user,request.form['api_kdock_id'])
        #装备拆解
        if funck == 'destroyitem2':
            slotitem_ids = request.form['api_slotitem_ids']
            return destroyitem(user,slotitem_ids)
        #船只解体
        if funck == 'destroyship':
            api_ship_id = request.form['api_ship_id']
            return destroyship(user,api_ship_id)
        #获得舰娘
        if funck == 'getship':
            api_kdock_id = request.form['api_kdock_id']
            return getkship(user,api_kdock_id)

@app.route('/kcsapi/api_req_member/<funcm1>',methods=[ 'POST'])
def api_req_member(funcm1):
    if request.form['api_token']:
        uid = request.form['api_token']
        user = Userdata.query.filter_by(uid=uid).first()
        if funcm1 == 'get_incentive':
            return r'svdata={"api_result":1,"api_result_msg":"\u6210\u529f","api_data":{"api_count":0}}'
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
            return r'svdata={"api_result":1,"api_result_msg":"\u6210\u529f"}'

#秃子榜
@app.route('/kcsapi/api_req_ranking/getlist',methods=[ 'POST'])
def api_req_ranking():
    svdata = r'svdata={"api_result":1,"api_result_msg":"\u6210\u529f","api_data":{"api_count":10,"api_page_count":1,"api_disp_page":1,"api_list":[{"api_no":1,"api_member_id":19053956,"api_level":97,"api_rank":1,"api_nickname":"DMM噎屎了","api_experience":813259,"api_comment":"","api_rate":227,"api_flag":0,"api_medals":1,"api_nickname_id":"132175244","api_comment_id":"TEST"}]}}'
    return svdata

if __name__ == '__main__':
    app.run()




