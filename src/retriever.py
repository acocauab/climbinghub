"""Retrieve all pages from a certain domain.

This will be perform in async way.
"""

# ==== IMPORTS SECTION ========================================================
import aiohttp
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import typing
import asyncio
from random import randint
from .analyzer import Analyzer
from .logs import logger
from .db import DBInterface

# ==== CONSTANTS DEFINITIONS ==================================================


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
        self.db = DBInterface()

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
        google_url = url
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Dnt": "1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
          }
        async with aiohttp.ClientSession() as session:
            async with session.get(google_url, headers=headers) as response:
                if response.status != 200:
                    logger.error(
                        "URL: " + url + " status code: "
                        + str(response.status))
                    return
                content_type = response.headers["Content-Type"]
                if "text/html" not in content_type:
                    logger.debug("URL: " + url + " is not a text/html")
                    return
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
                # To avoid querys to the db.
                if url not in self.visited:
                    await self.db.store_url(url, hostname)
                    self.visited.append(url)

    async def scheduler(self) -> None:
        """Schedule the next download."""
        await asyncio.sleep(randint(10, 20))
        asyncio.ensure_future(self.scheduler())
        url = await self.db.get_next_url()
        print(url)
        if url == "NO_URL":
            return
        else:
            await self.retrieve(url)
