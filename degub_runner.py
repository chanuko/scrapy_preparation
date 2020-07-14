import os
from scrapy.cmdline import execute

os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.chdir('samplesite')

try:
    execute(
        [
            'scrapy',
            'crawl',
            'samplesite'',
            #'-o',
            #'out.csv',
        ]
    )
except SystemExit:
    pass