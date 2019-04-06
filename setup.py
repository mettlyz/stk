from distutils.core import setup

setup(name='stk',
      author='Lukas Turcani',
      author_email='lukasturcani93@gmail.com',
      url='https://www.github.com/lukasturcani/stk',
      version='2019.04.06.0',
      packages=['stk',
                'stk.utilities',
                'stk.molecular',
                'stk.molecular.topologies',
                'stk.molecular.topologies.cage',
                'stk.optimization'],
      install_requires=['networkx',
                        'scipy',
                        'matplotlib',
                        'scikit-learn',
                        'psutil',
                        'pywindowx==0.0.3',
                        'pandas',
                        'seaborn'],
      python_requires='>=3.6')
