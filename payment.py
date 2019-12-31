#!/usr/bin/python3
import requests
from datetime import datetime


eth = 'https://api.nanopool.org/v1/eth/payments/WALLET'
xmr = 'https://api.nanopool.org/v1/xmr/payments/WALLET'


def get_info(wallet):
    r = requests.get(wallet)

    json_dict = r.json()

    amount = []

    for data in json_dict['data']:
        if datetime.utcfromtimestamp(data['date']).strftime('%Y-%m-%d %H:%M:%S') >= '2019-05-01' and datetime.utcfromtimestamp(data['date']).strftime('%Y-%m-%d %H:%M:%S') < '2019-06-01':
            print(f"{data['amount']} | {datetime.utcfromtimestamp(data['date']).strftime('%Y-%m-%d %H:%M:%S')}")
            amount.append(data['amount'])
    print(f"Total payments: {len(amount)} | Sum of all payments {sum(amount)}")

if __name__ == "__main__":
    get_info(eth)