from setuptools import setup
import pathlib

# The directory containing this file
HERE = '/recordcapture/recordcapture.py'

# The text of the README file
README = open("README.md").read()

# This call to setup() does all the work
setup(
    name="recordcapture",
    version="0.0.2",
    description="recordcapture is a library based on Desktop Duplication API, pillow, and pyaudio which provide multiple methods for capturing and recording Screen and Microphone.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Sandeeppushp/recordcapture",
    author="Sandeep Pushp",
    author_email="sandeepkumarpushp@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["recordcapture"],
    python_requires='>=3.8',
    include_package_data=True,
    install_requires=["screen_recorder_sdk","Pillow","pyaudio","wave"],
)