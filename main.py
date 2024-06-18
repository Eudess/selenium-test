from crawler.national_obesity.crawler import national_crawler
from crawler.california_obesity.crawler import california_crawler

if __name__ == '__main__':
    national_crawler()
    california_crawler()