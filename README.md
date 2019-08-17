# Music Store Scraper
A Scrapy (Python Framework) script to fetch all the instruments of a certain type (Bass, Guitar, Drums, etc)

## Instructions
Install the requirements (pip install -r requirements.txt)

Run the script with:
scrapy crawl music -a instrument='INSTRUMENT NAME'

If you want to store it into a JSON, CSV or XML file
scrapy crawl music -a instrument='INSTRUMENT NAME' -o FILENAME.FILE_EXTENSION

For example, if you want a bass list:
scrapy crawl music -a instrument='Bass' -o basses.json

Don't forget to edit your settings.py adding your USER_AGENT, DOWNLOAD_DELAY and CONCURRENT_REQUESTS to not choke the website. 

## Work In Progress
Right now only fetches:
- Brand
- Name
- Rating
- Description
- URL


I'll start adding things to the pipelines, items, downloading images, more instrument information, etc
