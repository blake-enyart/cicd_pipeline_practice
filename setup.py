import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="cicd_pipeline_practice",
    version="0.1.0",
    description="A sample CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="author",
    package_dir={"": "cicd_pipeline_practice"},
    packages=setuptools.find_packages(where="cicd_pipeline_practice"),
    install_requires=[
        "aws-cdk.core==1.87.0",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
