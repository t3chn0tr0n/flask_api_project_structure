"""
    Config Selector
    There are three type of configs:
        1. Development : `__dev.py` (default)
        2. Testing : `__test.py`
        3. Production : `__pro.py` 
    CHOOSE CONFIG CAREFULLY: ONLY 1 SHOULD BE ACTIVE AT A TIME
"""

# FOR DEVELOPMENT
from .__dev import *

# FOR TESTING
# from .__test import *

# FOR PRODUCTION
# from .pro import *