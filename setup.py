import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIREMENTS = [
    'argparse >= 1.4.0',
]

setuptools.setup(
    name='gatekeeper-suite',
    version='1.0.0',
    description='Gatekeeper is a suite of tools that sees and knows all about your code.',
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
    install_requires=REQUIREMENTS,
    extras_require={
        'dev': [
            'pylint >= 2.5.0',
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
