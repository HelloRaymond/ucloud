import hashlib
import urllib
import json
import requests

class ucloud_api:

    Region = {
        "cn-bj1":"北京一",
        "cn-bj2":"北京二",
        "cn-sh":"上海金融云",
        "cn-sh2":"上海二",
        "cn-gd":"广州",
        "cn-qz":"福建",
        "cn-hz":"杭州",
        "hk":"香港",
        "us-ca":"洛杉矶",
        "us-ws":"华盛顿",
        "ge-fra":"法兰克福",
        "th-bkk":"曼谷",
        "kr-seoul":"首尔",
        "sg":"新加坡",
        "tw-tp":"台北",
        "tw-kh":"高雄",
        "jpn-tky":"东京",
        "rus-mosc":"莫斯科",
        "uae-dubai":"迪拜",
        "idn-jakarta":"雅加达",
        "ind-mumbai":"孟买",
        "bra-saopaulo":"圣保罗",
        "uk-london":"伦敦",
        "afr-nigeria":"拉各斯",
        "vn-sng":"胡志明市"
    }
    Zone = {
        "cn-bj1-01":"北京一可用区A",
        "cn-bj2-02":"北京二可用区B",
        "cn-bj2-03":"北京二可用区C",
        "cn-bj2-04":"北京二可用区D",
        "cn-bj2-05":"北京二可用区E",
        "cn-sh-01":"金融云可用区A",
        "cn-sh-03":"金融云可用区C",
        "cn-sh2-01":"上海二可用区A",
        "cn-sh2-02":"上海二可用区B",
        "cn-sh2-03":"上海二可用区C",
        "cn-gd-02":"广州可用区B",
        "cn-qz-01":"GPU可用区A",
        "cn-hz-01":"杭州可用区A",
        "hk-01":"香港可用区A",
        "hk-02":"香港可用区B",
        "us-ca-01":"洛杉矶可用区A",
        "us-ws-01":"华盛顿可用区A",
        "ge-fra-01":"法兰克福可用区A",
        "th-bkk-01":"曼谷可用区A",
        "kr-seoul-01":"首尔可用区A",
        "sg-01":"新加坡可用区A",
        "tw-kh-01":"高雄可用区A",
        "tw-tp-01":"台北可用区A",
        "jpn-tky-01":"东京可用区A",
        "rus-mosc-01":"莫斯科可用区A",
        "uae-dubai-01":"迪拜可用区A",
        "idn-jakarta-01":"雅加达可用区A",
        "ind-mumbai-01":"孟买可用区A",
        "bra-saopaulo-01":"圣保罗可用区A",
        "uk-london-01":"伦敦可用区A",
        "afr-nigeria-01":"拉各斯可用区A",
        "vn-sng-01":"胡志明市可用区A"
    }
    def __init__(self,public,private):
        self.public = public
        self.private = private
    def __signature(self,private_key, params):
        items=params.items()
        # 请求参数串
        items = sorted(items)
        # 将参数串排序

        params_data = ""
        for key, value in items:
            params_data = params_data + str(key) + str(value)
        params_data = (params_data + private_key).encode('utf-8')
    
        sign = hashlib.sha1()
        sign.update(params_data)
        signature = sign.hexdigest()
    
        return signature
        # 生成的Signature值
    def __gen_json(self,action,spec_params):
        requests_common = {
            "Action"     :  action,
            "PublicKey"  :  self.public
        }
        requests = {**requests_common, **spec_params}
        requests['Signature'] = self.__signature(self.private,requests)
        return json.dumps(requests)
    def request(self,action,spec_params = {}):
        return requests.post(url='https://api.ucloud.cn', headers={"Content-Type": "application/json"}, data=self.__gen_json(action,spec_params))
    def GetRegion(self):
        return self.request("GetRegion")
    def GetProjectList(self):
        return self.request("GetProjectList")

class FireWalls_api(ucloud_api):
    def __init__(self,public,private):
        ucloud_api.__init__(self,public,private)
    def DescribeFirewall(self):
        data = {"Region":"hk"}
        response = ucloud_api.request(self,"DescribeFirewall",data)
        try:
            return json.loads(response.text)
        except:
            return {"RetCode":-1}
    def GrantFirewall(self,set_num):
        data = {"Region":"hk","FWId":set_num,"ResourceType":"UHost","ResourceId":"uhost-gg0plt"}
        response = ucloud_api.request(self,"GrantFirewall",data)
        try:
            return json.loads(response.text)["RetCode"]
        except:
            return {"RetCode":-1}


class UHost_api(ucloud_api):
    def __init__(self,public,private):
        ucloud_api.__init__(self,public,private)
    def DescribeUHostInstance(self):
        data = {"Region":"hk"}
        response = ucloud_api.request(self,"DescribeUHostInstance",data)
        try:
            return json.loads(response.text)
        except:
            return {"RetCode":-1}
    def DescribeImage(self):
        data = {"Region":"hk"}
        response = ucloud_api.request(self,"DescribeImage",data)
        try:
            return json.loads(response.text)
        except:
            return {"RetCode":-1}
    def StopUHostInstance(self,UHostId):
        data = {"Region":"hk","UHostId":UHostId}
        response = ucloud_api.request(self,"StopUHostInstance",data)
        try:
            return json.loads(response.text)["RetCode"]
        except:
            return {"RetCode":-1}
    def StartUHostInstance(self,UHostId):
        data = {"Region":"hk","UHostId":UHostId}
        response = ucloud_api.request(self,"StartUHostInstance",data)
        try:
            return json.loads(response.text)["RetCode"]
        except:
            return {"RetCode":-1}
    def RebootUHostInstance(self,UHostId):
        data = {"Region":"hk","UHostId":UHostId}
        response = ucloud_api.request(self,"RebootUHostInstance",data)
        try:
            return json.loads(response.text)["RetCode"]
        except:
            return {"RetCode":-1}
    def PoweroffUHostInstance(self,UHostId):
        data = {"Region":"hk","UHostId":UHostId}
        response = ucloud_api.request(self,"PoweroffUHostInstance",data)
        try:
            return json.loads(response.text)["RetCode"]
        except:
            return {"RetCode":-1}
    def ReinstallUHostInstance(self,UHostId,ImageId):
        data = {"Region":"hk","UHostId":UHostId,"ImageId":ImageId}
        response = ucloud_api.request(self,"ReinstallUHostInstance",data)
        try:
            return json.loads(response.text)["RetCode"]
        except:
            return {"RetCode":-1}


