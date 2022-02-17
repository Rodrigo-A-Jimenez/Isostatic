import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="isostatic",
    version="0.0.1dev",
    author="Rodrigo Jimenez",
    author_email="jimenezhuancarodrigo@gmail.com",
    description="A repository for designing isostatic structures",
    long_description= long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Rodrigo-A-Jimenez/Isostatic",
    project_urls={
        "Bug Tracker": "https://github.com/Rodrigo-A-Jimenez/Isostatic/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)