# Scrapy settings for vc project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import datetime

BOT_NAME = "vc"

SPIDER_MODULES = ["vc.spiders"]
NEWSPIDER_MODULE = "vc.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "vc (+http://www.yourdomain.com)"

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "vc.middlewares.VcSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "vc.middlewares.VcDownloaderMiddleware": 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    "vc.pipelines.VcPipeline": 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# 모든 요청에 대해 실패 시 재시도를 수행수 설정.
RETRY_TIMES = 10
# RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 403, 404, 408]
# 200 이외의 모든 상태 코드를 재시도
# RETRY_HTTP_CODES = [x for x in range(100, 600) if x != 200]

# 각 요청 사이에 최소 딜레이
# 기본적으로 랜덤화된 다운로드 딜레이를 사용 (추가적으로 0.5 ~ 1.5 배의 랜덤한 딜레이를 추가)
CONCURRENT_REQUESTS = 100
DOWNLOAD_DELAY = 0

SPIDER_MIDDLEWARES = {
    'vc.middlewares.VcSpiderMiddleware': 100,
}

# 프록시 설정
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 100,
    'vc.middlewares.VcDownloaderMiddleware': 100,
    # 각 요청에 대해 URL을 로그에 기록하고, 요청이 완료되면 다시 로그를 남깁니다.
    'vc.middlewares.LogDownloadMiddleware': 900
}

LOG_ENABLED = True  # 로그 기능 활성화
LOG_LEVEL = 'DEBUG'  # 로그 레벨 설정 (DEBUG, INFO, WARNING, ERROR, CRITICAL 중 선택)
LOG_FORMAT = '%(asctime)s [%(name)s] %(levelname)s: %(message)s'  # 로그 포맷 설정
LOG_FILE = f'logs/vc_{datetime.datetime.now().strftime("%Y-%m-%d")}.log'
LOG_BACKUP_COUNT = 7  # 유지할 로그 파일 개수






