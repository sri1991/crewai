from setuptools import setup, find_packages

setup(
    name="first",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "crewai",
        "python-dotenv",
        "google-cloud-aiplatform",
    ],
    python_requires=">=3.7",
) 