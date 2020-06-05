from setuptools import setup

setup(name='RuleFit',
      version='0.3',
      description='RuleFit algorithm',
      author='Rohan George Thampi',
      author_email='rohangt1591@gmail.com',
      url='',
      packages=['rulefit'],
      install_requires=[
            'scikit-learn>=0.20.2',
            'numpy>=1.16.1',
            'pandas>=0.24.1']
)
