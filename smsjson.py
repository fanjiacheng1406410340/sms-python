#-*- coding: utf-8 -*-
import urllib
import urllib2
import json
import hashlib
def req(info,url):
    args_data=json.loads(info)
    m=hashlib.md5()
    m.update(args_data["password"])
    args_data["password"]=m.hexdigest()
    post_url = "http://%s/json/sms/Submit" % url
    headers = {'Content-Type': 'application/json'}
    req = urllib2.Request(url = post_url, data=json.dumps(args_data),headers=headers,)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print res


def qunfa(info,url):
    args_data=json.loads(info)
    m=hashlib.md5()
    m.update(args_data["password"])
    args_data["password"]=m.hexdigest()
    post_url = "http://%s/json/sms/BatchSubmit" % url
    headers = {'Content-Type': 'application/json'}
    req = urllib2.Request(url = post_url, data=json.dumps(args_data),headers=headers,)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print res


def report(info,url):
    args_data=json.loads(info)
    m=hashlib.md5()
    m.update(args_data["password"])
    args_data["password"]=m.hexdigest()
    post_url = "http://%s/json/sms/Report" % url
    headers = {'Content-Type': 'application/json'}
    req = urllib2.Request(url = post_url, data=json.dumps(args_data),headers=headers,)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print res


def mo(info,url):
    args_data=json.loads(info)
    m=hashlib.md5()
    m.update(args_data["password"])
    args_data["password"]=m.hexdigest()
    post_url = "http://%s/json/sms/Deliver" % url
    headers = {'Content-Type': 'application/json'}
    req = urllib2.Request(url = post_url, data=json.dumps(args_data),headers=headers,)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print res

#############短信下发
#url="www.dh3t.com"
#info="""{"url":"www.dh3t.com",
#"account":"dh1234",
#"password":"lMm3PQ3O",
#"msgid":"",
#"msgmode":0,
#"phones":"13548563042",
#"content":"您的验证码是155",
#"sign":"【大汉三通】",
#"subcode":"",
#"sendtime":""}"""
#req(info,url)

##############群发
#url="www.dh3t.com"
#info="""{"account":"dh1234",
#         "password":"lMm3PQ3O",
#         "data":[{
#                   "msgid":"93786e387cf6462b9b60a36f8e7f1b27",
#                   "phones":"13333333333",
#                   "content":"你有一个快递,请注意查收。",
#                   "sign":"【大汉三通】",
#                   "subcode":"",
#                   "sendtime":""
#                  },{
#                   "msgid":"93786e387cf6462b9b60a36f8e7f1b28",
#                   "phones":"13333333333",
#                   "content":"您的订单今日送达",
#                   "sign":"【大汉三通】",
#                   "subcode":"",
#                   "sendtime":""
#                  }]
#        }"""
#qunfa(info,url)

###############状态报告
#url="www.dh3t.com"
#info="""{"account":"dh1234",
#         "password":"lMm3PQ3O"
#        }"""
#report(info,url)


###############上行
url="www.dh3t.com"
info="""{"account":"dh1234",
         "password":"lMm3PQ3O"
        }"""
mo(info,url)

