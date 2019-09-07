import types


@types.coroutine
def downloader(url):
	yield "demo"


async def download_url(url):
	html = await downloader(url)
	return html


if __name__ == "__main__":
	coro = download_url("http://www.baidu.com")
	coro.send(None)
