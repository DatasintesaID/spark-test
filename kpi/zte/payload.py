from .dlPayload import dl_payload
from .ulPayload import ul_payload


def payload(counters, duration):
    return ul_payload(counters, duration) + dl_payload(counters, duration)
