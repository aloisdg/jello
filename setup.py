import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='jello',
    version='0.3.1',
    author='Kelly Brazil',
    author_email='kellyjonbrazil@gmail.com',
    description='Filter JSON and JSON Lines data with Python syntax.',
    install_requires=[],
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    url='https://github.com/kellyjonbrazil/jello',
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'jello=jello.cli:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Utilities'
    ]
)
