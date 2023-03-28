import time
import requests
import json
import urllib.request 
from urllib.request import Request, urlopen
import urllib.error
from threading import Timer

DNSPodLoginToken='Login_Token' #'123456,qazwsxedcrfv'
DominId='DominId' #'123456'
RecordId='RecordId' #'123456'
 


def getLocalIPV4():   
# http://ip.42.pl/raw
# https://ifconfig.me/ip
  getIPResponse = requests.request("GET", 'https://ifconfig.me/ip', headers={}, data={},timeout=10)
  if(getIPResponse.status_code==200):  
   return getIPResponse.text
 
def getLocalIPV4_01(): 
   # http://jsonip.com
   # https://api.ipify.org?format=json
   getIPResponse = requests.request("GET", 'https://api.ipify.org?format=json', headers={}, data={},timeout=20)
   if(getIPResponse.status_code==200):  
    #print(getIPResponse.text)
    responseObj = json.loads(getIPResponse.text)
    ipstr=responseObj["ip"]
    return ipstr
  
def getDomainRecords():
   url="https://dnsapi.cn/Record.List"
   data={
    'login_token': DNSPodLoginToken,
    'format': 'json',
    'domain_id': DominId,
    }
   getDomainResponse = requests.request("POST", url, headers={}, data=data,timeout=10)
   if(getDomainResponse.status_code==200):  
    print(getDomainResponse.text) 


def updateDNSRecord(newip):
  #doc: https://docs.dnspod.cn/api/update-dns-records/
  #login_token : need signup and get token
  #domain_id：
  #record_id：
  #sub_domain
  url="https://dnsapi.cn/Record.Ddns"
  data={
    'login_token': '398390,f244936090331d24d4e746bfc74ad8ab',
    'format': 'json',
    'domain_id': DominId,
    'record_id': RecordId,
    'record_line': '默认',
    'record_line_id': '0',
    'value': newip,
    'sub_domain': 'rasp'
  }
  updateDNSResponse = requests.request("POST", url, headers={}, data=data,timeout=10)
  if(updateDNSResponse.status_code==200):  
    #print(updateDNSResponse.text) 
    responseObj = json.loads(updateDNSResponse.text)
    respStatus=responseObj["status"]["code"]
    if(respStatus=='1'):
      return 'success'
    else:
      return 'fail'

  
#getDomainRecords()

def GetIPv4UpdateDNSRecord(): 
  currentIP=getLocalIPV4_01()
  print(updateDNSRecord(currentIP))

#update dns every 120s once
if __name__=='__main__':
    GetIPv4UpdateDNSRecord()
    sTimer = Timer(120, GetIPv4UpdateDNSRecord)
    sTimer.start()




      