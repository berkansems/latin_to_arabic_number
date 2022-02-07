import os
from setuptools import setup

def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        return file.read()
setup(
    name="latin_to_arabic_number",
    version="0.0.3",
    description="This library helps to reverse numbers order OR change latin numbers to arabic in a .docx file",
    py_modules=["latin_to_arabic_number"],
    package_dir= {'':'src'},
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
      ],
    install_requires=[
              'Document>=0.8.11',
          ],
    url="https://github.com/berkansems/latin_to_arabic_number",
    author="berkan sems",
    author_email = "berkansems@gmail.com"

)