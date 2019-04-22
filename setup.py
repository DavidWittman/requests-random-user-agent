import setuptools

from requests_random_user_agent import __version__

setuptools.setup(
    name="requests_random_user_agent",
    version=__version__,
    author="David Wittman",
    author_email="david@wittman.com",
    url="https://github.com/DavidWittman/requests-random-user-agent",
    description="Automatically generate a random User-Agent for the requests library",
    install_requires=['requests>=2.0.1,<3.0.0'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
