import asyncio

from ..constants import DRAFT_API_URLS
from ..utils import fetch

class DraftLeague():
    """
    A class representing a Draft Classic or H2H league in the Fantasy Premier League. 
    H2H draft leagues will have an additional attribute (matches), which is a list of fixtures in the league.

    Basic usage::

        from fpl import FPL
        import aiohttp
        import asyncio
        >>>
        async def main():
            async with aiohttp.ClientSession() as session:
                fpl = FPL(session)
                draft_league = await fpl.get_draft_league(123456)
            print(draft_league)
        ...
        # Python 3.7+
        asyncio.run(main())
        ...
        # Python 3.6
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        League 829116 - 829116

    """ 
    def __init__(self, league_information, session):
        self._session = session

        for k, v in league_information.items():
            setattr(self, k, v)

    async def get_waivers(self):
        """Returns a list of waivers / trades in the Draft league.

        Information is taken from e.g.:
            https://draft.premierleague.com/api/draft/league/123456/transactions

        """
        fixtures = await fetch(self._session, DRAFT_API_URLS["transactions"].format(self.league["id"]))

        return fixtures

    async def get_trades(self):
        """Returns a list of trades in the Draft league.

        Information is taken from e.g.:
            https://draft.premierleague.com/api/draft/league/123456/trades

        """
        trades = await fetch(self._session, DRAFT_API_URLS["trades"].format(self.league["id"]))

        return trades

    def __str__(self):
        return f"{self.league['name']} - {self.league['id']}"