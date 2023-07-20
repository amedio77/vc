import scrapy
from ..com.common import common_headers
from ..com.common import handle_error
from ..com.common import config


class Vc03Spider(scrapy.Spider):
    name = "vc03"

    def start_requests(self):
        service_key = config.get('SERVICE_KEY')
        page_no = config.get('PAGE_NO')
        num_of_rows = config.get('NUM_OF_ROWS')
        request_type = config.get('REQUEST_TYPE')
        request_url_str = config.get('REQUEST_URL_STR')

        print(request_url_str)

        request_url = f"{request_url_str}?ServiceKey={service_key}&pageNo={page_no}&numOfRows={num_of_rows}&resultType={request_type}"

        yield scrapy.Request(
            url=request_url,
            method='GET',
            headers=common_headers,
            callback=self.parse,
            errback=handle_error
        )

    def parse(self, response):
        self.logger.debug(f"Response text: {response.text}")
