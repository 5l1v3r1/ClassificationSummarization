# -*- coding: utf-8 -*-
import os
import json
import io
__basedir__ = os.getcwd()


categories = os.listdir(__basedir__)

files_content = []
for category in categories:
    __dir__ = os.path.join(__basedir__, category)
    if not os.path.isfile(__dir__): # dosyayı dikkate almamak için
        for the_file in os.listdir(__dir__):
            with io.open(os.path.join(__dir__, the_file), 'r', encoding='utf8') as f:
                title = f.readline().replace("\n", "").strip()
                content = f.read().strip()
            files_content.append( {
                'id': u'{0}-{1}'.format(category, the_file.split('.txt')[0]),
                'category': u'{}'.format(category),
                'title': u'{}'.format(title),
                'content': u'{}'.format(content),
                'length': u'uzun' if len(content) > 1748 else u'kısa'
            } )

with open('result4.json', 'w',encoding='utf8') as fp:
    json.dump(files_content, fp, sort_keys=True)