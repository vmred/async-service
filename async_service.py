import grequests


class AsyncService:
    def __init__(self):
        self.base_url = 'https://google.com'

    def get_api_list(self):
        return [self.base_url + '/search?q=first', self.base_url + '/search?q=second',
                self.base_url + '/search?q=third']

    def verify_documents(self):
        responses = grequests.map([grequests.get(x) for x in self.get_api_list()])
        for i in responses:
            print('--> %s,  %d' % (i.url, i.status_code))
