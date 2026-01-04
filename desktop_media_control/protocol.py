#!/usr/bin/env python3
#
#  protocol.py
"""
Protocol interface for media controls.
"""
#
#  Copyright © 2025 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
#  OR OTHER DEALINGS IN THE SOFTWARE.
#

# stdlib
from typing import Protocol

# this package
from desktop_media_control.player import Player

__all__ = ["MediaControlProtocol"]


class MediaControlProtocol(Protocol):
	"""
	Windows media controls interface.

	:param player:
	:param app_name: The name of the application.
	"""

	player: Player

	def __init__(self, player: Player, app_name: str) -> None: ...

	def on_playback(self) -> None: ...

	def on_playpause(self) -> None: ...

	def on_volume(self) -> None: ...

	def play(self) -> None: ...

	def pause(self) -> None: ...
