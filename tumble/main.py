"""
main.py
Contains classes for managing and downloading media from Tumblr
"""
import re
import bs4
import requests

from itertools import count
from typing import Optional
from .misc import pageQuery, mediaQuery

session = requests.Session()


class Blog:
    """
    A Blog object assists with downloading media from a specific blog.
    It holds very basic information for cycling through all
    """
    def __init__(self, blogid, download: bool = True, max_pages: int = -1):
        """
        :param download: If true, begin downloading immediately following initialization.
        :param max_pages: The maximum number of pages
        """

        self.id = blogid
        self.max_pages = max_pages

        self.media_queue = []  # Stores URLs to media
        self.processed_media = []  # Stores URLs for successfully processed media
        self.pages = []  # Stores Request objects for every page. Index 0 => Page 1

        if download:
            self.process()

    def process(self, require_download: int = -1) -> None:
        """
        Processes the entire Tumblr blog acquiring all Media URLs
        :param require_download: The number of media endpoints the function will pass before downloading media early
        """

        # count up infinitely if a maximum page count is never offered
        pages = count(start=1) if self.max_pages == -1 else range(1, self.max_pages)

        for page in pages:
            urls = self.getMedia(page)
            if urls is not None:
                print(urls)
            else:
                print(f'Last page processed ({page}).')
                break

    def getMedia(self, page: int) -> Optional[str]:
        """
        Processes a Tumblr page on a blog, locating all media URLs.

        :param page: The page index
        :return: A list of URLs for pictures or videos found on the associated page
        """

        data = session.get(self.pageURL(page)).text
        soup = bs4.BeautifulSoup(data, 'lxml')

        urls = []

        posts = soup.find_all(class_=re.compile('post-\d+'))
        if len(posts) == 0:
            print('No posts found on page. Quitting.')
            return None
        else:
            print(f'{len(posts)} posts found on page.')

        for videoTag in soup.find_all(class_='video'):
            pass

        for photosetTag in soup.find_all(class_='photoset'):
            pass

        for photoTag in soup.find_all(class_='photo'):
            pass

        return urls

    def pageURL(self, page) -> str:
        """
        Returns the appropriate URL for a given page, for a given Tumblr blog
        :param page: The page index
        :return: The URL-like string containing the URL to the given page
        """
        return f'https://{self.id}.tumblr.com{f"/page/{page}" if page > 0 else ""}'
