# import requests   # request is a sync library hence even after using async await it blocks the event loop until the api executes. Use httpx or aiohttp
import httpx
import asyncio

# async def fetch_data_from_url(url, num):
#     print(f"Fetching data from url : {num}")
#     resp = await requests.get(url)
#     return f"Execution done for {num}"

async def fetch_data_from_url(client, url, num):
    print(f"Fetching data from url : {num}")
    resp = await client.get(url)
    print(f"Got resp for {num}")
    return f"Execution done for {num}"

async def async_url_exec(): 
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/5",
        "https://httpbin.org/delay/1"
    ]

    async with httpx.AsyncClient(timeout=10.0) as Client:
        result = await asyncio.gather(*[fetch_data_from_url(Client, url, i+1) for i, url in enumerate(urls)])

    print("Executing line after gather")
    print(f"result : {result}")


asyncio.run(async_url_exec())


"""
# ❌ What you have (Indirect queuing):
result = await asyncio.gather(*[fetch_data_from_url(...) for ...])

# 🚀 Better Visualisation (Explicit queuing):
tasks = [asyncio.create_task(fetch_data_from_url(Client, url, i+1)) for i, url in enumerate(urls)]
# <-- At this exact point, all 3 tasks have ALREADY started running in the background!

result = await asyncio.gather(*tasks) # Now we just wait for them to finish

"""