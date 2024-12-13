import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-loguru",
    version="2.0.0",
    author="Tiago Silva",
    author_email="tiago.arasilva@gmail.com",
    contributor="Amitabh Suman",
    contributor_email="amitabhsuman.ss89@gmail.com",
    description="A middleware to log the requests and responses using loguru.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tarsil/django-loguru",
    packages=setuptools.find_packages(exclude=['tests*']),
    install_requires=["django>=3.1", "loguru"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires='>=3.7',
)
