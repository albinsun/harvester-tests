"""
Image Component - delegates to Rest implementation
"""
from constant import HarvesterOperationStrategy
from image.crd import CRD
from image.gui import GUI
from image.rest import Rest
from robot.libraries.BuiltIn import BuiltIn


class Image:
    """Image component - delegates to Rest implementation"""
    def __init__(self):
        op_strategy = BuiltIn().get_variable_value("${OPERATION_STRATEGY}")

        if op_strategy == HarvesterOperationStrategy.CRD.value:
            self.image = CRD()
        elif op_strategy == HarvesterOperationStrategy.REST.value:
            self.image = Rest()
        elif op_strategy == HarvesterOperationStrategy.GUI.value:
            self.image = GUI()
        else:
            BuiltIn().fatal_error(f"Unexpected HARVESTER_OPERATION_STRATEGY: {op_strategy}")

    def create_from_url(self, image_name, image_url, checksum, **kwargs):
        return self.image.create_from_url(image_name, image_url, checksum, **kwargs)

    def wait_for_downloaded(self, image_name, timeout):
        return self.image.wait_for_downloaded(image_name, timeout)

    def wait_for_ready(self, image_name, timeout):
        return self.image.wait_for_ready(image_name, timeout)

    def delete(self, image_name, namespace):
        return self.image.delete(image_name, namespace)

    def wait_for_deleted(self, image_name, timeout):
        return self.image.wait_for_deleted(image_name, timeout)

    def get_status(self, image_name, namespace):
        return self.image.get_status(image_name, namespace)

    def list(self, namespace):
        return self.image.list(namespace)

    def exists(self, image_name, namespace):
        return self.image.exists(image_name, namespace)

    def cleanup(self):
        return self.image.cleanup()
