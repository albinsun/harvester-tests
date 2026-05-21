""" Setting Component: REST Implementation

Layer 4: Component and its implementation
"""

from utility.utility import get_harvester_api_client
from .base import Base


class Rest(Base):
    """REST implementation for Setting operations using Harvester API"""

    def __init__(self):
        super().__init__()
        self.api_client = get_harvester_api_client()
        self.port_forward_process = None

    def get(self, setting_id):
        try:
            code, data = self.api_client.get(
                f"v1/harvester/harvesterhci.io.settings/{setting_id}"
            )
            if code != 200:
                raise Exception(f"Failed to get setting {setting_id}: {code}, {data}")
            return data
        except Exception as e:
            raise Exception(f"Failed to get setting {setting_id}: {e}")
        # return super().get(setting_id)

    def enable(self, setting_id):
        try:
            payload = self.get(setting_id)
            payload["value"] = "true"
            code, data = self.api_client.put(
                f"v1/harvester/harvesterhci.io.settings/{setting_id}",
                data=payload
            )
            if code not in [200, 201]:
                raise Exception(f"Failed to enable setting {setting_id}: {code}, {data}")
        except Exception as e:
            raise Exception(f"Failed to enable setting {setting_id}: {e}")
        # return super().enable(setting_id)
