from setuptools import setup

setup(name='nutcracker',
      version='0.1.0',
      description='A collection of software tools for validation of flash xray imaging reconstructions packaged as a Python library.',
      url='https://github.com/FXIhub/nutcracker',
      author='Louis Doctor',
      author_email='doctor@xray.bmc.uu.se',
      license='BSD',
      package_dir={'nutcracker':'nutcracker'},
      package_data={'nutcracker':['data/test_data.h5',
                                 'data/test_data_rot_shift.h5',
                                  'data/test_quaternions.h5']},
      packages=['nutcracker',
                'nutcracker.utils',
                'nutcracker.tests'],
      entry_points={'console_scripts':[]},
      scripts=[],
      test_suite='nutcracker.tests.test_all')
