import http.client
import time
import json
import threading
from pprint import pprint

def get_binance_user_data(user_id):
    conn = http.client.HTTPSConnection("binance-futures-leaderboard1.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "467157cd05mshb970c2bf96194acp1f1317jsn55233c04915d",
        'X-RapidAPI-Host': "binance-futures-leaderboard1.p.rapidapi.com"
    }

    conn.request("GET", "/v1/getOtherPerformance?encryptedUid=" + user_id, headers=headers)

    response = conn.getresponse()
    performance_data = response.read()

    peformance = json.loads(performance_data.decode("utf-8"))

    pprint(peformance)


def get_user_position_data(user_id):
    conn = http.client.HTTPSConnection("binance-futures-leaderboard1.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "467157cd05mshb970c2bf96194acp1f1317jsn55233c04915d",
        'X-RapidAPI-Host': "binance-futures-leaderboard1.p.rapidapi.com"
    }

    conn.request("GET", "/v2/getTraderPositions?encryptedUid=" + user_id, headers=headers)

    response = conn.getresponse()
    data = response.read()

    positions = json.loads(data.decode("utf-8"))

    perpetual = positions['data'][0]['positions']['perpetual']

    while True:
        if perpetual is not None:
            pprint(positions)

        time.sleep(60)  # wait for 60 seconds before checking again


if __name__ == '__main__':
    thread1 = threading.Thread(target=get_binance_user_data, args=["C305DE28D092565778258E06DC31AAF9"])
    thread2 = threading.Thread(target=get_user_position_data, args=["C305DE28D092565778258E06DC31AAF9"])

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
