import setuptools


def get_readme():
    with open('README.rst') as f:
        return f.read()


setuptools.setup(
    # the first three fields are a must according to the documentation
    name="pyweblight",
    version="0.0.3",
    packages=[
        'pyweblight',
        'pyweblight.endpoints',
    ],
    # from here all is optional
    description="pyweblight is a small configurable web server for developers",
    long_description=get_readme(),
    long_description_content_type="text/x-rst",
    author="Mark Veltzer",
    author_email="mark.veltzer@gmail.com",
    maintainer="Mark Veltzer",
    maintainer_email="mark.veltzer@gmail.com",
    keywords=[
        'http',
        'https',
        'apache',
        'python',
        'python3',
        'server',
        'web',
    ],
    url="https://veltzer.github.io/pyweblight",
    download_url="https://github.com/veltzer/pyweblight",
    license="MIT",
    platforms=[
        'python3',
    ],
    install_requires=[
        'python-daemon',
        'pytconf',
        'pylogconf',
    ],
    extras_require={
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
    ],
    data_files=[
    ],
    entry_points={"console_scripts": [
        'pyweblight=pyweblight.endpoints.main:main',
    ]},
    python_requires=">=3.6",
)
