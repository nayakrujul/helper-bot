from setuptools import setup, find_packages

long_description = 'A command-line bot which can do a lot of things - read the docs at https://www.github.com/nayakrujul/helper-bot'

setup(
  name = 'helper-bot',
  version = '0.1',
  license='Apache',
  description = 'A command-line bot which can do a lot of things',
  author = 'Rujul Nayak',
  author_email = 'rujulnayak@outlook.com',
  url = 'https://github.com/nayakrujul/helper-bot',
  download_url = 'https://github.com/nayakrujul/helper-bot/archive/refs/tags/v_01.tar.gz',
  keywords = ['bot', 'command-line'],
  install_requires=[
    'pytz'
  ],
  classifiers=[
    'Development Status :: 3 - Alpha', 
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
  long_description=long_description,
  long_description_content_type='text/x-rst',
  packages = find_packages(),
  entry_points = {
    'console_scripts': [
      'randint = helper_bot.scripts:randint',
      'output = helper_bot.scripts:output',
      'timein = helper_bot.scripts:timein'
    ]
  }
)
