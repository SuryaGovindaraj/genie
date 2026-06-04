# Generated Playwright Tests for home
from playwright.sync_api import sync_playwright, expect, TimeoutError as PlaywrightTimeoutError
from home_pom import GeneratedPage
import json
import re
import time
import os

urls = {}
from Utility import Utility


# Test Case 1 - TC-0001
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
# Global URLs dictionary (update with actual URL as needed)
urls: dict[str, str] = {
    "main_page": os.environ.get("CALCULATOR_MAIN_URL", "http://localhost:8000/")
}
def test_calculator_title_is_displayed_correctly_on_main_page() -> None:
    """
    TC-0001: Calculator Title Is Displayed Correctly on Main Page
    Verifies that the calculator title is always visible, correctly styled,
    and consistently displayed at the top of the main page.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        header_xpath: str = "//h1[normalize-space()='Simple Calculator']"
        header_selector: str = f"xpath={header_xpath}"
        timeout: int = 15000
        # Attach console message logger
        page.on("console", lambda msg: Utility.log_console_message(msg))
        try:
            # --- Given: Setup and navigation to initial state ---
            Utility.log_test_step("Navigate to the main page of the calculator application.")
            navigation_success: bool = Utility.navigate_to_page(page, urls["main_page"], timeout=timeout)
            if not navigation_success:
                Utility.log_test_result("FAIL", "Navigation to main page failed.")
                raise Exception("Navigation to main page failed.")
            Utility.log_test_step("Wait for the page body to be visible.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=timeout)
            # Accept cookies/pop-ups if present
            cookie_accepted: bool = False
            cookie_selectors: list[str] = [
                "text=Accept", "text=I Agree", "text=Got it", "text=Allow"
            ]
            for selector in cookie_selectors:
                if Utility.wait_for_element_state(page, selector, state="visible", timeout=3000):
                    Utility.safe_wait_and_interact(page, selector, "click", timeout=timeout)
                    cookie_accepted = True
                    Utility.log_test_step(f"Accepted cookie popup using selector: {selector}")
                    break
            # --- When: Perform the action ---
            Utility.log_test_step("Validate essential calculator elements are visible.")
            Utility.retry_assertion(
                lambda: generated_page.validate_essential_elements(),
                retries=3,
                delay=1000
            )
            Utility.log_test_step("Observe the top section of the page for the header.")
            Utility.retry_assertion(
                lambda: expect(page.locator(header_selector)).to_be_visible(timeout=timeout),
                retries=3,
                delay=1000
            )
            Utility.log_element_state("Calculator Header", page.locator(header_selector), timeout=timeout)
            # --- Then: Verify expected outcomes ---
            # 1. The header "Simple Calculator" is visible and clearly displayed.
            Utility.log_test_step("Verify the header text is 'Simple Calculator'.")
            header_text: str = Utility.get_element_text(page, header_selector, timeout=timeout)
            header_text = Utility.validate_and_convert_data(header_text, str)
            if header_text.strip() != "Simple Calculator":
                Utility.log_test_result("FAIL", f"Header text mismatch: '{header_text}'")
                raise AssertionError(f"Header text mismatch: '{header_text}'")
            Utility.log_test_result("PASS", "Header text is correct.")
            # 2. The header is centered or appropriately aligned as per the page layout.
            Utility.log_test_step("Check the alignment of the header.")
            bounding_box = page.locator(header_selector).bounding_box()
            viewport_width = page.viewport_size["width"] if page.viewport_size else 1920
            if bounding_box:
                header_center = bounding_box["x"] + bounding_box["width"] / 2
                viewport_center = viewport_width / 2
                alignment_diff = abs(header_center - viewport_center)
                if alignment_diff > 50:
                    Utility.log_test_result("FAIL", f"Header alignment off by {alignment_diff:.2f}px")
                    raise AssertionError(f"Header alignment off by {alignment_diff:.2f}px")
                Utility.log_test_result("PASS", "Header is centered/aligned properly.")
            else:
                Utility.log_test_result("FAIL", "Could not determine header bounding box.")
                raise AssertionError("Could not determine header bounding box.")
            # 3. The header uses a readable font and is visually distinct from other text.
            Utility.log_test_step("Verify the font style and size of the header.")
            font_size = page.locator(header_selector).evaluate("el => window.getComputedStyle(el).fontSize")
            font_weight = page.locator(header_selector).evaluate("el => window.getComputedStyle(el).fontWeight")
            if not font_size or float(font_size.replace("px", "")) < 18:
                Utility.log_test_result("FAIL", f"Header font size too small: {font_size}")
                raise AssertionError(f"Header font size too small: {font_size}")
            if not font_weight or int(font_weight) < 500:
                Utility.log_test_result("FAIL", f"Header font weight not bold enough: {font_weight}")
                raise AssertionError(f"Header font weight not bold enough: {font_weight}")
            Utility.log_test_result("PASS", f"Header font size: {font_size}, font weight: {font_weight}")
            # 4. The header remains at the top and is not hidden or overlapped after scrolling.
            Utility.log_test_step("Scroll the page and confirm header remains visible.")
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            Utility.retry_assertion(
                lambda: expect(page.locator(header_selector)).to_be_visible(timeout=timeout),
                retries=3,
                delay=1000
            )
            Utility.log_test_result("PASS", "Header remains visible after scrolling.")
            # 5. Refresh the page and verify header again.
            Utility.log_test_step("Refresh the page and observe the header again.")
            page.reload(timeout=timeout)
            Utility.wait_for_element_state(page, "body", state="visible", timeout=timeout)
            Utility.retry_assertion(
                lambda: expect(page.locator(header_selector)).to_be_visible(timeout=timeout),
                retries=3,
                delay=1000
            )
            header_text_after_refresh: str = Utility.get_element_text(page, header_selector, timeout=timeout)
            header_text_after_refresh = Utility.validate_and_convert_data(header_text_after_refresh, str)
            if header_text_after_refresh.strip() != "Simple Calculator":
                Utility.log_test_result("FAIL", f"Header text mismatch after refresh: '{header_text_after_refresh}'")
                raise AssertionError(f"Header text mismatch after refresh: '{header_text_after_refresh}'")
            Utility.log_test_result("PASS", "Header is visible and correct after refresh.")
            Utility.log_test_result("PASS", "TC-0001: Calculator title is displayed correctly on main page.")
        except AssertionError as ae:
            Utility.log_error(f"Assertion failed: {ae}")
            raise
        except Exception as e:
            Utility.log_error(f"Test failed due to unexpected error: {e}")
            raise
        finally:
            try:
                browser.close()
            except Exception as close_err:
                Utility.log_error(f"Error during browser cleanup: {close_err}")
#---#
#######
