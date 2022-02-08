from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Developers',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name = 'hashily',
  version = '0.0.1',
  description = 'A module that allows you to encode and decode text in numerous ciphers.',
  long_description = open('README.md').read(),
  long_description_content_type = "text/markdown",
  url = "https://github.com/MystYT-21/hashily", 
  project_urls = {
   "Documentation": "https://hashily.readthedocs.io/en/latest/",
   "Issue tracker": "https://github.com/MystYT-21/hashily/issues",
                 },

  author = 'myst.67',
  author_email = 'saidulalamirfan3245@gmail.com',
  license = 'MIT', 
  classifiers= classifiers,
  keywords = ["encrypt", "encoding", "decoder", "encoder", "ciphers"], 
  packages = find_packages(),
  install_requires=[''] 
  
)