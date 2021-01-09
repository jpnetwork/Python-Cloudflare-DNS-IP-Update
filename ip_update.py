#!/usr/bin/env python
import requests
import json
import sys 

IP_API = 'https://api.ipify.org?format=json' #อ่านค่า Public IP ของเน็ตที่กำลังใช้งานอยู่
CF_API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  #ค่า Global API Key เอาจาก Cloudflare ตรงเมนู 'My Profile'
CF_EMAIL = 'xxxxxx@myemail.com'    #อีเมล์ที่เป็น Username ของ Cloudflare
ZONE_ID = '111xxxxxxxxxxxxxxxxxxxxxx'  #ดูจากหน้า Dashboard ของโดเมนเนม ใน Cloudflare
RECORD_ID = ''  ##ค่า RECORD_ID นี้ให้ทำการรัน Script ก่อน 1 ครั้ง จากนั้นระบบจะแสดงผล เป็นชื่อ dns name ที่เราสร้างไว้ใน DNS ของ Cloudflare ให้คัดลองตรง "id": "xxxxxxx"  มาใส่


if not RECORD_ID:
    resp = requests.get(
        'https://api.cloudflare.com/client/v4/zones/{}/dns_records'.format(ZONE_ID),
        headers={
            'X-Auth-Key': CF_API_KEY,
            'X-Auth-Email': CF_EMAIL
        })
    print(json.dumps(resp.json(), indent=4, sort_keys=True))
    print('Please find the DNS record ID you would like to update and entry the value into the script')
    sys.exit(0)

resp = requests.get(IP_API)
ip = resp.json()['ip']


resp = requests.put(
    'https://api.cloudflare.com/client/v4/zones/{}/dns_records/{}'.format(
        ZONE_ID, RECORD_ID),
    json={
        'type': 'A',
        'name': 'myname.myweb.com',
        'content': ip,
        'proxied': False
    },
    headers={
        'X-Auth-Key': CF_API_KEY,
        'X-Auth-Email': CF_EMAIL
    })
assert resp.status_code == 200

print('Updated dns record for {}'.format(ip))
