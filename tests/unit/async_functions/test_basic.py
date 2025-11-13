from pytest import mark
from src.basic import async_add,async_sub
import pytest_asyncio
import asyncio

@mark.asyncio
async def test_async_add():

    result =  await async_add(5,1)

    assert result == 6

@mark.asyncio
async def test_async_sub():

    result = await async_sub(5,1)

    assert result

@pytest_asyncio.fixture
async def loaded_data():
    await asyncio.sleep(5)
    return {"key":"value"}

@mark.asyncio
async def test_fetch_data(loaded_data):
    assert loaded_data['key'] == "value"

