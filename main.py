import asyncio
import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from telegram import Bot

load_dotenv()


async def main():
    # Setup Selenium with headless Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    # Your Telegram Bot's token and the chat ID
    telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")
    bot = Bot(token=telegram_bot_token)

    try:
        # Open the webpage
        driver.get("http://192.168.0.24:8080/browserfs.html")
        await asyncio.sleep(5)

        # Take screenshot
        screenshot_path = "screenshot.png"
        driver.save_screenshot(screenshot_path)

        # Send the screenshot over Telegram
        with open(screenshot_path, "rb") as photo:
            await bot.send_photo(chat_id=telegram_chat_id, photo=photo)
    finally:
        driver.quit()


if __name__ == "__main__":
    asyncio.run(main())
