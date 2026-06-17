"""
Hermes Agent Workshop — Screenshot Capture Script
Captures tutorial screenshots for each workshop section
"""
import asyncio
import os
from pathlib import Path
from playwright.async_api import async_playwright

SCREENSHOTS_DIR = Path(__file__).parent / "screenshots"
SCREENSHOTS_DIR.mkdir(exist_ok=True)

# Viewport
VIEWPORT = {"width": 1280, "height": 800}

async def screenshot(page, name, full_page=False):
    path = SCREENSHOTS_DIR / f"{name}.png"
    await page.screenshot(path=str(path), full_page=full_page)
    print(f"  ✓ {name}.png")
    return str(path)

async def run():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        context = await browser.new_context(viewport=VIEWPORT)
        page = await context.new_page()

        # ─────────────────────────────────────────────
        # 1. GitHub Repo
        # ─────────────────────────────────────────────
        print("\n[1] GitHub Repo")
        await page.goto("https://github.com/andri-setiawan/Hermes-Agent-Workshop", timeout=60000)
        await page.wait_for_load_state("networkidle")
        await screenshot(page, "01_github_repo")

        # ─────────────────────────────────────────────
        # 2. Hermes Install page
        # ─────────────────────────────────────────────
        print("\n[2] Hermes Install page")
        await page.goto("https://hermes-agent.nousresearch.com/docs/", timeout=60000)
        await page.wait_for_load_state("networkidle")
        await screenshot(page, "02_hermes_docs")

        # ─────────────────────────────────────────────
        # 3. Hermes Github page
        # ─────────────────────────────────────────────
        print("\n[3] Hermes GitHub")
        await page.goto("https://github.com/NousResearch/hermes-agent", timeout=60000)
        await page.wait_for_load_state("networkidle")
        await screenshot(page, "03_hermes_github")

        # ─────────────────────────────────────────────
        # 4. Custom provider config
        # ─────────────────────────────────────────────
        print("\n[4] Custom Provider Config")
        await page.goto("https://hermes-agent.nousresearch.com/docs/integrations/providers", timeout=60000)
        await page.wait_for_load_state("networkidle")
        await screenshot(page, "04_custom_provider_docs")

        # ─────────────────────────────────────────────
        # 5. Telegram BotFather
        # ─────────────────────────────────────────────
        print("\n[5] Telegram BotFather (web)")
        await page.goto("https://telegram.me/botfather", timeout=60000)
        await page.wait_for_load_state("networkidle")
        await screenshot(page, "05_telegram_botfather")

        # ─────────────────────────────────────────────
        # 6. Elsevier Developer Portal (Scopus)
        # ─────────────────────────────────────────────
        print("\n[6] Elsevier Dev Portal")
        await page.goto("https://dev.elsevier.com/", timeout=60000)
        await page.wait_for_load_state("networkidle")
        await screenshot(page, "06_elsevier_dev_portal")

        # ─────────────────────────────────────────────
        # 7. Google Cloud Console
        # ─────────────────────────────────────────────
        print("\n[7] Google Cloud Console")
        await page.goto("https://console.cloud.google.com/", timeout=60000)
        await page.wait_for_load_state("networkidle")
        await screenshot(page, "07_google_cloud_console")

        # ─────────────────────────────────────────────
        # 8. Stitch with Google
        # ─────────────────────────────────────────────
        print("\n[8] Stitch with Google")
        await page.goto("https://stitch.withgoogle.com/", timeout=60000)
        await page.wait_for_load_state("networkidle")
        await screenshot(page, "08_stitch_withgoogle")

        # ─────────────────────────────────────────────
        # 9. NotebookLM
        # ─────────────────────────────────────────────
        print("\n[9] NotebookLM")
        await page.goto("https://notebooklm.google.com/", timeout=60000)
        await page.wait_for_load_state("networkidle")
        await screenshot(page, "09_notebooklm")

        # ─────────────────────────────────────────────
        # 10. Hermes Profiles docs
        # ─────────────────────────────────────────────
        print("\n[10] Hermes Profiles docs")
        await page.goto("https://hermes-agent.nousresearch.com/docs/user-guide/profiles", timeout=60000)
        await page.wait_for_load_state("networkidle")
        await screenshot(page, "10_hermes_profiles_docs")

        await browser.close()
        print(f"\n✅ All screenshots saved to: {SCREENSHOTS_DIR}")

if __name__ == "__main__":
    asyncio.run(run())
