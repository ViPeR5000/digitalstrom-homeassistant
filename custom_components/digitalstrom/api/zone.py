from .apartment import DigitalstromApartment
from .client import DigitalstromClient


class DigitalstromZone:
    def __init__(
        self, client: DigitalstromClient, apartment: DigitalstromApartment, zone_id: int
    ):
        self.client = client
        self.zone_id = zone_id
        self.apartment = apartment
        self.name = ""
        self.group_ids = []

    async def call_scene(self, scene: int) -> None:
        await self.client.request(
            f"zone/callScene?id={self.zone_id}&sceneNumber={scene}"
        )

    async def undo_scene(self, scene: int) -> None:
        await self.client.request(
            f"zone/undoScene?id={self.zone_id}&sceneNumber={scene}"
        )

    def load_from_dict(self, data: dict) -> None:
        if "zoneID" in data:
            zone_id = int(data["zoneID"])
            if zone_id == self.zone_id:
                if (name := data.get("name")) and (len(name) > 0):
                    self.name = name
                if (group_ids := data.get("groups")) and (len(group_ids) > 0):
                    self.group_ids = group_ids