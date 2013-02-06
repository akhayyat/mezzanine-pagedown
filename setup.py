from distutils.core import setup

import os
if os.path.exists("README.txt"):
    readme = open("README.txt")
else:
    print "Warning: using markdown README"
    readme = open("README.md")

setup(
    name = "mezzanine-pagedown",
    version = "0.2",
    description = "PageDown rich text widget for Mezzanine",
    long_description = readme.read(),
    author = "Ahmad Khayyat",
    author_email = "akhayyat@gmail.com",
    license = "BSD",
    url = "https://bitbucket.org/akhayyat/mezzanine-pagedown",
    install_requires=(
        "setuptools",
        "filebrowser_safe >= 0.2.13",
        "mezzanine >= 1.3.0",
        "markdown",),
    packages = [
        "mezzanine_pagedown",
    ],
    package_data = {
        "mezzanine_pagedown": [
            "templates/mezzanine_pagedown/*.html",
            "static/mezzanine_pagedown/pagedown/Markdown.Converter.js",
            "static/mezzanine_pagedown/pagedown/Markdown.Sanitizer.js",
            "static/mezzanine_pagedown/pagedown/Markdown.Editor.js",
            "static/mezzanine_pagedown/pagedown/wmd-buttons.png",
            "static/mezzanine_pagedown/css/*",
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: JavaScript",
        "Framework :: Django",
    ],
)
