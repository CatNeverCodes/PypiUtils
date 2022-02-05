from src import catnevercodes
from setuptools import setup, find_packages

setup(
    name="catnevercodes",
    version=catnevercodes.__version__,
    description="Some Simple Utils",
    author="CatNeverCodes",
    author_email="574469831@qq.com",
    url="https://github.com/CatNeverCodes/PypiUtils",
    classifiers=["Programming Language :: Python :: 3"],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    package_data={"": ["*.yaml"]}
)