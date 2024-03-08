# pylint: disable=W0621
"""Asynchronous Python client providing Open Data information of Brussel."""

from __future__ import annotations

import asyncio

from brussel import ODPBrussel


async def main() -> None:
    """Show example on using the Brussel API client for disabled parkings."""
    async with ODPBrussel() as client:
        disabled_parkings = await client.disabled_parkings(limit=1000)

        count: int = len(disabled_parkings)
        for item in disabled_parkings:
            print(item)

        # Count unique id's in disabled_parkings
        unique_values: list[str] = [str(item.spot_id) for item in disabled_parkings]
        num_values = len(set(unique_values))

        print("__________________________")
        print(f"Total locations found: {count}")
        print(f"Unique ID values: {num_values}")


if __name__ == "__main__":
    asyncio.run(main())
