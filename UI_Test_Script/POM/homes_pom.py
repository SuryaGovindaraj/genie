from playwright.sync_api import Page, Locator, expect, TimeoutError as PlaywrightTimeoutError

class GeneratedPage:
    """
    Page Object Model for the Dropdown Example page.
    """

    def __init__(self, page: Page, timeout: int = 5000):
        """
        Initializes the GeneratedPage with XPath locators for interactable elements.

        :param page: Playwright Page object.
        :param timeout: Timeout in milliseconds for element interactions.
        """
        self._page = page
        self._timeout = timeout

        self._select_topic_xpath = "//select[@id='mySelect']"

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
        Safely fills an input or textarea element specified by its XPath.

        :param xpath: XPath string of the element to fill.
        :param text: Text to input.
        """
        locator = self._page.locator(f"xpath={xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)
        locator.clear()
        locator.fill(text)

    def _safe_check(self, xpath: str):
        """
        Safely checks a checkbox or radio button specified by its XPath.

        :param xpath: XPath string of the element to check.
        """
        locator = self._page.locator(f"xpath={xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)
        if not locator.is_checked():
            locator.check()

    def _safe_select(self, xpath: str, value: str):
        """
        Safely selects an option in a <select> element specified by its XPath.

        :param xpath: XPath string of the select element.
        :param value: Value attribute of the option to select.
        """
        locator = self._page.locator(f"xpath={xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)
        locator.select_option(value)

    def select_topic(self, value: str):
        """
        Selects a topic from the dropdown by value.

        :param value: Value attribute of the option to select (e.g., 'html', 'css', 'javascript').
        """
        self._safe_select(self._select_topic_xpath, value)

    def validate_essential_elements(self):
        """
        Validates that essential elements are visible on the page.
        """
        locator = self._page.locator(f"xpath={self._select_topic_xpath}")
        expect(locator).to_be_visible(timeout=self._timeout)