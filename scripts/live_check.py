#!/usr/bin/env python3
"""Read-only browser check for a live website demo."""

import argparse
import json
from pathlib import Path
from urllib.parse import urlparse

from playwright.sync_api import sync_playwright


VARIANTS = (
    ("desktop", 1440, 900),
    ("mobile", 375, 812),
)


def inspect_page(page):
    return page.evaluate("""() => {
      const images = [...document.images];
      const head = document.head;
      const meta = (name) => head.querySelector(`meta[name="${name}"]`)?.content || "";
      const ogImage = head.querySelector('meta[property="og:image"]')?.content || "";
      const footer = [...document.querySelectorAll('footer')].at(-1);
      return {
        title: document.title,
        theme: document.documentElement.dataset.theme || "",
        horizontalOverflowPx: Math.max(0, document.documentElement.scrollWidth - innerWidth),
        brokenImages: images.filter(img => img.complete && img.naturalWidth === 0).map(img => img.currentSrc || img.src),
        imagesWithoutAlt: images.filter(img => !img.hasAttribute('alt')).map(img => img.currentSrc || img.src),
        noindex: meta('robots').toLowerCase().includes('noindex'),
        ogImage,
        skipLink: !!document.querySelector('a[href="#main"], a[href="#content"]'),
        contact: {
          phone: !!document.querySelector('a[href^="tel:"]'),
          email: !!document.querySelector('a[href^="mailto:"]'),
          whatsapp: !!document.querySelector('a[href*="wa.me"], a[href*="whatsapp.com"]'),
        },
        legalLinks: footer ? [...footer.querySelectorAll('a')].filter(a => /privacy|cookie|voorwaarden/i.test(a.textContent || a.href)).map(a => ({text: a.textContent.trim(), href: a.href})) : [],
        favicon: head.querySelector('link[rel~="icon"]')?.href || "",
      };
    }""")


def run(url, out_dir, theme_selector):
    out_dir.mkdir(parents=True, exist_ok=True)
    report = {"url": url, "variants": [], "themePersistence": None}
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        try:
            for device, width, height in VARIANTS:
                for scheme in ("light", "dark"):
                    context = browser.new_context(
                        viewport={"width": width, "height": height},
                        device_scale_factor=1,
                        color_scheme=scheme,
                        reduced_motion="reduce",
                    )
                    page = context.new_page()
                    console_errors = []
                    page.on("console", lambda message: console_errors.append(f"{message.location.get('url', '')}: {message.text}") if message.type == "error" else None)
                    page.on("pageerror", lambda error: console_errors.append(str(error)))
                    item = {"device": device, "colorScheme": scheme, "viewport": [width, height]}
                    try:
                        response = page.goto(url, wait_until="domcontentloaded", timeout=30000)
                        page.wait_for_timeout(700)
                        item["status"] = response.status if response else None
                        item.update(inspect_page(page))
                        item["screenshot"] = f"{device}-{scheme}.png"
                        page.screenshot(path=str(out_dir / item["screenshot"]), full_page=True)
                        item["consoleErrors"] = console_errors
                        item["failures"] = []
                        if item["status"] != 200:
                            item["failures"].append(f"HTTP {item['status']}")
                        if item["horizontalOverflowPx"] > 1:
                            item["failures"].append("horizontal overflow")
                        if item["brokenImages"]:
                            item["failures"].append("broken images")
                        if console_errors:
                            item["failures"].append("console errors")
                    except Exception as error:
                        item["failures"] = [str(error)]
                    report["variants"].append(item)
                    context.close()

            if theme_selector:
                context = browser.new_context(viewport={"width": 1440, "height": 900})
                page = context.new_page()
                try:
                    page.goto(url, wait_until="domcontentloaded", timeout=30000)
                    before = page.locator("html").get_attribute("data-theme")
                    page.locator(theme_selector).click(timeout=5000)
                    after = page.locator("html").get_attribute("data-theme")
                    page.reload(wait_until="domcontentloaded")
                    reloaded = page.locator("html").get_attribute("data-theme")
                    report["themePersistence"] = {"before": before, "after": after, "reloaded": reloaded, "passed": before != after and after == reloaded}
                except Exception as error:
                    report["themePersistence"] = {"passed": False, "error": str(error)}
                context.close()
        finally:
            browser.close()

    (out_dir / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", help="Live http(s) URL to check")
    parser.add_argument("--out", type=Path, default=Path("qa-output"), help="Directory for screenshots and report.json")
    parser.add_argument("--theme-selector", help="CSS selector for an optional theme toggle button")
    args = parser.parse_args()
    if urlparse(args.url).scheme not in ("http", "https"):
        parser.error("URL must start with http:// or https://")
    report = run(args.url, args.out, args.theme_selector)
    for item in report["variants"]:
        label = f"{item['device']} {item['colorScheme']}"
        print(f"{label}: {'OK' if not item['failures'] else '; '.join(item['failures'])}")
    if report["themePersistence"] is not None:
        print(f"theme persistence: {'OK' if report['themePersistence']['passed'] else 'FAILED'}")
    print(f"Report: {args.out / 'report.json'}")
    failed = any(item["failures"] for item in report["variants"])
    failed |= bool(report["themePersistence"] and not report["themePersistence"]["passed"])
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
