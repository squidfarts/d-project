#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: build.py                                                                  #
#                                                                                 #
# AUTHOR: Michael Brockus.                                                        #
#                                                                                 #
# CONTACT: <mailto:michael@squidfarts.com>                                        #
#                                                                                 #
# NOTICES:                                                                        #
#                                                                                 #
# License: Apache-2.0                                                             #
#                                                                                 #
###################################################################################
import subprocess, os

subprocess.check_call(["meson", "setup", "build_dir", "--backend=ninja"])
subprocess.check_call(["ninja", "-j8", "-C", "build_dir"])