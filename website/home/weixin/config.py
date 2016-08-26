#coding:utf-8
'''
Created on 2014-5-13

@author: skycrab
'''

# Refer to https://github.com/Skycrab/weixin-knife/

class WxPayConf_pub(object):
    """配置账号信息"""

    #=======【基本信息设置】=====================================
    #微信公众号身份的唯一标识。审核通过后，在微信发送的邮件中查看
    APPID = "xxx"
    #JSAPI接口中获取openid，审核后在公众平台开启开发模式后可查看
    APPSECRET = "xxx"
    #接口配置token
    TOKEN = "xxx"
    #受理商ID，身份标识
    MCHID = "xxx"
    #商户支付密钥Key。审核通过后，在微信发送的邮件中查看
    KEY = "xxx"
   

    #=======【异步通知url设置】===================================
    #异步通知url，商户根据实际开发过程设定
    NOTIFY_URL = "192.168.1.104:8000/payback"

    #=======【证书路径设置】=====================================
    #证书路径,注意应该填写绝对路径
    SSLCERT_PATH = "/******/cacert/apiclient_cert.pem"
    SSLKEY_PATH = "/******/cacert/apiclient_key.pem"

    #=======【curl超时设置】===================================
    CURL_TIMEOUT = 30

    #=======【HTTP客户端设置】===================================
    HTTP_CLIENT = "CURL"  # ("URLLIB", "CURL", "REQUESTS")


