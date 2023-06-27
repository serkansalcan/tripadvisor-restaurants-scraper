import scrapy
from itemloaders.processors import TakeFirst, MapCompose


class TripadvisorItem(scrapy.Item):
    name = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())
    cuisine = scrapy.Field(input_processor=MapCompose(str.strip))
    reviews = scrapy.Field(input_processor=MapCompose(str.strip, lambda x: x.replace(",", "")), output_processor=TakeFirst())
    rating = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())
    address = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())
    email = scrapy.Field(input_processor=MapCompose(lambda x: x.replace("mailto:", "").replace("?subject=?", ""), str.strip), output_processor=TakeFirst())
    phone = scrapy.Field(input_processor=MapCompose(str.strip), output_processor=TakeFirst())

