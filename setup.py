import setuptools
# https://packaging.python.org/en/latest/tutorials/packaging-projects/

root_module_folder = 'genankichinese'

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="genanki-chinese",
    version="0.1.6",
    author="Ruben Serradas",
    author_email="rubenserradas@gmail.com",
    description="Packages which automates the creation and update of chinese notes for Anki",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RubenSerradas/genanki-chinese",
    scripts=['bin/genanki-chinese'],
    project_urls={
        "Bug Tracker": "https://github.com/RubenSerradas/genanki-chinese/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Intended Audience :: Education"
    ],
    package_dir={root_module_folder: root_module_folder},
    packages=[root_module_folder],
    install_requires=[
        'genanki',
        'requests',
        'OpenCC',
        'pypinyin',
        'gTTS',
        'googletrans==4.0.0rc1',
    ],
    python_requires=">=3.8",
)
