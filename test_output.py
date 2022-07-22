# pylint: disable=W0621
"""Asynchronous Python client providing Open Data information of Brussel."""

import asyncio

from brussel import ODPBrussel


async def main() -> None:
    """Show example on using the Brussel API client."""
    async with ODPBrussel() as client:
        garages = await client.garages(limit=25)
        disabled_parkings = await client.disabled_parkings(limit=1000)

        print(garages)

        count: int
        for index, item in enumerate(disabled_parkings, 1):
            count = index
            print(item)
        print(f"{count} locations found")


if __name__ == "__main__":
    asyncio.run(main())
