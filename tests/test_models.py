"""Test the models."""

from __future__ import annotations

from typing import TYPE_CHECKING

from aresponses import ResponsesMockServer
from syrupy.assertion import SnapshotAssertion

from . import load_fixtures

if TYPE_CHECKING:
    from brussel import DisabledParking, Garage, ODPBrussel


async def test_all_garages(
    aresponses: ResponsesMockServer,
    snapshot: SnapshotAssertion,
    odp_brussel_client: ODPBrussel,
) -> None:
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
    spaces: list[Garage] = await odp_brussel_client.garages()
    assert spaces == snapshot


async def test_disabled_parkings(
    aresponses: ResponsesMockServer,
    snapshot: SnapshotAssertion,
    odp_brussel_client: ODPBrussel,
) -> None:
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
    spaces: list[DisabledParking] = await odp_brussel_client.disabled_parkings()
    assert spaces == snapshot
