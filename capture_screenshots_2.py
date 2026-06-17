"""
Hermes Agent Workshop — Screenshot Capture (Part 2)
Continue capturing remaining screenshots with try/except per page
"""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

SCREENSHOTS_DIR = Path(__file__).parent / "screenshots"
SCREENSHOTS_DIR.mkdir(exist_ok=True)
VIEWPORT = {"width": 1280, "height": 800}

async def safe_goto(page, url, timeout=30000):
    try:
        await page.goto(url, timeout=timeout)
        await page.wait_for_load_state("networkidle", timeout=15000)
        return True
    except Exception as e:
        print(f"    ! navigation warning: {e.__class__.__name__}")
        return False

async def screenshot(page, name, full_page=False):
    path = SCREENSHOTS_DIR / f"{name}.png"
    await page.screenshot(path=str(path), full_page=full_page)
    print(f"  ✓ {name}.png")

async def run():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        context = await browser.new_context(viewport=VIEWPORT)
        page = await context.new_page()

        targets = [
            ("05_telegram_botfather", "https://telegram.me/botfather"),
            ("06_elsevier_dev_portal", "https://dev.elsevier.com/"),
            ("07_google_cloud_console", "https://console.cloud.google.com/"),
            ("08_stitch_withgoogle", "https://stitch.withgoogle.com/"),
            ("09_notebooklm", "https://notebooklm.google.com/"),
            ("10_hermes_profiles_docs", "https://hermes-agent.nousresearch.com/docs/user-guide/profiles"),
        ]
        for name, url in targets:
            print(f"\n[{name}]")
            ok = await safe_goto(page, url)
            if ok:
                await screenshot(page, name)
            else:
                print(f"    skipping (page did not load)")

        await browser.close()
        print(f"\n✅ Done")

if __name__ == "__main__":
    asyncio.run(run())
