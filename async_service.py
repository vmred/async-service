import asyncio

import requests
import time


class AsyncService:
    def __init__(self):
        self.base_url = 'https://google.com'
        self.result_url = None

    def get_api_list(self):
        return [self.base_url + '/search?q=first', self.base_url + '/search?q=second',
                self.base_url + '/search?q=third']

    def wait_is_processed(self, iteration, timeout, polling=1):
        i = 0
        while i < timeout:
            response = requests.get(f'http://127.0.0.1:5000/get_document?iteration={iteration}').json()
            if response['status'] == 'success':
                print(f'---> success, iteration = {iteration}')
                self.result_url = response['url']
                break

            print(f'---> pending, iteration = {iteration}')
            i += polling
            time.sleep(polling)

    async def is_processed(self, iteration, timeout, polling=1):
        i = 0
        while i < timeout:
            response = requests.get('http://127.0.0.1:5000/get_document').json()
            if response['status'] == 'success':
                print(f'---> success, iteration = {iteration}')
                self.result_url = response['url']
                break

            print(f'---> pending, iteration = {iteration}')
            i += polling
            await asyncio.sleep(polling)
