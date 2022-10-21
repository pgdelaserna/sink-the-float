#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This library contains the board game to be used
"""

#================================================================#

# Built-in/Generic imports
import os
import sys

# Libraries
import string
#import gameelements

__author__ = "pgdelaserna"
__version__ = "1.0"

#================================================================#

class Position:
  """
  This class represents a position on the board
  """

  def __init__(self, pos_x, pos_y, has_boat=False, is_hit=False) -> None:
    """
    This is the init function for the position class
    """
    # Initialise values
    self.pos_x = pos_x
    self.pos_y = pos_y
    self.has_boat = has_boat
    self.is_hit = is_hit

# Properties
  @property
  def pos_x(self):
    return self._pos_x
  
  @pos_x.setter
  def pos_x(self, value):
    self._pos_x = value

  @property
  def pos_x(self):
    return self._pos_x
  
  @pos_x.setter
  def pos_x(self, value):
    self._pos_x = value

  @property
  def has_boat(self):
    return self._has_boat
  
  @has_boat.setter
  def has_boat(self, value):
    self._has_boat = value

  @property
  def is_hit(self):
    return self._is_hit
  
  @is_hit.setter
  def is_hit(self, value):
    self._is_hit = value

class Board:
  """
  This class represents the board to be used in Sink the Float
  """
  def __init__(self, width: int=10, height: int=10) -> None:
    """
    Init function for the board class
    """
    # Set values as input by the user, otherwise default are used
    self.width = width
    self.height = height
    self.grid = self.initise_grid()

# Properties
  @property
  def width(self):
    """
    width property
    """
    return self._width

  @width.setter
  def width(self, value: int):
    """
    width setter
    """
    if ( value < 0 ):
      raise ValueError( "height cannot be less than 0" ) 
    self._width= value
  
  @property
  def height(self):
    """
    height property
    """
    return self._height

  @height.setter
  def height(self, value: int):
    """
    height setter
    """
    if ( value < 0 ):
      raise ValueError( "height cannot be less than 0" ) 
    self._height= value

# Additional methods
  def initise_grid(self):
    """
    This function initialises the grid
    """
    grid = []
    for y in range(self.height):
      col = []
      for x in range(1,self.width):
        Pos = Position(pos_x=x, pos_y=y, has_boat=False, is_hit=False)
        col.append(Pos)
      grid.append((col))

    return grid

  def print_grid(self):
    """
    This function prints the grid into the console
    """
    status = 'X'

    # Build horizontal header and separator
    hor_hed = '|   '
    hor_sep = '+---'
    for i in range(1,self.width+1):
      hor_hed += '| ' + str(i) + ' '
      hor_sep += '+-' + len(str(i))*'-' + '-'
    hor_hed += '|'
    hor_sep += '+'

    # Print to terminal
    print(hor_sep)
    print(hor_hed)
    print(hor_sep)

    # Build vertical line and separator
    ver_line = ''
    for i in range(0,self.height):
      ver_line = '| ' + string.ascii_uppercase[i] + ' '
      for j in range(1,self.width+1):
        ver_line += '|' + len(str(j))*' ' + status + ' '
      ver_line += '|'
      # Print to terminal
      print(ver_line)
      print(hor_sep)

#================================================================#

# Executable code
if __name__ == '__main__':
  # Create object
  Board = Board()
  # Board.print_grid()


