""""This Crawler gets data from Booking.com  website"""
# -*- coding: utf-8 -*-
import scrapy
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapy.http import Request
from Booking.items import *
class Booking(BaseSpider):
    """Starts name of the Crawler here"""
    name = "Booking"
    start_urls = ['https://www.booking.com/country/in.en-gb.html'] 
    def parse(self, response):
        """Nodes starts here""" 
        sel = Selector(response)
        Hotels = sel.xpath('//ul[@class="ia_body clearfix"]/li[@class="ia_section active"]//li[@class="ia_section_item  fl"]')
        for hotel in Hotels:
            link = ''.join(hotel.xpath('./a/@href').extract())
            url = 'https://www.booking.com'+link
            yield Request(url, callback = self.parse_hotel, meta={})
    def parse_hotel(self, response):
        """Moving to next link"""
        sel = Selector(response)
        City_Hotel = ''.join(sel.xpath('//div[@class="lp_promotion_cards_allproperties_box"]//p[@id="lp-featured-hotels-more"]/a/@href').extract())
        url = 'https://www.booking.com' + City_Hotel
        yield Request(url, callback = self.parse_Cityhotel, meta={})
    def parse_Cityhotel(self, response):
        sel = Selector(response)
        City_Hotels = sel.xpath('//div[@data-block-id="hotel_list"]//div[@data-hotelid]')
        State = ''.join(sel.xpath('//div[@property="itemListElement"][contains(@data-google-track, "province/")]/meta[@property="name"]/@content').extract())
        Country = ''.join(sel.xpath('//div[@property="itemListElement"][contains(@data-google-track, "country/")]/meta[@property="name"]/@content').extract())
        City = ''.join(sel.xpath('//div[@property="itemListElement"][contains(@data-google-track, "city/")]/meta[@property="name"]/@content').extract())
        for hotels in City_Hotels:
            Hotel_ID = ''.join(hotels.xpath('.//self::div/@data-hotelid').extract())
            Hotel_Name = ''.join(hotels.xpath('.//span[contains(@class, "sr-hotel__name")]//text()').extract()).replace('\n', '').strip()
            #City = ''.join(hotels.xpath('.//a[contains(@class, " jq_tooltip   district_link visited_link ")]//text()').extract())
            #City = replace('\n', '' )#getting show on map like that information as well #{'City': u'  Ooty\n            \u2013 Show on map' from your xpath 
            Booking = BookingItem()
            Booking['State'] = State
            Booking['Country'] = Country
            Booking['Hotel_ID'] = Hotel_ID
            Booking['Hotel_Name'] = Hotel_Name
            Booking['City'] = City
            yield Booking
        #next_page_link = ''.join(sel.xpath('//ul[@class="x-list"]//li[@class="sr_pagination_item current"]/a/@href').extract()) 
        next_page_link = ''.join(sel.xpath('//li[@class="sr_pagination_item current"]/following-sibling::li[1]/a/@href').extract())
        if next_page_link :
                yield Request(next_page_link, callback=self.parse_Cityhotel)


