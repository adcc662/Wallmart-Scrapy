import scrapy
from scrapy import Request

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

class DespensaSpider(scrapy.Spider):
    name = "despensa"
    allowed_domains = ["super.walmart.com.mx"]
    start_urls = ["https://super.walmart.com.mx/content/abarrotes/120005"]


    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, headers=headers)


    def parse(self, response):
        for department in response.css(".side-menu-item"):
            department_name = department.css("a::text").get().strip()
            department_url = response.urljoin(department.css("a::attr(href)").get())
            yield scrapy.Request(department_url, callback=self.parse_category, meta={"department": department_name})

    def parse_category(self, response):
        department = response.meta["department"]
        for category in response.css(".main-category-link"):
            category_name = category.css("a::text").get().strip()
            category_url = response.urljoin(category.css("a::attr(href)").get())
            yield scrapy.Request(category_url, callback=self.parse_subcategory, meta={"department": department, "category": category_name})

    def parse_subcategory(self, response):
        department = response.meta["department"]
        category = response.meta["category"]
        for subcategory in response.css(".subcategory-link"):
            subcategory_name = subcategory.css("a::text").get().strip()
            subcategory_url = response.urljoin(subcategory.css("a::attr(href)").get())
            yield {
                "department": department,
                "category": category,
                "subcategory": subcategory_name,
                "url": subcategory_url
            }
            
