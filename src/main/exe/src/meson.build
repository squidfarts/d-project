###################################################################################
#                                                                                 #
# NAME: src/main/exe/src/meson.build                                              #
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


exe_dir = include_directories('.')

exe_src = [ 'project.d' ]


exe_lib = static_library('exe-lib', exe_src,
    #dependencies: [ ???_dep ],  
    include_directories: exe_dir,
    install: true)

exe_dep = declare_dependency(
    version: meson.project_version(),
    link_with: exe_lib,
    include_directories: exe_dir)