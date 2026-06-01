# Generated Playwright Tests for homes
from playwright.sync_api import sync_playwright, expect, TimeoutError as PlaywrightTimeoutError
from homes_pom import GeneratedPage
import json
import re
import time
import os

urls = {}
from Utility import Utility


# Test Case 1 - TC-0001
from playwright.sync_api import sync_playwright, expect
  # Import the POM class
# Global URLs dictionary (update with actual URL)
def test_topic_description_displayed_on_valid_selection() -> None:
    """
    TC-0001: Topic Description Is Displayed When a Valid Option Is Selected
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            ignore_https_errors=True
        )
        page = context.new_page()
        generated_page = GeneratedPage(page)
        page.on("console", Utility.log_console_message)
        test_result = "PASSED"
        test_details = ""
        try:
            # Given: Navigate to the main page and accept cookies/pop-ups if present
            Utility.log_test_step("Navigating to the main page.")
            navigation_success = Utility.navigate_to_page(page, urls["main_page"], timeout=15000)
            if not navigation_success:
                raise Exception("Navigation to main page failed.")
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            # Accept cookies/pop-ups if present
            Utility.safe_wait_and_interact(page, "button:has-text('Accept')", "click", timeout=5000)
            Utility.log_test_step("Validating essential elements on the page.")
            generated_page.validate_essential_elements()
            Utility.log_element_state("Topic Dropdown", page.locator("xpath=//select[@id='mySelect']"), timeout=15000)
            # Then: Verify heading and dropdown label
            Utility.log_test_step("Verifying heading and dropdown label.")
            heading_text = Utility.get_element_text(page, "xpath=//h1", timeout=15000)
            heading_text = Utility.validate_and_convert_data(heading_text, str)
            if heading_text.strip() != "Select a Topic":
                raise AssertionError(f"Expected heading 'Select a Topic', got '{heading_text.strip()}'")
            dropdown_text = Utility.get_element_text(page, "xpath=//select[@id='mySelect']/option[1]", timeout=15000)
            dropdown_text = Utility.validate_and_convert_data(dropdown_text, str)
            if dropdown_text.strip() != "-- Choose an option --":
                raise AssertionError(f"Expected dropdown label '-- Choose an option --', got '{dropdown_text.strip()}'")
            # When: Observe dropdown menu options
            Utility.log_test_step("Verifying dropdown options.")
            options = []
            for i in range(2, 5):
                option_text = Utility.get_element_text(page, f"xpath=//select[@id='mySelect']/option[{i}]", timeout=15000)
                option_text = Utility.validate_and_convert_data(option_text, str)
                options.append(option_text.strip())
            expected_options = ["HTML", "CSS", "JavaScript"]
            if options != expected_options:
                raise AssertionError(f"Dropdown options mismatch. Expected {expected_options}, got {options}")
            # When: Click dropdown to expand (visual, no action needed as select is always visible)
            Utility.log_test_step("Selecting 'HTML' from dropdown.")
            generated_page.select_topic("html")
            # Then: Verify 'HTML' is selected and correct description is shown
            Utility.retry_assertion(
                lambda: expect(page.locator("xpath=//select[@id='mySelect']")).to_have_value("html", timeout=15000),
                retries=3, delay=1000
            )
            Utility.log_test_step("Verifying description for 'HTML'.")
            html_desc = Utility.get_element_text(page, "xpath=//div[@id='result']", timeout=15000)
            html_desc = Utility.validate_and_convert_data(html_desc, str)
            if html_desc.strip() != "HTML is used to create the structure of web pages.":
                raise AssertionError("Incorrect description for HTML.")
            # When: Refresh and repeat for 'CSS'
            Utility.log_test_step("Refreshing page and selecting 'CSS'.")
            page.reload()
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            generated_page.validate_essential_elements()
            generated_page.select_topic("css")
            Utility.retry_assertion(
                lambda: expect(page.locator("xpath=//select[@id='mySelect']")).to_have_value("css", timeout=15000),
                retries=3, delay=1000
            )
            css_desc = Utility.get_element_text(page, "xpath=//div[@id='result']", timeout=15000)
            css_desc = Utility.validate_and_convert_data(css_desc, str)
            if css_desc.strip() != "CSS is used for styling web pages.":
                raise AssertionError("Incorrect description for CSS.")
            # When: Refresh and repeat for 'JavaScript'
            Utility.log_test_step("Refreshing page and selecting 'JavaScript'.")
            page.reload()
            Utility.wait_for_element_state(page, "body", state="visible", timeout=15000)
            generated_page.validate_essential_elements()
            generated_page.select_topic("javascript")
            Utility.retry_assertion(
                lambda: expect(page.locator("xpath=//select[@id='mySelect']")).to_have_value("javascript", timeout=15000),
                retries=3, delay=1000
            )
            js_desc = Utility.get_element_text(page, "xpath=//div[@id='result']", timeout=15000)
            js_desc = Utility.validate_and_convert_data(js_desc, str)
            if js_desc.strip() != "JavaScript is used to add interactivity to web pages.":
                raise AssertionError("Incorrect description for JavaScript.")
            test_details = "All topic descriptions displayed correctly."
            Utility.log_test_result(test_result, test_details)
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
