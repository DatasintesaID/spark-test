from .s1SignalSuccess import s1_signal_success
from .rrcSetupSuccess import rrc_setup_success
from .erabSetupSuccess import erab_setup_success


def accessibility(counters, duration):
    return s1_signal_success(counters, duration) + rrc_setup_success(counters, duration) + erab_setup_success(counters, duration)
