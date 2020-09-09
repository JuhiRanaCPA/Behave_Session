# from distutils.core import setup
from setuptools import setup
setup(name='PythonBDDtutorial',
      version='1.0',
      description='Python Behave project',
      # author='Admas Kinfu',
      # author_email='admaskinfu@gmail.com',
      url='https://www.google.com/',
      packages=[
            'common',
            'common.commonFuncs',
            'common.commonSteps',
            'common.commonConfigs'
      ],
     )

