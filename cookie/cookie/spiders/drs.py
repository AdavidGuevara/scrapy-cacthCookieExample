import scrapy


class DrsSpider(scrapy.Spider):
    name = "drs"
    start_urls = ["https://drs.faa.gov/guest/login?targetUrl=/search"]
    custom_settings = {"COOKIES_ENABLE": True, "COOKIES_DEBUG": True}

    def parse(self, response):
        cookie = response.request.headers.get("Cookie")
        if cookie:
            value = cookie.split(b";")
            if len(value) > 0:
                jwt = value[1].decode().strip().replace("jwt=", "")
                yield {"jwt": jwt.split(".")[0]}
