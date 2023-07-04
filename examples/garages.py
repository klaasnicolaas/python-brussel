# pylint: disable=W0621
"""Asynchronous Python client providing Open Data information of Brussel."""

import asyncio

from brussel import ODPBrussel


async def main() -> None:
    """Show example on using the Brussel API client for garages."""
    async with ODPBrussel() as client:
        garages = await client.garages(limit=25)

        count: int = len(garages)
        for item in garages:
            print(item)

        # Count unique id's in disabled_parkings
        unique_values: list[str] = [str(item.garage_id) for item in garages]
        num_values = len(set(unique_values))

        print("__________________________")
        print(f"Total garages found: {count}")
        print(f"Unique ID values: {num_values}")


if __name__ == "__main__":
    asyncio.run(main())
