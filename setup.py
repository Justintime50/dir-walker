import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

REQUIREMENTS = [
    'pretty-tables == 1.*',
]

DEV_REQUIREMENTS = [
    'coveralls == 3.*',
    'flake8',
    'pytest == 6.*',
    'pytest-cov == 2.*',
]

setuptools.setup(
    name='roverio',
    version='2.3.0',
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
        'dev': DEV_REQUIREMENTS,
    },
    entry_points={
        'console_scripts': [
            'roverio-file-extension = roverio.file_extension:main',
            'roverio-phone-email-searcher = roverio.phone_email_searcher:main',
            'roverio-readmy-readmes = roverio.readmy_readmes:main',
            'roverio-scout = roverio.scout:main',
            'roverio-secrets = roverio.secrets:main',
            'roverio-sequential-renamer = roverio.sequential_renamer:main',
        ]
    },
    python_requires='>=3.7',
)
