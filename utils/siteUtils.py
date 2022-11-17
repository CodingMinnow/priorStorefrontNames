import urllib.robotparser

def checkRobotsTxt():
    rp = urllib.robotparser.RobotFileParser()
    useragent = '*'

    rp.set_url('https://www.sellerratings.com/robots.txt')
    rp.read()

    rrate = rp.request_rate(useragent)
    print(f'Request-rate details: {rrate}')
    if rrate:
        print('Request-rate details')
        print(f'Number of requests: {rrate.requests}')
        print(f'Seconds: {rrate.seconds}')

    print(f'Crawl-delay: {rp.crawl_delay(useragent)}')

    if rp.can_fetch(useragent, 'https://www.sellerratings.com/amazon/usa'):
        print("All good! Scrape away!")
    else:
        print("Alert!! Can't scrape!")