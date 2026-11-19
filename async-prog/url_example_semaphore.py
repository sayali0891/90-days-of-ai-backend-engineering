import asyncio
import httpx

"""
For 1,000 network API requests, you should use concurrency (Asyncio) rather than multiprocessing.Here is why:Network-Bound vs. CPU-Bound: API calls are network-bound. Your code spends 99% of its time doing nothing—just sitting and waiting for data to travel across the internet.Resource Cost: Creating 1,000 OS processes (multiprocessing) would instantly crash your computer by consuming all your RAM and CPU. Concurrency, on the other hand, handles thousands of open connections smoothly inside a single process using almost no extra memory.The Problem with 1,000 Simultaneous RequestsIf you pass 1,000 URLs into asyncio.gather all at once, your script will try to open 1,000 network connections at the exact same millisecond. This will usually result in:The target server blocking your IP for attacking them (Rate limiting / DDOS protection).Your own operating system running out of available file descriptors/sockets and crashing.The Solution: asyncio.SemaphoreA Semaphore acts like a bouncer at a club. If you set a semaphore limit of 5, it means only 5 requests are allowed to run actively at any given time. As soon as one request finishes, the next one in line is allowed to start.
"""

async def fetch_data_from_url(client, url, num, semaphore):
    # 'async with semaphore' locks a spot. If 5 slots are full, it waits here.
    async with semaphore:
        print(f"Fetching data from url : {num} (Active)")
        resp = await client.get(url)
        print(f"Got resp for {num}")
        return f"Execution done for {num}"


async def async_url_exec():
    # Let's pretend we have 1000 URLs
    urls = ["https://httpbin.org"] * 1000

    # Create a Semaphore that restricts execution to 5 concurrent tasks max
    semaphore = asyncio.Semaphore(5)

    # Note: increased timeout because 1000 requests processed 5 at a time will take a while
    async with httpx.AsyncClient(timeout=30.0) as Client:

        # Pass the semaphore down into each task
        result = await asyncio.gather(
            *[
                fetch_data_from_url(Client, url, i + 1, semaphore)
                for i, url in enumerate(urls)
            ]
        )

    print(f"Total results collected: {len(result)}")


asyncio.run(async_url_exec())
