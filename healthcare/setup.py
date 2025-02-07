from setuptools import setup, find_packages

setup(
    name="healthcare",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "crewai",
        "google-generativeai",
        "python-dotenv",
        "pyyaml"
    ],
    entry_points={
        'console_scripts': [
            'healthcare=healthcare.main:main',
        ],
    },
) 