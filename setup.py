import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="decOM",
    version="0.0.30",
    author="Camila Duitama González",
    author_email="cduitama@pasteur.fr",
    description="decOM: Similarity-based microbial source tracking for contamination assessment of ancient oral samples using k-mer-based methods",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CamilaDuitama/decOM",
    project_urls={
        "Bug Tracker": "https://github.com/CamilaDuitama/decOM/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
        "plotly>=5.5.0",
        "importlib_resources>=5.4.0",
        "dask>=2021.12.0",
        "numpy",
        "kaleido",
        "colorama",
        "pandas",
    ],
    python_requires=">=3.6",
    include_package_data=True,
    package_data={"": ["data/*"]},
    entry_points={
        "console_scripts": [
            "decOM = decOM.__main__:main",
            "decOM-aOralOut = decOM.aOralOut.__main__:main",
            "decOM-format = decOM.format.__main__:main",
            "decOM-LOO = decOM.LOO.__main__:main",
            "decOM-CV = decOM.CV.__main__:main",
            "decOM-MST = decOM.MST.__main__:main",
        ],
    },
)
