"""Retrieve all pages from a certain domain.

This will be perform in async way.
"""

# ==== IMPORTS SECTION ========================================================
import aiohttp
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import typing
import asyncio
import logging
from .analyzer import Analyzer

# ==== CONSTANTS DEFINITIONS ==================================================
# logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# ==== CLASS DEFINITION =======================================================
class Retriever():
    """Retrive pages from domain."""

    def __init__(self, url: str)-> None:
        """__init__.

        Args:
            url (str): Webpage URL.
        """
        self.url = url
        self.hostname = urlparse(self.url).netloc
        self.visited: typing.List[str] = []

    async def retrieve(self, url: str = "") -> None:
        """Retrieve a single webpage.

        Args:
            url (str): Webpage URL to retrieve.
        """
        # Get the first URL
        logger.debug("Retrieving url: " + url)
        if url == "":
            url = self.url
        google_url =\
            "http://webcache.googleusercontent.com/search?q=cache:" + url
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'
            ' AppleWebKit/537.36 (KHTML, like Gecko)'
            ' Chrome/39.0.2171.95 Safari/537.36'
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                html = await response.text()
        await self.get_all_links(html)
        analyzer = Analyzer(url, html)
        analyzer.analyze()

    async def get_all_links(self, html: str) -> None:
        """Get all links from html and retrieve them.

        NOTE: Only the links that share domain with the original hostname

        Args:
            html (str): html to parse.

        """
        soup = BeautifulSoup(html, "html.parser")

        for link in soup.find_all('a', href=True):
            url = link['href']
            hostname = urlparse(url).netloc
            if self.hostname == hostname:
                if url not in self.visited:
                    # NOTE: Do I need to save the task?
                    asyncio.sleep(1)
                    asyncio.ensure_future(self.retrieve(url))
                    self.visited.append(url)
                else:
                    continue
            else:
                continue
