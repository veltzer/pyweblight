import setuptools

"""
The documentation can be found at:
http://setuptools.readthedocs.io/en/latest/setuptools.html
"""
setuptools.setup(
    # the first three fields are a must according to the documentation
    name='pyweblight',
    version='0.0.1',
    packages=[
        'pyweblight',
        'pyweblight.endpoints',
    ],
    # from here all is optional
    description='pyweblight is a small configurable web server for developers',
    long_description='pyweblight is a small configurable web server for developers',
    author='Mark Veltzer',
    author_email='mark.veltzer@gmail.com',
    maintainer='Mark Veltzer',
    maintainer_email='mark.veltzer@gmail.com',
    keywords=[
        'http',
        'https',
        'apache',
        'python',
        'python3',
        'server',
        'web',
    ],
    url='https://veltzer.github.io/pyweblight',
    download_url='https://github.com/veltzer/pyweblight',
    license='MIT',
    platforms=[
        'python3',
    ],
    install_requires=[
        'python-daemon',
        'pytconf',
        'pylogconf',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    data_files=[
    ],
    entry_points={'console_scripts': [
        'pyweblight=pyweblight.endpoints.main:main',
    ]},
    python_requires='>=3.4',
)
