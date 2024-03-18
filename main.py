import asyncio
import logging
import os
from datetime import datetime

from dotenv import load_dotenv
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from telegram.ext import Application

# Load environment variables
load_dotenv()

# Logging configuration
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def crop_photo(screenshot_path):
    # Crop photo from bottom
    img = Image.open(screenshot_path)
    print(img.size)
    img = img.crop((0, 0, 800, 450))
    img.save(screenshot_path)


async def send_photo_via_telegram(bot_token, chat_id, photo_path):
    application = Application.builder().token(bot_token).build()

    with open(photo_path, "rb") as photo:
        media_message = await application.bot.send_photo(
            chat_id=chat_id,
            photo=photo,
            caption=f"Current time: {datetime.now().strftime('%H:%M:%S')}",
        )
        # media_message_id = media_message["message_id"]

        # Text if needed
        # message = await application.bot.send_message(chat_id=chat_id, text="Hello, world!")
        # message_id = message["message_id"]
        # await application.bot.edit_message_text(
        #     chat_id=chat_id, message_id=message_id, text="Hello, edited world!"
        # )

        logger.info("Photo sent successfully via Telegram.")


async def main():
    # Selenium setup with headless Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    service = Service(
        executable_path=os.getenv("CHROMEDRIVER_PATH", "./chromedriver.exe")
    )
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Telegram Bot setup
    telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")

    try:
        logger.info("Opening webpage...")
        driver.get("http://192.168.0.24:8080/browserfs.html")
        await asyncio.sleep(20)  # Wait for page load/any async operations on the page

        screenshot_path = "screenshot.png"
        driver.save_screenshot(screenshot_path)
        crop_photo(screenshot_path)

        logger.info(f"Screenshot saved to {screenshot_path}.")

        await send_photo_via_telegram(
            telegram_bot_token, telegram_chat_id, screenshot_path
        )

    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)
    finally:
        driver.quit()
        logger.info("WebDriver session closed.")


if __name__ == "__main__":
    asyncio.run(main())
