from setuptools import setup, find_packages

setup(
    name="brill_postagger",
    version="0.1.0",
    description="Brill Postagger for various languages using NLTK",
    author="JarbasAi",
    author_email="jarbasai@mailfence.com",
    url="https://github.com/TigreGotico/brill_postaggers",
    packages=find_packages(),
    install_requires=[
        'nltk>=3.6.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
    include_package_data=True,
    package_data={
        '': ['*.pkl'],  # Include your .pkl model files in the distribution
    },
)
