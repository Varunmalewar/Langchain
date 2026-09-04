import time
import asyncio

async def fetch_weather():
    print("Fetching weather data...")
    await asyncio.sleep(4)  # Simulate a delay (non-blocking)
    print("Weather data fetched.")

async def fetch_news():
    print("Fetching news...")
    await asyncio.sleep(2)  # Simulate a delay (non-blocking)
    print("News data fetched.")


async def main():
    start_time = time.time()

    await asyncio.gather(
        fetch_weather(),
        fetch_news()
    )

    end_time = time.time()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
