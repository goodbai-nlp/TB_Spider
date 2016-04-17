# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import requests
import os
import settings
class PicgetPipeline(object):
    def __init__(self):
        self.images = []
        self.dir = os.getcwd() + settings.IMAGES_STORE
        if not os.path.exists(self.dir):
            os.makedirs(self.dir)

    def process_item(self, item, spider):
        if 'image_urls' in item:
            for tmpitem in item['image_urls']:
                us = tmpitem.split('/')[6:]
                image_name = '_'.join(us)
                file = '%s/%s' % (self.dir, image_name)
                self.images.append(file)
                if os.path.exists(file):
                    continue
                with open(file, 'wb') as handle:
                    response = requests.get(tmpitem, stream=True)
                    for block in response.iter_content(1024):
                        if not block:
                            break
                        handle.write(block)
            item['images'] = self.images
        return item
