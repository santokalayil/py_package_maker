print("The library py_package_maker is importable")

from .templates import license, readme, setup, package_dir_n_init

license.create_license_file()
readme.create_readme_file()
setup.create_setup_py_file()
package_dir_n_init.create_src_dir_n_init_file()

