""" Setting Component

Layer 4: Component and its implementation
"""

import os
from constant import HarvesterOperationStrategy
from utility.utility import logging
from .base import Base
from .crd import CRD
from .rest import Rest



class Setting(Base):
    def __init__(self):
        self.crd = CRD()
        self.rest = Rest()

    def get(self, setting_id):
        """Get setting details - delegates to implementation"""
        # if self.strategy == "crd":
        #     return self.crd.enable(setting_id)
        # elif self.strategy == "rest":
        #     return self.rest.enable(setting_id)

        try:
            return self.crd.get(setting_id)
        except NotImplementedError as e:
            logging(e)
            return self.rest.get(setting_id)

    def enable(self, setting_id):
        """Enable a setting - delegates to implementation"""
        try:
            return self.crd.enable(setting_id)
        except NotImplementedError as e:
            logging(e)
            return self.rest.enable(setting_id)
