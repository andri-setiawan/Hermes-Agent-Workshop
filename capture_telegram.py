"""
Capture Telegram screenshots — use web.telegram.org directly
and also capture @userinfobot page
"""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

SCREENSHOTS_DIR = Path(__file__).parent / "screenshots"
VIEWPORT = {"width": 1280, "height": 800}

async def run():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        context = await browser.new_context(viewport=VIEWPORT)
        page = await context.new_page()

        # Telegram web (will show login page - that's OK for tutorial)
        print("[05a] Telegram Web")
        try:
            await page.goto("https://web.telegram.org/k/", timeout=30000)
            await asyncio.sleep(3)
            await page.screenshot(path=str(SCREENSHOTS_DIR / "05a_telegram_web.png"))
            print("  ✓ 05a_telegram_web.png")
        except Exception as e:
            print(f"  ! {e}")

        # Telegram core register page
        print("[05b] Telegram Register/Core")
        try:
            await page.goto("https://my.telegram.org/", timeout=30000)
            await asyncio.sleep(2)
            await page.screenshot(path=str(SCREENSHOTS_DIR / "05b_my_telegram.png"))
            print("  ✓ 05b_my_telegram.png")
        except Exception as e:
            print(f"  ! {e}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
