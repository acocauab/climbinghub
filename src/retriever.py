"""Retrieve all pages from a certain domain.

This will be perform in async way.
"""

# ==== IMPORTS SECTION ========================================================
import aiohttp
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import typing
import asyncio

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

    async def retrieve(self, url: str = "") -> None:
        """Retrieve a single webpage.

        Args:
            url (str): Webpage URL to retrieve.
        """
        # Get the first URL
        if url == "":
            url = self.url
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                html = await response.text()
        self.get_all_links(html)
        # TODO: Call Analyzer

    def get_all_links(self, html: str) -> None:
        """Get all links from html and retrieve them.

        NOTE: Only the links that share domain with the original hostname

        Args:
            html (str): html to parse.

        """
        soup = BeautifulSoup(html, "html.parser")

        for link in soup.find_all('a'):
            url = link['href']
            hostname = urlparse(url).netloc
            if self.hostname == hostname:
                if url not in self.visited:
                    # NOTE: Do I need to save the task?
                    asyncio.ensure_future(self.retrieve(url))
                    self.visited.append(url)
                else:
                    continue
            else:
                continue
