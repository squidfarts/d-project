#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: install.py                                                                #
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
import subprocess
import sys, os

subprocess.check_call(["pip3", "install", "meson==0.50.0", "conan==1.19.0"])
subprocess.check_call(["mkdir", ".ntmp"])
subprocess.check_call(["curl", "-L", "https://github.com/ninja-build/ninja/releases/download/v1.8.2/ninja-linux.zip", "-o", ".ntmp/ninja-linux.zip"])
subprocess.check_call(["unzip", ".ntmp/ninja-linux.zip", "-d", ".ntmp"])