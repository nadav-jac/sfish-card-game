from setuptools import setup, find_packages

setup(
    name="sfish",
    version="0.0.1",
    packages=find_packages(),  # Automatically find all packages under 'sfish'
    python_requires='>=3.11',  # Specify the minimum Python version
    extras_require={
        'dev': [
            'pytest',
            'pytest-mock',
        ]
    },

)
