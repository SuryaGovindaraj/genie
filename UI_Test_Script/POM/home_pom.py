from playwright.sync_api import Page, Locator, expect, TimeoutError as PlaywrightTimeoutError

class GeneratedPage:
    """
    Page Object Model for the Simple Calculator page.
    """

    def __init__(self, page: Page, timeout: int = 5000):
        """
        Initializes the GeneratedPage with XPath locators for interactable elements.

        :param page: Playwright Page object.
        :param timeout: Timeout in milliseconds for element interactions.
        """
        self._page = page
        self._timeout = timeout

        self._input_num1_xpath = "//input[@id='num1']"
        self._input_num2_xpath = "//input[@id='num2']"
        self._btn_add_xpath = "//button[normalize-space()='Add']"
        self._btn_subtract_xpath = "//button[normalize-space()='Subtract']"
        self._btn_multiply_xpath = "//button[normalize-space()='Multiply']"
        self._btn_divide_xpath = "//button[normalize-space()='Divide']"

    def _safe_click(self, xpath: str):
        """
        Safely clicks an element specified by its XPath.

        :param xpath: XPath string of the element to click.
        """
        locator = self._page.locator(f"xpath={xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)
        locator.click()

    def _safe_fill(self, xpath: str, text: str):
        """
        Safely fills an input field specified by its XPath.

        :param xpath: XPath string of the input element.
        :param text: Text to fill into the input.
        """
        locator = self._page.locator(f"xpath={xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)
        locator.clear()
        locator.fill(text)

    def _safe_check(self, xpath: str):
        """
        Safely checks a checkbox or radio button specified by its XPath.

        :param xpath: XPath string of the checkbox or radio element.
        """
        locator = self._page.locator(f"xpath={xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)
        if not locator.is_checked():
            locator.check()

    def _safe_select(self, xpath: str, value: str):
        """
        Safely selects an option in a select dropdown specified by its XPath.

        :param xpath: XPath string of the select element.
        :param value: Value attribute of the option to select.
        """
        locator = self._page.locator(f"xpath={xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)
        locator.select_option(value)

    def fill_num1_field(self, value: str):
        """
        Fills the first number input field.

        :param value: Value to enter in the Number 1 field.
        """
        self._safe_fill(self._input_num1_xpath, value)

    def fill_num2_field(self, value: str):
        """
        Fills the second number input field.

        :param value: Value to enter in the Number 2 field.
        """
        self._safe_fill(self._input_num2_xpath, value)

    def click_add_button(self):
        """
        Clicks the Add button.
        """
        self._safe_click(self._btn_add_xpath)

    def click_subtract_button(self):
        """
        Clicks the Subtract button.
        """
        self._safe_click(self._btn_subtract_xpath)

    def click_multiply_button(self):
        """
        Clicks the Multiply button.
        """
        self._safe_click(self._btn_multiply_xpath)

    def click_divide_button(self):
        """
        Clicks the Divide button.
        """
        self._safe_click(self._btn_divide_xpath)

    def validate_essential_elements(self):
        """
        Validates that all essential elements are visible on the page.
        """
        locator = self._page.locator(f"xpath={self._input_num1_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)

        locator = self._page.locator(f"xpath={self._input_num2_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)

        locator = self._page.locator(f"xpath={self._btn_add_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)

        locator = self._page.locator(f"xpath={self._btn_subtract_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)

        locator = self._page.locator(f"xpath={self._btn_multiply_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)

        locator = self._page.locator(f"xpath={self._btn_divide_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)