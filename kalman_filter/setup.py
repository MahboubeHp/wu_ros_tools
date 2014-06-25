from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

package_info = generate_distutils_setup(
    packages=['kalman_filter'],
    package_dir={'': 'src'},
)

setup(**package_info)
