from setuptools import setup, find_packages

setup(
    name='Open Waste',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/OwenRube7/open-waste',
    license='MIT',
    author='Owen Rubenis',
    author_email='orubenis.edu@gmail.com',
    description='A short description of my project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'numpy',
        'pandas',
        # other dependencies...
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.12.1',
    ],
)