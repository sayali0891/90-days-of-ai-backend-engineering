import asyncio

async def do_work(name: str, secs: float) -> str:
    print(f"Async started for {name}")
    await asyncio.sleep(secs)
    print(f"------Work done for {name} & secs : {secs}")
    return f"Work done for {name}"

async def async_start():
    # Pass the coroutines directly into gather
    results = await asyncio.gather(
        do_work("Like", 1),
        do_work("Comment", 5),
        do_work("Subscribe", 1.5)
    )
    print(f"results : {results}")

if __name__ == "__main__":
    asyncio.run(async_start())
