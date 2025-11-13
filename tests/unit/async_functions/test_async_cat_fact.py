import pytest_asyncio
from src.cat_fact import CatFact
from pytest import mark
from asyncmock import AsyncMock
from unittest.mock import patch


@pytest_asyncio.fixture
async def cat_fact():

    return CatFact()

@mark.asyncio
async def test_get_cat_fact(cat_fact):

    result = await cat_fact.get_cat_fact()
    print(result)
    assert result["status"] == 200
    assert "data" in result["result"]

@mark.asyncio
async def test_get_cat_fact_mocked(mocker):

    mock_response = { "status": 200, "result": {"data": "Cats are awesome!"}}
    mocker.patch.object(CatFact,"get_cat_fact", AsyncMock(return_value=mock_response))

    cat_fact_instance = CatFact()
    result = await cat_fact_instance.get_cat_fact()

    assert result["status"] == 200
    assert "data" in result["result"]
    assert result["result"]["data"] == "Cats are awesome!"

@mark.asyncio
async def test_get_cat_fact_mocked_patch_string(mocker):

    mock_response = { "status": 200, "result": {"data": "Cats are awesome!"}}
    mocker.patch("src.cat_fact.CatFact.get_cat_fact",AsyncMock(return_value=mock_response))

    cat_fact_instance = CatFact()
    result = await cat_fact_instance.get_cat_fact()

    assert result["status"] == 200
    assert "data" in result["result"]
    assert result["result"]["data"] == "Cats are awesome!"

@patch("src.cat_fact.CatFact.get_cat_fact",new_callable=AsyncMock)
@mark.asyncio
async def test_get_cat_fact_mocked_patch_decorator(mock_get):

    mock_get.return_value = { "status": 200, "result": {"data": "Cats are awesome!"}}

    cat_fact_instance = CatFact()
    result = await cat_fact_instance.get_cat_fact()

    assert result["status"] == 200
    assert "data" in result["result"]
    assert result["result"]["data"] == "Cats are awesome!"