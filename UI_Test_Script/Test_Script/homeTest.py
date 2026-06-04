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
    "counter_app": os.environ.get("COUNTER_APP_URL", "http://localhost:3000")
}
def test_counter_value_increases_when_plus_button_is_clicked() -> None:
    """
    TC-0001: Counter Value Increases When Plus Button Is Clicked
    1. This test verifies that clicking the plus button increases the counter value by one each time and that the UI updates accordingly.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        page.on("console", lambda msg: Utility.log_console_message(msg))
        test_result: str = "PASSED"
        test_details: str = ""
        try:
            # Given: Navigate to Counter App main page
            Utility.log_test_step("Navigating to Counter App main page.")
            navigation_success: bool = Utility.navigate_to_page(page, urls["counter_app"], timeout=15000)
            if not navigation_success:
                raise Exception("Navigation to Counter App failed.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            Utility.log_test_step("Validating essential elements are visible.")
            generated_page.validate_essential_elements()
            Utility.log_element_state("Decrease Button", page.locator(f"xpath={generated_page._btn_decrease_xpath}"))
            Utility.log_element_state("Increase Button", page.locator(f"xpath={generated_page._btn_increase_xpath}"))
            Utility.log_element_state("Reset Button", page.locator(f"xpath={generated_page._btn_reset_xpath}"))
            # Accept cookies/pop-ups if present
            Utility.safe_wait_and_interact(page, "text=Accept", "click", timeout=5000)
            # When: Verify header and initial counter value
            Utility.log_test_step("Verifying header 'Counter App' is present.")
            header_selector: str = "xpath=//h1[normalize-space()='Counter App']"
            header_text: str = Utility.get_element_text(page, header_selector, timeout=15000)
            header_text = Utility.validate_and_convert_data(header_text, str)
            if header_text.strip() != "Counter App":
                raise AssertionError("Header 'Counter App' not found or incorrect.")
            Utility.log_test_step("Verifying initial counter value is 0.")
            counter_selector: str = "xpath=//span[contains(@class,'counter-value')]"
            counter_value: str = Utility.get_element_text(page, counter_selector, timeout=15000)
            counter_value_int: int = Utility.validate_and_convert_data(counter_value, int)
            if counter_value_int != 0:
                raise AssertionError(f"Expected counter value 0, got {counter_value_int}")
            # Then: Plus button is visible and enabled
            Utility.log_test_step("Verifying plus (+) button is visible and enabled.")
            plus_btn_locator = page.locator(f"xpath={generated_page._btn_increase_xpath}")
            Utility.log_element_state("Plus Button", plus_btn_locator)
            expect(plus_btn_locator).to_be_enabled(timeout=15000)
            # When: Click plus button once
            Utility.log_test_step("Clicking plus (+) button once.")
            generated_page.click_increase_button()
            Utility.retry_assertion(
                lambda: expect(page.locator(counter_selector)).to_have_text("1", timeout=15000),
                retries=3,
                delay=1000
            )
            counter_value = Utility.get_element_text(page, counter_selector, timeout=15000)
            counter_value_int = Utility.validate_and_convert_data(counter_value, int)
            if counter_value_int != 1:
                raise AssertionError(f"Expected counter value 1, got {counter_value_int}")
            # When: Click plus button again
            Utility.log_test_step("Clicking plus (+) button a second time.")
            generated_page.click_increase_button()
            Utility.retry_assertion(
                lambda: expect(page.locator(counter_selector)).to_have_text("2", timeout=15000),
                retries=3,
                delay=1000
            )
            counter_value = Utility.get_element_text(page, counter_selector, timeout=15000)
            counter_value_int = Utility.validate_and_convert_data(counter_value, int)
            if counter_value_int != 2:
                raise AssertionError(f"Expected counter value 2, got {counter_value_int}")
            # When: Click plus button a third time
            Utility.log_test_step("Clicking plus (+) button a third time.")
            generated_page.click_increase_button()
            Utility.retry_assertion(
                lambda: expect(page.locator(counter_selector)).to_have_text("3", timeout=15000),
                retries=3,
                delay=1000
            )
            counter_value = Utility.get_element_text(page, counter_selector, timeout=15000)
            counter_value_int = Utility.validate_and_convert_data(counter_value, int)
            if counter_value_int != 3:
                raise AssertionError(f"Expected counter value 3, got {counter_value_int}")
            # Then: Counter display always shows correct incremented value
            Utility.log_test_step("Verifying counter display increments correctly after each click.")
            for expected_value in [1, 2, 3]:
                Utility.retry_assertion(
                    lambda: expect(page.locator(counter_selector)).to_have_text(str(expected_value), timeout=15000),
                    retries=3,
                    delay=1000
                )
            # Then: Plus button remains enabled after multiple clicks
            Utility.log_test_step("Verifying plus (+) button remains enabled after multiple clicks.")
            expect(plus_btn_locator).to_be_enabled(timeout=15000)
            Utility.log_test_result("PASSED", "Counter increments and UI updates as expected.")
        except AssertionError as ae:
            test_result = "FAILED"
            test_details = f"Assertion failed: {ae}"
            Utility.log_error(test_details)
            raise
        except Exception as e:
            test_result = "FAILED"
            test_details = f"Test failed: {e}"
            Utility.log_error(test_details)
            raise
        finally:
            Utility.log_test_result(test_result, test_details)
            browser.close()
#---#
#######
