"""FILE TITLE.

Short description
"""

# ==== IMPORTS SECTION ========================================================
import motor.motor_asyncio
from .logs import logger
# ==== CONSTANTS DEFINITIONS ==================================================


# ==== CLASS DEFINITION =======================================================
class DBInterface():
    """Database interface."""

    def __init__(self) -> None:
        """Conection to db."""
        # TODO: Use configurations to load the connection
        self.db =\
            motor.motor_asyncio.AsyncIOMotorClient(
                "mongodb://localhost:27017/")["CLIMBING_HUB"]

    async def store_url(self, url: str, host: str) -> None:
        """Store new discovered url.

        Args:
            url (str): url to store
            host (str): host for that url
        """
        data = {
            "_id": url,
            "host": host,
            "visited": False,
            "errors": None
        }
        try:
            await self.db["urls"].insert_one(data)
        except Exception as e:
            logger.debug("Url: " + url + "Already in the database")

    async def get_next_url(self) -> str:
        """Get the next parseable url.

        Returns:
            (str): url
        """
        response = await self.db["urls"].find_one({"visited": False})
        if response is None:
            return "NO_URL"

        # NOTE: If the request fail this url wont be retrieved again
        update = {"$set": {"visited": True}}
        query = {"_id": response["_id"]}
        await self.db["urls"].update_one(query, update)
        return response["_id"]
