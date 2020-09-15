import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='gatekeeper-suite',
    version='1.1.0',
    description='Gatekeeper is a suite of tools that sees and knows all about your code.',  # noqa
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/justintime50/gatekeeper',
    author='Justintime50',
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    extras_require={
        'dev': [
            'pytest >= 6.0.0',
            'pytest-cov >= 2.10.0',
            'coveralls >= 2.1.2',
            'flake8 >= 3.8.0',
        ]
    },
    entry_points={
        'console_scripts': [
            'gatekeeper-scout = gatekeeper.scout:main',
            'gatekeeper-secrets = gatekeeper.secrets:main',
            'gatekeeper-file-extension = gatekeeper.file_extension:main'
        ]
    },
    python_requires='>=3.6',
)
