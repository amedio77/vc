import time
import scrapy
from multiprocessing import Process
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
# Import your spiders here
from vc.vc.spiders.vc01 import Vc01Spider
from vc.vc.spiders.vc02 import Vc02Spider
from vc.vc.spiders.vc03 import Vc03Spider


def run_crawler():
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(Vc01Spider)
    process.crawl(Vc02Spider)
    process.crawl(Vc03Spider)
    process.crawl(Vc01Spider)
    process.crawl(Vc02Spider)
    process.crawl(Vc03Spider)
    process.crawl(Vc01Spider)
    process.crawl(Vc02Spider)
    process.crawl(Vc03Spider)
    process.start()


# main entry point
if __name__ == '__main__':
    while True:
        # Start crawler in a separate process
        p = Process(target=run_crawler)
        try:
            p.start()
            p.join()
        except Exception as e:
            print("An error occurred: ", e)
            p.terminate()
            time.sleep(5)
            continue

        # Sleep for a while before the next crawl
        time.sleep(30)
