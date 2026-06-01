# Generated Playwright Tests for index
from playwright.sync_api import sync_playwright, expect, TimeoutError as PlaywrightTimeoutError
from index_pom import GeneratedPage
import json
import re
import time
import os

urls = {}
from Utility import Utility


# Test Case 1 - TC-0001
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
def test_topic_description_displayed_on_valid_selection() -> None:
    """
    TC-0001: Topic Description Is Displayed When a Valid Option Is Selected
    This test verifies that selecting each valid topic from the dropdown displays
    the correct description in the result area, ensuring the dropdown and dynamic
    text update work as intended.
    """
    # --- Test Data and URLs ---
    urls: dict[str, str] = {
        "main": os.environ.get("TOPIC_DROPDOWN_URL", "http://localhost:8000/")
    }
    expected_header: str = "Select a Topic"
    expected_dropdown_label: str = "-- Choose an option --"
    expected_options: dict[str, str] = {
        "html": "HTML is used to create the structure of web pages.",
        "css": "CSS is used to style web pages and make them attractive.",
        "javascript": "JavaScript is used to add interactivity and dynamic behavior to web pages."
    }
    dropdown_value_map: dict[str, str] = {
        "HTML": "html",
        "CSS": "css",
        "JavaScript": "javascript"
    }
    # --- Begin Playwright Test ---
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        # --- Enhanced Console and Dialog Handling ---
        page.on("console", lambda msg: Utility.log_console_message(msg))
        try:
            # --- Given: Navigate to main page and accept cookies/pop-ups if present ---
            Utility.log_test_step("Navigating to the main page.")
            navigation_success: bool = Utility.navigate_to_page(page, urls["main"], timeout=15000)
            if not navigation_success:
                Utility.log_error("Navigation to main page failed.")
                raise Exception("Navigation to main page failed.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            # Accept cookies/pop-ups if present
            Utility.safe_wait_and_interact(page, "button:has-text('Accept')", "click", timeout=5000)
            # --- Then: Validate essential elements are visible ---
            Utility.log_test_step("Validating essential elements on the page.")
            generated_page.validate_essential_elements()
            # --- Given: Verify header and dropdown label ---
            Utility.log_test_step("Verifying header and dropdown label.")
            header_selector: str = "//h1"
            dropdown_selector: str = generated_page._select_topic_xpath
            header_text: str = Utility.get_element_text(page, header_selector, timeout=15000)
            header_text = Utility.validate_and_convert_data(header_text, str)
            if header_text.strip() != expected_header:
                Utility.log_error(f"Header mismatch: '{header_text}' != '{expected_header}'")
                raise AssertionError(f"Header mismatch: '{header_text}' != '{expected_header}'")
            dropdown_label_selector: str = f"{dropdown_selector}/option[1]"
            dropdown_label_text: str = Utility.get_element_text(page, dropdown_label_selector, timeout=15000)
            dropdown_label_text = Utility.validate_and_convert_data(dropdown_label_text, str)
            if dropdown_label_text.strip() != expected_dropdown_label:
                Utility.log_error(f"Dropdown label mismatch: '{dropdown_label_text}' != '{expected_dropdown_label}'")
                raise AssertionError(f"Dropdown label mismatch: '{dropdown_label_text}' != '{expected_dropdown_label}'")
            # --- When: Observe dropdown options ---
            Utility.log_test_step("Observing dropdown options.")
            for idx, (option_key, _) in enumerate(expected_options.items(), start=2):
                option_selector: str = f"{dropdown_selector}/option[{idx}]"
                option_text: str = Utility.get_element_text(page, option_selector, timeout=15000)
                option_text = Utility.validate_and_convert_data(option_text, str)
                if option_text.strip() not in dropdown_value_map:
                    Utility.log_error(f"Dropdown option '{option_text}' not found in expected options.")
                    raise AssertionError(f"Dropdown option '{option_text}' not found in expected options.")
            # --- When: Click dropdown to expand ---
            Utility.log_test_step("Clicking dropdown to expand options.")
            Utility.safe_wait_and_interact(page, dropdown_selector, "click", timeout=15000)
            Utility.wait_for_element_state(page, dropdown_selector, state="visible", timeout=15000)
            # --- When: Select "HTML" option ---
            Utility.log_test_step("Selecting 'HTML' option from dropdown.")
            generated_page.select_topic("html")
            # --- Then: Verify "HTML" description is displayed ---
            Utility.log_test_step("Verifying 'HTML' description is displayed.")
            def assert_html_description() -> None:
                result_selector: str = "//div[@id='result']"
                result_text: str = Utility.get_element_text(page, result_selector, timeout=15000)
                result_text = Utility.validate_and_convert_data(result_text, str)
                if result_text.strip() != expected_options["html"]:
                    raise AssertionError(f"Expected '{expected_options['html']}', got '{result_text.strip()}'")
            Utility.retry_assertion(assert_html_description, retries=3, delay=1000)
            # --- When: Change selection to "CSS" ---
            Utility.log_test_step("Selecting 'CSS' option from dropdown.")
            generated_page.select_topic("css")
            # --- Then: Verify "CSS" description is displayed ---
            Utility.log_test_step("Verifying 'CSS' description is displayed.")
            def assert_css_description() -> None:
                result_selector: str = "//div[@id='result']"
                result_text: str = Utility.get_element_text(page, result_selector, timeout=15000)
                result_text = Utility.validate_and_convert_data(result_text, str)
                if result_text.strip() != expected_options["css"]:
                    raise AssertionError(f"Expected '{expected_options['css']}', got '{result_text.strip()}'")
            Utility.retry_assertion(assert_css_description, retries=3, delay=1000)
            # --- When: Change selection to "JavaScript" ---
            Utility.log_test_step("Selecting 'JavaScript' option from dropdown.")
            generated_page.select_topic("javascript")
            # --- Then: Verify "JavaScript" description is displayed ---
            Utility.log_test_step("Verifying 'JavaScript' description is displayed.")
            def assert_js_description() -> None:
                result_selector: str = "//div[@id='result']"
                result_text: str = Utility.get_element_text(page, result_selector, timeout=15000)
                result_text = Utility.validate_and_convert_data(result_text, str)
                if result_text.strip() != expected_options["javascript"]:
                    raise AssertionError(f"Expected '{expected_options['javascript']}', got '{result_text.strip()}'")
            Utility.retry_assertion(assert_js_description, retries=3, delay=1000)
            Utility.log_test_result("PASS", "All topic descriptions displayed as expected.")
        except AssertionError as ae:
            Utility.log_test_result("FAIL", f"Assertion failed: {ae}")
            raise
        except Exception as e:
            Utility.log_test_result("FAIL", f"Test failed: {e}")
            raise
        finally:
            browser.close()
#---#
#######
