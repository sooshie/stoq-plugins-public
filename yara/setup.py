from setuptools import setup, find_packages

setup(
    name="yara",
    version="2.0.1",
    author="Marcus LaFerrera (@mlaferrera), David Maydewd",
    url="https://github.com/PUNCH-Cyber/stoq-plugins-public",
    license="Apache License 2.0",
    description="Process a payload using yara",
    packages=find_packages(),
    include_package_data=True,
    test_suite='tests',
    package_data={'yarascan': ['yarascan.stoq', 'rules/*']},
)
