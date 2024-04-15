import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return response.content.decode('utf-8')

    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body)
    
get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
get_requester.load_json()