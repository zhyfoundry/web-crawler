from com.zhyfoundry.spider import Spider, Configuration
from com.zhyfoundry.spider.impl.demo import DemoFetcher, DemoParser, DemoTracker

class DemoSpider(Spider.Spider):

    def __init__(self):
        super(DemoSpider, self).__init__()

    def crawl(self):

        fetcher = DemoFetcher.DemoFetcher();
        html = fetcher.fetch("http://python.org/", Configuration.Configuration.readFromCfgFile());
        html = html.decode('gbk').encode('utf-8')

        parser = DemoParser.DemoParser()
        parseResult = parser.parse(html)
        print "http://python.org" + parseResult.content

        tracker = DemoTracker.DemoTracker()
        tracker.track(parseResult.newSeeds, "http://python.org/")
