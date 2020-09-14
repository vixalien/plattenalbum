#!/usr/bin/python3
# -*- coding: utf-8 -*-
import DistUtilsExtra.auto

DistUtilsExtra.auto.setup(
	name='mpdevil',
	version='0.9.1',  # sync with bin/mpdevil
	author="Martin Wagner",
	author_email="martin.wagner.dev@gmail.com",
	description=('A simple music browser for MPD'),
	url="https://github.com/SoongNoonien/mpdevil",
	license='GPL-3.0',
	data_files=[
		('share/icons/hicolor/16x16/apps/', ['data/icons/16x16/mpdevil.png']),
		('share/icons/hicolor/22x22/apps/', ['data/icons/22x22/mpdevil.png']),
		('share/icons/hicolor/24x24/apps/', ['data/icons/24x24/mpdevil.png']),
		('share/icons/hicolor/32x32/apps/', ['data/icons/32x32/mpdevil.png']),
		('share/icons/hicolor/48x48/apps/', ['data/icons/48x48/mpdevil.png']),
		('share/icons/hicolor/64x64/apps/', ['data/icons/64x64/mpdevil.png']),
		('share/icons/hicolor/128x128/apps/', ['data/icons/128x128/mpdevil.png']),
		('share/icons/hicolor/256x256/apps/', ['data/icons/256x256/mpdevil.png']),
		('share/icons/hicolor/scalable/apps/', ['data/icons/scalable/mpdevil.svg'])
	],
)

