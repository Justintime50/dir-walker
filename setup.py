import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIREMENTS = [
    'pretty-tables >= 1.0.0',
]

setuptools.setup(
    name='roverio',
    version='2.1.0',
    description='Rover IO is a suite of tools that traverses your directories and performs IO file operations.',  # noqa
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/justintime50/roverio',
    author='Justintime50',
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIREMENTS,
    extras_require={
        'dev': [
            'pytest >= 6.0.0',
            'pytest-cov >= 2.10.0',
            'coveralls >= 2.1.2',
            'flake8 >= 3.8.0',
            'mock >= 4.0.0',
        ]
    },
    entry_points={
        'console_scripts': [
            'roverio-scout = roverio.scout:main',
            'roverio-secrets = roverio.secrets:main',
            'roverio-file-extension = roverio.file_extension:main',
            'roverio-sequential-renamer = roverio.sequential_renamer:main',
            'roverio-readmy-readmes = roverio.readmy_readmes:main',
        ]
    },
    python_requires='>=3.6',
)
