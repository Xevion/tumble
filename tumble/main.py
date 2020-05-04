"""
main.py
Contains classes for managing and downloading media from Tumblr
"""

class Blog:
    def __init__(self, blogid, download: bool = True, max_pages: int = 99999):
        """
        :param download: If true, begin downloading immediately following initialization.
        :param max_pages: The maximum number of pages
        """

        self.id = blogid
        self.max_pages = max_pages

        self.media_urls = []
        self.pagenum = 0

        if download:
            self.process()

    def process(self) -> None:
        for page in range(1, self.max_pages):
            url = self.pageURL(page)

    def pageURL(self, page):
        return f'https://{self.id}.tumblr.com' + f'/page/{page}' if page > 0 else ''
