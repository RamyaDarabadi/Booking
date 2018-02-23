# -*- coding: utf-8 -*-

# Scrapy settings for Booking project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'Booking'

SPIDER_MODULES = ['Booking.spiders']
NEWSPIDER_MODULE = 'Booking.spiders'
ITEM_PIPELINES = {
        'Booking.pipelines.BookingPipeline': 300
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Booking (+http://www.yourdomain.com)'
