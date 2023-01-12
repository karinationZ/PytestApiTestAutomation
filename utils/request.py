from dataclasses import dataclass

import requests


@dataclass
class Response:
    status_code: int
    text: str
    body: object
    headers: dict
    description: str


class APIRequest:
    def get(self, url):
        response = requests.get(url)
        return self._get_responses(response)

    def post(self, url, payload, headers):
        response = requests.post(url, data=payload, headers=headers)
        return self._get_responses(response)

    def delete(self, url):
        response = requests.delete(url)
        return self._get_responses(response)

    @staticmethod
    def _get_responses(response):
        status_code = response.status_code
        text = response.text
        try:
            body = response.json()
        except Exception:
            body = {}

        headers = response.headers

        return Response(
            status_code, text, body, headers, f'{response.request.method} {response.url}')
