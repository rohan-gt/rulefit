from setuptools import setup

setup(name='rulefit',
      version='0.3',
      description='RuleFit algorithm',
      author='Rohan George Thampi',
      author_email='rohangt1591@gmail.com',
      url='https://github.com/rohan-gt/rulefit',
      packages=['rulefit'],
      install_requires=[
            'numpy>=1.16.1',
            'pandas>=0.24.1',
            'scikit-learn>=0.20.2']
)
