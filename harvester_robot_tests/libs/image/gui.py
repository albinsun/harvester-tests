"""
Image GUI Implementation - Operates via Harvester GUI using Playwright
"""

import re
from utility.utility import get_harvester_gui_client
from utility.utility import get_retry_count_and_interval
from utility.utility import logging
from .base import Base
from constant import DEFAULT_NAMESPACE


class GUI(Base):
    """Image GUI implementation - Operates via Harvester GUI using Playwright"""

    def __init__(self):
        self.retry_count, self.retry_interval = get_retry_count_and_interval()
        self.b = get_harvester_gui_client()

    def create_from_url(self, image_name, image_url, checksum, **kwargs):
        """Create image from URL"""
        namespace = kwargs.get('namespace', DEFAULT_NAMESPACE)

        logging(f"Creating VirtualMachineImage {namespace}/{image_name}")
        self.b.page.get_by_role("link", name="Images").click()
        self.b.page.get_by_test_id("masthead-create").click()
        self.b.page.get_by_role("combobox", name="Search for option").click()
        self.b.page.get_by_test_id("name-ns-description-namespace").get_by_text(namespace).click()
        self.b.page.get_by_test_id("NameNsDescriptionNameInput").click()
        self.b.page.get_by_test_id("NameNsDescriptionNameInput").fill(image_name)
        self.b.page.get_by_role("textbox", name="URL").click()
        self.b.page.get_by_role("textbox", name="URL").fill(image_url)
        self.b.page.get_by_test_id("form-save").click()

    def wait_for_downloaded(self, image_name, timeout):
        """Wait for image to be downloaded"""
        self.b.page.get_by_role("cell", name="Age", exact=True).click()
        self.b.expect(
            self.b.page.get_by_test_id("sortable-table-0-row")
        ).to_contain_text(image_name)
        self.b.expect(
            self.b.page.get_by_test_id("sortable-cell-0-4")
        ).to_contain_text("Completed", timeout=timeout)
        self.b.expect(
            self.b.page.get_by_test_id("sortable-cell-0-0")
        ).to_contain_text("Active")

    def wait_for_ready(self, image_name, timeout):
        """Wait for image to be ready"""
        pass

    def delete(self, image_name, namespace):
        """Delete an image"""
        pass

    def wait_for_deleted(self, image_name, timeout):
        """Wait for image to be deleted"""
        pass

    def get_status(self, image_name, namespace):
        """Get image status"""
        pass

    def list(self, namespace):
        """List all images"""
        pass

    def exists(self, image_name, namespace):
        """Check if image exists"""
        pass

    def cleanup(self):
        """Clean up all test images"""
        self.b.page.get_by_role("link", name="Images").click()
        self.b.expect(
            self.b.page
        ).to_have_url(re.compile(".*/harvesterhci.io.virtualmachineimage"))

        self.b.page.get_by_test_id("sortable-table_check_select_all").locator("label").click()
        self.b.page.get_by_test_id("sortable-table-promptRemove").click()
        self.b.page.get_by_test_id("prompt-remove-confirm-button").click()
        self.b.expect(
            self.b.page.locator("td")
        ).to_contain_text("There are no rows to show.", timeout=30000)
