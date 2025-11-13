import asyncio


async def async_add(a,b):

    print("Starting async_add")
    await asyncio.sleep(5)
    print("Result From async_add", a + b)
    return a + b

async def async_sub(a,b):

    print("Starting async_sub")
    print("Result From async_sub", a - b)
    return a - b

async def main():

    res_add, res_b = await asyncio.gather(
        async_add(1,2),
        async_sub(1, 2)
    )

if __name__ == "__main__":

    asyncio.run(main())