import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Pysafe",
    version="0.1.2",
    author="MNKANOUT",
    author_email="mnkanout@gmail.com",
    description="Python password manger",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    py_modules = ['pysafe','cryptor','password','input','output','keys',
                  'reset'],
    scripts=["pysafe.py"],
    install_requires=[
        'cffi==1.14.0',
        'colorama==0.4.3',
        'cryptography==2.8',
        'pycparser==2.20',
        'six==1.14.0',
        'termcolor==1.1.0',

      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)