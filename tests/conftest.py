"""Fixture for the Brussel tests."""

from collections.abc import AsyncGenerator

import pytest
from aiohttp import ClientSession

from brussel import ODPBrussel


@pytest.fixture(name="odp_brussel_client")
async def client() -> AsyncGenerator[ODPBrussel, None]:
    """Brussel client fixture."""
    async with (
        ClientSession() as session,
        ODPBrussel(session=session) as odp_brussel_client,
    ):
        yield odp_brussel_client
