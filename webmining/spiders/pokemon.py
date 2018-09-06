import scrapy
import json
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
class GenerationOnePokemonScrapper(scrapy.Spider):
    name = "pokemon1"
    def start_requests(self):
        urls = [
            "https://pokemondb.net/pokedex/national"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        pokemonData = []
        for i in range(1,152):
            pokemonData.append({
                'name' : response.xpath("//html/body/main/div[3]/div["+str(i)+"]/span[2]/a//text()").extract()[0],
                'rank' : i
            })
        with open('generation1.json', 'w') as outfile:
            json.dump(pokemonData, outfile)
        print 'Data saved successfully!'

#second class to scrape generation 2 pokemons

class GenerationTwoPokemonScrapper(scrapy.Spider):
    name = "pokemon2"
    def start_requests(self):
        urls = [
            "https://pokemondb.net/pokedex/national"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        pokemonData = []
        for i in range(1,100):
            pokemonData.append({
                'name' : response.xpath("//html/body/main/div[4]/div["+str(i)+"]/span[2]/a//text()").extract()[0],
                'rank' : i+151
            })
        with open('generation2.json', 'w') as outfile:
            json.dump(pokemonData, outfile)
        print 'Data saved successfully!'
configure_logging()
runner = CrawlerRunner()
runner.crawl(GenerationOnePokemonScrapper)
runner.crawl(GenerationTwoPokemonScrapper)
d = runner.join()
d.addBoth(lambda _: reactor.stop())

reactor.run()