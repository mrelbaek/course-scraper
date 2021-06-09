import requests

if __name__ == '__main__':
    API_KEY = '<YOUR API KEY>'
    URL_TO_SCRAPE = 'https://httpbin.org/ip'

    params = {'api_key': API_KEY, 'url': URL_TO_SCRAPE, 'render_js': 'false'}

    r = requests.get('http://app.scrapingbee.com/api/v1/', params=params, timeout=20)

    if r.status_code == 200:
        html = r.text
        print(html)
