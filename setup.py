from setuptools import setup

setup(
    name="latin_to_arabic_number",
    version="0.0.1",
    description="This is a library to reverse numbers order and change latin numbers to arabic in a .docx file",
    py_modules=["latin_to_arabic_number"],
    package_dir= {'':'src'},
    long_description= 'Reverse Latin Numbers Order || Change It To Arabic',
    classifiers=[
        'Programming Language :: Python :: 3',
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