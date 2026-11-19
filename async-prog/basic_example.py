import asyncio

async def async_start():
    print("Async started")

    async def do_work(name: str, secs: int):
        print(f"do work for {name} started")
        await asyncio.sleep(secs)   # time.sleep doesnt work because it doesnt return awaited obj
        print(f"------Work done for {name} & secs : {secs}")
        return f"Work done for {name}"

    task1 = asyncio.create_task(do_work("Like", 1))
    task2 = asyncio.create_task(do_work("Comment", 5))
    task3 = asyncio.create_task(do_work("Subscribe", 1.5))

    results = await asyncio.gather(task1, task2, task3)      # this is the line that awaits and collects all the data otherwise we get the Task pending msg
    print(f"results : {results}")

    # print(f"Results : {task1}, {task2}, {task3}")



asyncio.run(async_start())