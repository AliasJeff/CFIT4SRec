# Only ship imports for modules that actually exist in this fork. The
# upstream cl4srec.py / duorec.py sources were removed from the release but
# their stale imports here used to break the whole package on fresh
# machines (ModuleNotFoundError at import time). cfit4srec.py is
# self-contained and is resolved dynamically by RecBole's model loader.
