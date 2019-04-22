import re
import setuptools

def find_version(path):
    version_file = open(path).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

with open('README.md') as f:
    long_description = f.read()

setuptools.setup(
    name="requests_random_user_agent",
    version=find_version("requests_random_user_agent/__init__.py"),
    author="David Wittman",
    author_email="david@wittman.com",
    description="Automatically generate a random User Agent for the requests library",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/DavidWittman/requests-random-user-agent",
    install_requires=['requests>=2.0.1,<3.0.0'],
    include_package_data=True,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
