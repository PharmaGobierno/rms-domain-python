from enum import Enum


class OrderTypes(str, Enum):
    REMISSION = "REMISSION"


class RemissionPodEvents(str, Enum):
    CREATED = "CREATED"
    TRANSPORT_ARRIVAL = "TRANSPORT_ARRIVAL"
    PODS_SUBMITTED = "PODS_SUBMITTED"
    IA_REVIEWED = "IA_REVIEWED"
    VALIDATOR_REVIEWED = "VALIDATOR_REVIEWED"
    DELIVERY_ACCEPTED = "DELIVERY_ACCEPTED"
    PHYSICAL_SCANNED = "PHYSICAL_SCANNED"


class FileType(str, Enum):
    pass


class DocumentName(str, Enum):
    pass
