from django import models


class NodeStatus(models.TextChoices):
    ONLINE = "online", "Online"
    OFFLINE = "offline", "Offline"
    MAINTENANCE = "maintenance", "Maintenance"


class Cluster(models.TextChoices):
    NORTH_AMERICA = "North America", "North America"
    EUROPE = "Europe", "Europe"
    MIDDLE_EAST = "Middle East", "Middle East"
    SEA = "Southeast Asia", "Southeast Asia"
    SOUTH_AMERICA = "South America", "South America"
    AFRICA = "Africa", "Africa"


class ChunkStatus(models.TextChoices):
    PENDING = "pending", "Pending"
    UPLOADING = "uploading", "Uploading"
    COMPLETED = "completed", "Completed"
    FAILED = "failed", "Failed"
