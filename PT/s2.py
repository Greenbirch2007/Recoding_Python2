# asyncio 是 Python 用于解决异步 IO 编程的一整套解决方案   
import asyncio           
from functools import partial  

async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    print("end get url")
    # return "demo"

if __name__ == "__main__":
    tasks = [get_html("https://www.baidu.com") for i in range(10)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    # get_future = asyncio.ensure_future(get_html("https://www.baidu.com")) # loop.create_task()几乎等价
    # task = loop.create_task(get_html("https://www.baidu.com"))
    # task.add_done_callback(partial(callback, "https://www.baidu.com"))  
    # loop.run_until_complete(get_html("https://www.baidu.com"))
    # print(task.result()) # 打印返回值
    # loop.run_until_complete(asyncio.gather(*tasks))   # gather较wait更加 high-level  
    # call_later, call_at, call_soon, call_soon_threadsafe
