###################################################################################
#                                                                                 #
# NAME: src/main/dlang/meson.build                                                #
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



subdir('src')

exe_main = executable(meson.project_name(), 'main.d',
    dependencies: [ exe_dep ],
    install: true)

test('Test exe', exe_main)