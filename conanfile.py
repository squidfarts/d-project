#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: conanfile.py                                                              #
#                                                                                 #
# AUTHOR: Michael Brockus.                                                        #
#                                                                                 #
# CONTACT: <mailto:michael@squidfarts.com>                                        #
#                                                                                 #
# NOTICES:                                                                        #
#                                                                                 #
# License: Apache 2.0 :http://www.apache.org/licenses/LICENSE-2.0                 #
#                                                                                 #
###################################################################################
from conans import ConanFile, tools, Meson
from os.path import join as join_paths
import sys

if sys.version_info[0] < 3:
    raise Exception("The version of Python must be 3 or greater.")



class MesonProject(ConanFile):
    generators = 'pkg_config'
    settings = 'os', 'compiler', 'build_type', 'arch'
    topics = ('conan', 'meson', 'mesonbuild', 'build-system', 'c++14')
                
    def build(self):
        meson = Meson(self)
        meson.configure()
        meson.build()
    # end of method build

# end of class MesonProject
