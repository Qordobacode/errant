from distutils.core import setup

setup(
    name='errant',
    packages=['errant'],
    version='1.1.0',
    license='MIT',
    description='ERRor ANnotation Toolkit: Automatically extract and classify grammatical errors in parallel original and corrected sentences.',
    author='Christopher Bryant, Mariano Felice',
    maintainer='Sam Havens, Melisa Stahl, Manhal Daaboul',
    maintainer_email='sam.havens@qordoba.com, melisa@qordoba.com, manhal@qordoba.com',
    python_requires='>=3.4.0',
    url='https://github.com/Qordobacode/errant',
    download_url='https://github.com/Qordobacode/errant/archive/1.1.0.tar.gz',
    keywords=['error annotation toolkit', 'grammatical correction errors', '', 'grammatical errors', '', 'grammatical correction', 'GEC'],
    install_requires=[
        'spacy==1.9.0',
        'nltk==3.4.5'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    include_package_data=True
)
