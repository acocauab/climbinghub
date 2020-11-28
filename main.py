"""FILE TITLE.

Short description
"""

# ==== IMPORTS SECTION ========================================================
from src.retriever import Retriever
import asyncio
# ==== CONSTANTS DEFINITIONS ==================================================

INITIAL = "https://www.rocjumper.com/escalada/via-tardo-calenta-k-forat-bruixes-coll-roig-montgrony/"
# ==== CLASS DEFINITION =======================================================
async def main() -> None:
    """Just the main function."""
    r = Retriever(INITIAL)
    await r.retrieve(INITIAL)
    # print(r.website)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
