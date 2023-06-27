from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from ..items import TripadvisorItem


class RestaurantSpider(CrawlSpider):
    name = "istanbul"
    allowed_domains = ["www.tripadvisor.com"]
    start_urls = ["https://www.tripadvisor.com/Restaurants-g293974-Istanbul.html"]

    collectLinks = Rule(LinkExtractor(restrict_css="div+ div > .o .Lwqic"), callback="parse_item", follow=False)
    next_page = Rule(LinkExtractor(restrict_css="a.nav.next"), follow=True)
    rules = (collectLinks, next_page)

    def parse_item(self, response):
        loader = ItemLoader(item=TripadvisorItem(), response=response)

        loader.add_css("name", ".HjBfq::text")
        loader.add_css("cuisine", ".dlMOJ+ .dlMOJ::text")
        loader.add_css("reviews", ".IcelI::text")
        loader.add_css("rating", ".ZDEqb::text")
        loader.add_css("address", ".kDZhm .FPPgD .yEWoV::text")
        loader.add_css("email", ".sNsFa+ .sNsFa a::attr(href)")
        loader.add_css("phone", "a span .yEWoV::text")

        yield loader.load_item()
