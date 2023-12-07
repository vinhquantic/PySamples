from setuptools import setup
# We have to split our dependencies up by those that run on Windows and those that do not since
# some won't install on Windows.
# install_requires = [
#     'peewee==3.17.0'
# ]
setup(
    name='PySamples',
    version='',
    packages=['models'],
    url='',
    license='',
    author='test',
    author_email='',
    description='',
    # install_requires=install_requires
)
