"""Test the models."""
import aiohttp
import pytest
from aresponses import ResponsesMockServer

from brussel import DisabledParking, Garage, ODPBrussel

from . import load_fixtures


@pytest.mark.asyncio
async def test_all_garages(aresponses: ResponsesMockServer) -> None:
    """Test all garages function."""
    aresponses.add(
        "bruxellesdata.opendatasoft.com",
        "/api/records/1.0/search/",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixtures("garages.json"),
        ),
    )
    async with aiohttp.ClientSession() as session:
        client = ODPBrussel(session=session)
        spaces: list[Garage] = await client.garages()
        assert spaces is not None
        for item in spaces:
            assert isinstance(item, Garage)
            assert item.capacity is not None
            assert item.longitude is not None
            assert item.latitude is not None
            assert isinstance(item.longitude, float)
            assert isinstance(item.latitude, float)


@pytest.mark.asyncio
async def test_disabled_parkings(aresponses: ResponsesMockServer) -> None:
    """Test disabled parking spaces function."""
    aresponses.add(
        "bruxellesdata.opendatasoft.com",
        "/api/records/1.0/search/",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixtures("disabled_parkings.json"),
        ),
    )
    async with aiohttp.ClientSession() as session:
        client = ODPBrussel(session=session)
        spaces: list[DisabledParking] = await client.disabled_parkings()
        assert spaces is not None
        for item in spaces:
            assert item.spot_id is not None
            assert item.longitude is not None
            assert item.latitude is not None
            assert isinstance(item.longitude, float)
            assert isinstance(item.latitude, float)
