"""Capture notebooklm-py GitHub repo screenshot"""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

SCREENSHOTS_DIR = Path(__file__).parent / "screenshots"

async def run():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1280, "height": 800})
        page = await context.new_page()

        print("[notebooklm-py GitHub]")
        await page.goto("https://github.com/teng-lin/notebooklm-py", timeout=60000)
        await page.wait_for_load_state("networkidle")
        await page.screenshot(path=str(SCREENSHOTS_DIR / "09a_notebooklm_py_github.png"))
        print("  ✓ 09a_notebooklm_py_github.png")

        print("[notebooklm-py PyPI]")
        await page.goto("https://pypi.org/project/notebooklm-py/", timeout=60000)
        await page.wait_for_load_state("networkidle")
        await page.screenshot(path=str(SCREENSHOTS_DIR / "09b_notebooklm_pypi.png"))
        print("  ✓ 09b_notebooklm_pypi.png")

        await browser.close()
        print("Done.")

asyncio.run(run())
