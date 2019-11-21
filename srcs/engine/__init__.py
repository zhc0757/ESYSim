#
# File name : __init__.py
# Function : Initilization file of module engine.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA  02110-1301, USA.
#
# Copyright (C) 2017, Junshi Wang <wangeddie67@gmail.com>

##
# @ingroup ESY_SIM_ENGINE
# @package engine
# Simulation engine, including event and event queue

##
# @ingroup ESY_SIM_ENGINE
# @file engine/__init__.py
# @brief Initialization file of python module engine.

##
# @class engine.EsyEventQueue
# @brief

##
# @fun engine.addOptions
# @brief

import os
import sys
sys.path.append( os.path.split(__file__)[ 0 ] )

from .esy_engine import EsyEventQueue
from .py_esy_engine import addOptions, \
                           buildEngine
