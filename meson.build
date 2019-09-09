###################################################################################
#                                                                                 #
# NAME: meson.build                                                               #
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



project('d-exe', 'd',
    version         : '0.1.0',
    license         : 'Apache-2.0',
    meson_version   : '>=0.50.0',
    default_options : 
    [
        'buildtype=release',
        'b_lundef=true',
        'werror=true',
        'optimization=3',
        'warning_level=3'
    ]
)

subdir('src')

install_data(
    sources: [ 'code_of_conduct.md', 'contributing.md', 'LICENSE', 'readme.md' ],
    install_dir: join_paths(get_option('datadir'), meson.project_name()))