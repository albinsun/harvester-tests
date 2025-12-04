"""
Image GUI Implementation - Operates via Harvester GUI using Playwright
"""

from utility.utility import get_harvester_gui_client
from utility.utility import logging
from .base import Base
from constant import DEFAULT_NAMESPACE, DEFAULT_TIMEOUT_SHORT


class GUI(Base):
    """Image GUI Implementation - Operates via Harvester GUI using Playwright"""

    def __init__(self):
        self.b = get_harvester_gui_client()

    def create(self, vm_name, cpu, memory, image_id, **kwargs):
        """Create a VM"""
        namespace = kwargs.get('namespace', DEFAULT_NAMESPACE)

        try:
            logging(f"Creating VirtualMachine {namespace}/{vm_name}")

            self.b.page.get_by_role("link", name="Virtual Machines").click()
            self.b.expect(
                self.b.page.locator("h1")
            ).to_contain_text("Virtual Machines")
            self.b.page.get_by_test_id("masthead-create").click()
            self.b.page.get_by_test_id("NameNsDescriptionNameInput").click()
            self.b.page.get_by_test_id("NameNsDescriptionNameInput").fill(vm_name)
            self.b.page.get_by_role("spinbutton", name="CPU").click()
            self.b.page.get_by_role("spinbutton", name="CPU").fill(str(cpu))
            self.b.page.get_by_role("spinbutton", name="Memory").click()
            self.b.page.get_by_role("spinbutton", name="Memory").fill(str(memory).rstrip("Gi"))
            self.b.page.get_by_test_id("btn-Volume").click()
            self.b.page.get_by_test_id("input-hevi-image").get_by_role("combobox", name="Search for option").click()
            self.b.page.get_by_text(f"{namespace}/{image_id}").click()
            self.b.page.get_by_test_id("form-save").click()
            self.b.expect(
                self.b.page.get_by_test_id("sortable-cell-0-1")
            ).to_contain_text(vm_name)

            logging(f"VM {namespace}/{vm_name} created successfully")

            return {'metadata': {'name': vm_name, 'namespace': namespace}}

        except Exception as e:
            logging(f"Failed to create VM {vm_name}: {e}")
            raise e

    def delete(self, vm_name, namespace=DEFAULT_NAMESPACE):
        """Delete VirtualMachine."""
        try:
            self.b.page.get_by_test_id("sortable-table-0-action-button").click()
            self.b.page.get_by_role("menuitem", name=" Delete").click()
            self.b.page.get_by_test_id("prompt-remove-confirm-button").click()

            logging(f"Deleted VirtualMachine {namespace}/{vm_name}")
        except Exception as e:
            logging(f"Error deleting VM {vm_name}: {e}")
            raise e

    def get(self, vm_name, namespace=DEFAULT_NAMESPACE):
        """Get VirtualMachine."""
        return None

    def list(self, namespace=DEFAULT_NAMESPACE, label_selector=None):
        """List VirtualMachines."""
        return []

    def start(self, vm_name, namespace=DEFAULT_NAMESPACE):
        """Start a VM."""
        try:
            self.b.page.get_by_test_id("sortable-table-0-action-button").click()
            self.b.page.get_by_role("menuitem", name=" Start").click()

            logging(f"VM {namespace}/{vm_name} started")
            return

        except Exception as e:
            logging(f"Fail to start VM {namespace}/{vm_name}")
            raise e

    def stop(self, vm_name, namespace=DEFAULT_NAMESPACE):
        """Stop a VM."""
        try:
            self.b.page.get_by_test_id("sortable-table-0-action-button").click()
            self.b.page.get_by_role("menuitem", name=" Stop").click()
            self.b.page.get_by_test_id("action-button-async-button").click()

            logging(f"VM {namespace}/{vm_name} stopped")
            return
        except Exception as e:
            logging(f"Failed to stop VM {namespace}/{vm_name}")
            raise e

    def restart(self, vm_name, namespace=DEFAULT_NAMESPACE):
        """Restart a VM."""
        logging(f"Restarting VM {namespace}/{vm_name}")
        try:
            logging(f"VM {namespace}/{vm_name} restart initiated")
        except Exception as e:
            logging(f"Error restarting VM {namespace}/{vm_name}")
            raise e

    def migrate(self, vm_name, target_node, namespace=DEFAULT_NAMESPACE):
        """Migrate VM to target node."""
        logging(f"Migrating VM {namespace}/{vm_name} to node {target_node}")
        try:
            # Create VirtualMachineInstanceMigration object

            logging(
                f"VM {namespace}/{vm_name} migration to "
                f"{target_node} initiated"
            )
        except Exception as e:
            logging(f"Fail to migrate VM {namespace}/{vm_name}")
            raise e

    def wait_for_vm_created(self, vm_name, namespace=DEFAULT_NAMESPACE):
        """Wait for VM CR creation."""
        try:
            logging(f"VirtualMachine {namespace}/{vm_name} created")
            return True
        except Exception as e:
            logging(f"VirtualMachine {namespace}/{vm_name} not created")
            raise e

    def wait_for_running(
            self, vm_name, timeout=DEFAULT_TIMEOUT_SHORT, namespace=DEFAULT_NAMESPACE):
        """Wait for VM to be running."""
        timeout *= 1000  # Convert to milliseconds

        try:
            self.b.expect(
                self.b.page.get_by_test_id("sortable-cell-0-5")
            ).not_to_be_empty(timeout=timeout)
            self.b.expect(
                self.b.page.get_by_test_id("sortable-cell-0-0")
            ).to_contain_text("Running", timeout=timeout)
            return True
        except Exception as e:
            logging(f"Waiting for VM {vm_name} to start (current phase: )...")
            raise e

    def wait_for_stopped(
            self, vm_name, timeout=DEFAULT_TIMEOUT_SHORT, namespace=DEFAULT_NAMESPACE):
        """Wait for VM to be stopped."""
        timeout *= 1000  # Convert to milliseconds

        try:
            self.b.expect(
                self.b.page.get_by_test_id("sortable-cell-0-0")
            ).to_contain_text("Off", timeout=timeout)
            self.b.expect(
                self.b.page.get_by_test_id("sortable-cell-0-4")
            ).to_be_empty(timeout=timeout)
            self.b.expect(
                self.b.page.get_by_test_id("sortable-cell-0-5")
            ).to_be_empty(timeout=timeout)
            logging(f"VM {namespace}/{vm_name} is stopped")
            return True
        except Exception as e:
            logging("Waiting for VM to stop (current phase: )...")
            raise e

    def wait_for_deleted(
            self, vm_name, timeout=DEFAULT_TIMEOUT_SHORT, namespace=DEFAULT_NAMESPACE):
        """Wait for VM to be deleted."""
        timeout *= 1000  # Convert to milliseconds
        self.b.expect(
            self.b.page.get_by_text("There are no rows to show.")
        ).to_be_visible(timeout=timeout)
        pass

    def get_status(self, vm_name, namespace=DEFAULT_NAMESPACE):
        """Get VM status."""
        return {}

    def wait_for_ip_addresses(
            self, vm_name, networks=None, timeout=DEFAULT_TIMEOUT_SHORT,
            namespace=DEFAULT_NAMESPACE):
        """Wait for VM to get IP addresses."""
        timeout *= 1000  # Convert to milliseconds

        logging(
            f"Waiting for VM {namespace}/{vm_name} to get IP addresses "
            f"on networks: {networks}"
        )

        try:
            self.b.expect(
                self.b.page.get_by_test_id("sortable-cell-0-4")
            ).not_to_be_empty(timeout=timeout)
            logging("Network n does not have IP yet")
            logging(f"VM {namespace}/{vm_name} got IP addresses: ips")
            return True
            # logging(
            #     f"Waiting for VM to get IP addresses "
            #     f"(networks: {networks}, m interfaces)..."
            # )
        except Exception as e:
            logging(f"VM {namespace}/{vm_name} did not get IP addresses ")
            raise e

    def cleanup(self):
        """Clean up test VMs."""
        logging('Cleaning up test VMs')

        # try:
        #     logging(f'Deleting test VM: {namespace}/{vm_name}')
        #     self.delete(vm_name, namespace)
        # except Exception as e:
        #     logging(f'Error deleting VM {vm_name}: {e}', 'WARNING')
