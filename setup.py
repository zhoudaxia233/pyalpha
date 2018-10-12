from setuptools import setup

version = '0.1.0'

setup(
    name='pyalpha',
    version=version,
    description="A process mining tool written in Python3",
    keywords='alpha miner',
    author='Zheng Zhou',
    author_email='yootaoo@gmail.com',
    url='https://github.com/zhoudaxia233/pyalpha',
    license='MIT',
    packages=['pyalpha'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    dependency_links=[],
    entry_points={
        'console_scripts': [
          'pyalpha=pyalpha.main:main',
      ]
    }

)