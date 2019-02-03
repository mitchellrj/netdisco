"""Discover Sky devices."""
from . import SSDPDiscoverable


class Discoverable(SSDPDiscoverable):
    """Sky+ HD or Sky Q boxes."""

    def get_entries(self):
        """Get all the Sky uPnP entries specific to media playback."""
        return self.find_by_st("urn:schemas-nds-com:service:SkyPlay:2")
