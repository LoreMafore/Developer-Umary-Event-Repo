import asyncio
import aiohttp
import time

# Trying to learn async/await
# Getting confused by event loops and coroutines

async def fetch_url(session, url):
    """Fetch a single URL"""
    try:
        async with session.get(url) as response:
            # TODO: check status code
            data = await response.text()
            return data
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

async def fetch_all(urls):
    """Fetch multiple URLs concurrently"""
    async with aiohttp.ClientSession() as session:
        # TODO: is this the right way to create tasks?
        tasks = []
        for url in urls:
            task = asyncio.create_task(fetch_url(session, url))
            tasks.append(task)
        
        # Wait for all tasks
        results = await asyncio.gather(*tasks)
        return results

def main():
    """Main function"""
    urls = [
        'https://example.com',
        'https://example.org',
        'https://example.net'
    ]
    
    # TODO: how do I run async function from sync code?
    # asyncio.run(fetch_all(urls))  # this gives warnings
    
    # Or should I use this?
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(fetch_all(urls))
    
    pass

# TODO: add retry logic with exponential backoff
# async def fetch_with_retry(session, url, max_retries=3):
#     

# TODO: add rate limiting
# Getting 429 errors from API

# TODO: add timeout handling
# Some requests hang forever

if __name__ == "__main__":
    main()
    print("Done")  # this prints before tasks complete?
