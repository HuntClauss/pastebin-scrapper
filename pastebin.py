import random
import string
import requests
import threading
import time

CHECKED = 0

def sendToServer(link):
    data = {"password": "salomona312", "data": link}
    requests.post("https://www.huntclauss.com.pl/other/pastebin.php", data)

def generateID(length=8):
    return ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(length)])

def startSearching(url_base, leng, thread_name):
    global CHECKED
    while True:
        id = generateID(leng)
        url = url_base + id
        resp = requests.get(url)
        CHECKED += 1
        if resp.status_code == 200:
            sendToServer(url)
            # print(url)
            # with open('result.txt', 'a') as file:
            #     file.writelines(url + "\n")


def stats():
    global CHECKED
    before_stat = 0
    while True:
        print(CHECKED, "(" + str((CHECKED-before_stat)/5) + "/s)")
        before_stat = CHECKED
        time.sleep(5)

def genThreads(base, leng, threads_count):
    threads = [threading.Thread(target=startSearching, args=(base, leng, ("Thread-" + str(i)),)) for i in range(threads_count)]
    threads.append(threading.Thread(target=stats))
    print("Created threads: ", len(threads)-1)
    for t in threads:
        t.start()
    for t in threads:
        t.join()

def test(url):
    resp = requests.get(url)
    print(resp)


genThreads("https://pastr.io/view/", 6, 16)

# startSearching("https://pastr.io/view/", 6)
# test("https://pastr.io/view/1nXTMs")

# https://pastr.io/view/1nXTMI
# https://throwbin.io/xHxhrld
