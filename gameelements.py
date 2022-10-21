#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This library contains the board elements
"""

#================================================================#
# Built-in/Generic imports
import os
import sys

# Libraries

__author__ = "pgdelaserna"
__version__ = "1.0"

#================================================================#

class Boat:
  """
  This class represents a boat
  """
  def __init__(self, length, str_x, end_x, str_y, end_y):
    """
    This function initialises the boat class
    """
    # Boat length
    self.length = length
    # Start position X
    self.str_x = str_x
    # End position X
    self.end_x = end_x
    # Start position Y
    self.str_y = str_y
    # End position Y
    self.end_y = end_y
  
# Properties
  @property
  def length(self):
    """
    Boat length property
    """
    return self._length

  @length.setter
  def length(self, value: int):
    """
    Boat length setter
    """
    if ( value < 2 ):
      raise ValueError( "Boat length cannot be less than 2" ) 
    self._length = value
  
  @property
  def str_x(self):
    """
    Boat str_x property
    """
    return self._str_x

  @str_x.setter
  def str_x(self, value: int):
    """
    Boat str_x setter
    """
    if ( value < 0 ):
      raise ValueError( "Boat str_x cannot be less than 0" ) 
    self._str_x = value
  
  @property
  def end_x(self):
    """
    Boat end_x property
    """
    return self._end_x

  @end_x.setter
  def end_x(self, value: int):
    """
    Boat end_x setter
    """
    if ( value < 0 ):
      raise ValueError( "Boat end_x cannot be less than 0" ) 
    self._end_x = value
  
  @property
  def str_y(self):
    """
    Boat str_y property
    """
    return self._str_y

  @str_y.setter
  def str_y(self, value: int):
    """
    Boat str_y setter
    """
    if ( value < 0 ):
      raise ValueError( "Boat str_y cannot be less than 0" ) 
    self._str_y = value
  
  @property
  def end_y(self):
    """
    Boat end_y property
    """
    return self._end_y

  @end_y.setter
  def end_y(self, value: int):
    """
    Boat end_y setter
    """
    if ( value < 0 ):
      raise ValueError( "Boat end_y cannot be less than 0" ) 
    self._end_y = value

#================================================================#

# Executable code
if __name__ == '__main__':
  # Create object
  Boat = Boat(length=4, str_x=0, end_x=0, str_y=0, end_y=0)
