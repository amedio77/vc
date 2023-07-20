import time
import os
from multiprocessing import Process
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# Import your spiders here
from vc.vc.spiders.vc01 import Vc01Spider
from vc.vc.spiders.vc02 import Vc02Spider
from vc.vc.spiders.vc03 import Vc03Spider

# Map from command-line spider names to Spider classes
SPIDERS = {
    'vc01': Vc01Spider,
    'vc02': Vc02Spider,
    'vc03': Vc03Spider
}


def run_crawler(spider_name):
    # Create the CrawlerProcess and start crawling
    process = CrawlerProcess(get_project_settings())
    process.crawl(SPIDERS[spider_name])
    process.start()


while True:
    # Read the spider name from the environment variable
    spider_name = os.environ.get('SPIDER_NAME')
    sleep_time = int(os.environ.get('SLEEP'))

    try:
        # Start crawler in a separate process
        p = Process(target=run_crawler, args=(spider_name,))
        p.start()
        p.join()
    except Exception as e:
        print("An error occurred: ", e)
        p.terminate()
        # time.sleep(5)
        # continue

    # Sleep for a while before the next crawl
    time.sleep(sleep_time)
