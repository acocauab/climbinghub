"""FILE TITLE.

Short description
"""

# ==== IMPORTS SECTION ========================================================
from src.retriever import Retriever
import asyncio
# ==== CONSTANTS DEFINITIONS ==================================================

INITIAL = "https://www.rocjumper.com/escalada/via-tardo-calenta-k-forat-bruixes-coll-roig-montgrony/"
INITIAL = "https://www.rocjumper.com/"
# ==== CLASS DEFINITION =======================================================
async def main() -> None:
    """Just the main function."""
    r = Retriever(INITIAL)
    await r.retrieve(INITIAL)
    await r.scheduler()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
