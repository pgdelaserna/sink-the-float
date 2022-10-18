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

__author__ = "pgdelaserna"
__version__ = "1.0"

#================================================================#

class Position:
  """
  This class represents a position on the board
  """

  def __init__(self) -> None:
    """
    This is the init function for the position class
    """
    # Initialise values
    self.pos_x = 0
    self.pos_y = 0
    self.has_boat = False
    self.is_hit = False

class Board:
  """
  This class represents the board to be used in Sink the Float
  """

  # Properties
  width = 0
  heidht = 0

  def __init__(self, width: int=10, height: int=10) -> None:
    """
    Init function for the board class
    """
    # Set values as input by the user, otherwise default are used
    self.width = width
    self.height = height

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
  Board.print_grid()


