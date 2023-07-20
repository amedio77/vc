
config = {
    'SERVICE_KEY': 'DpsY0SLnLYLCVI9PHHVGKDbLLhv8NsDlcA74RTRvIdHAmZ0ouizGYFlgmQgr7%2BXP4ddGsB49OOpWygzeD%2BqTBA%3D%3D',
    'PAGE_NO': 1,
    'NUM_OF_ROWS': 1,
    'REQUEST_TYPE': 'json',
    'REQUEST_URL_STR': 'https://apis.data.go.kr/1160100/service/GetCorpBasicInfoService_V2/getCorpOutline_V2',
}

asp_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'WMONID=sllR9CylS0i; acgroupswithpersist=nada; JSESSIONID=lk6lLHv1fnqVKUVagPomzVV7vsVgsIIJuZia4wXQ3zLU4oN8xeekQ7ciglX1aKCS.ZG1fZGFydC9kYXJ0MV9kYXJ0X21zMQ==',
    'Referer': '',
    'Sec-Fetch-Dest': 'iframe',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="114", "Chromium";v="114", "Not-A.Brand";v="8"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

common_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'close',
    'Content-Type': 'application/json',
    'Cookie': 'WMONID=sllR9CylS0i; acgroupswithpersist=nada; JSESSIONID=lk6lLHv1fnqVKUVagPomzVV7vsVgsIIJuZia4wXQ3zLU4oN8xeekQ7ciglX1aKCS.ZG1fZGFydC9kYXJ0MV9kYXJ0X21zMQ==',
    'Referer': 'https://www.data.go.kr/index.do',
    'Sec-Fetch-Dest': 'iframe',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="114", "Chromium";v="114", "Not-A.Brand";v="8"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


def handle_error(self, response, failure):
    # error happened
    execution_number = response.meta.get('execution_number')
    yield {
        'url': failure.request.url,
        'error': str(failure),
        'execution_number': execution_number
    }