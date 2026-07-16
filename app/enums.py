from enum import Enum


class NodeStatus(Enum):
    ONLINE = "online"
    OFFLINE = "offline"
    MAINTENANCE = "maintenance"


class Cluster(Enum):
    NORTH_AMERICA = "North America"
    EUROPE = "Europe"
    MIDDLE_EAST = "Middle East"
    SEA = "Southeast Asia"
    SOUTH_AMERICA = "South America"
    AFRICA = "Africa"


class ChunkStatus(Enum):
    PENDING = "pending"
    UPLOADING = "uploading"
    COMPLETED = "completed"
    FAILED = "failed"


class PermissionLevel(Enum):
    OWNER = "owner"
    WRITE = "write"
    READ = "read"
