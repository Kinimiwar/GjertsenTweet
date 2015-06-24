"""
Welcome to GjertsenTweet's documentation!
=========================================

**GjertsenTweet** is a twitter client built for the command line.
It has been built with npyscreen which is based on curses to create a simple 
text-based user interface.

It lets you read the tweets from your feed, search for tweets and post tweets.

.. image:: http://i.imgur.com/t3bofl5.png

Usage
-----
Run *gjertsentweet* in your terminal to fire it up. There's no command-line arguments.
When launched for the first time you will be asked to open a link in your browser
in order to approve the app. You will be given a pin from twitter which lets 
you log into your account from GjertsenTweet.

When logged in, you can simply use the arrow keys or enter to move around.
Note that once you have moved down to feed, you can't use the arrow key to
move the cursor back to the tweet/search fields. To do this you will have to
press one of the buttons.

The twitter feed will be updated on the fly.

Note that you have to press enter when the dialog boxes pops up in order
to move the cursor down to the button/buttons

Platform
--------
This was originally written to be run on unix like operating systems, but
it's also possible to run on windows, all you need to do is to install curses 
for windows from here http://www.lfd.uci.edu/~gohlke/pythonlibs/ if you haven't 
already done it  
"""

from setuptools import setup

setup(name='GjertsenTweet',
      version='0.3.7',
      description='A simple twitter client for the terminal',
      long_description = __doc__,
      author='Fredrik Gjertsen',
      author_email='f.gjertsen@gmail.com',
      url='https://github.com/fredgj/GjertsenTweet',
      packages=['GjertsenTweet'],
      license='GNU General Public License',
      install_requires=['npyscreen==4.9.1',
                        'twitter==1.17.0'],
      entry_points={
          'console_scripts':
            ['gjertsentweet=GjertsenTweet.client:main',
             'GjertsenTweet=GjertsenTweet.client:main']
          },
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Console',
                   'Intended Audience :: End Users/Desktop',
                   'Natural Language :: English',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Utilities'],
      keywords='twitter, command-line tools')


__author__ = 'Fredrik Gjertsen'

