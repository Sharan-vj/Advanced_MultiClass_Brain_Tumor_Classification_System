# Import the setuptools module
import setuptools

# Open the README.md file and read its content.
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read() 

# version of the package
__version__ = "1.0.0"

# Meta data about the package
REPO_NAME = "Advanced_MultiClass_Brain_Tumor_Classification_System"
AUTHOR_USER_NAME = "Sharan-vj"
PACKAGE_NAME = "tumorClassifier"
AUTHOR_EMAIL = "sharanvj678@gmail.com"

# Set up the package using the setuptools module
setuptools.setup(
    name=PACKAGE_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src", exclude='test')
)