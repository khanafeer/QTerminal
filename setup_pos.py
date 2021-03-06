from setuptools import setup
import py2exe
import os
Mydata_files = [('', ['logo.ico']),('imageformats',['C:\\Python27/Lib/site-packages/PySide/plugins/imageformats/qjpeg4.dll',

    'C:\\Python27/Lib/site-packages/PySide/plugins/imageformats/qgif4.dll',

    'C:\\Python27/Lib/site-packages/PySide/plugins/imageformats/qico4.dll',

    'C:\\Python27/Lib/site-packages/PySide/plugins/imageformats/qmng4.dll',

    'C:\\Python27/Lib/site-packages/PySide/plugins/imageformats/qsvg4.dll',

    'C:\\Python27/Lib/site-packages/PySide/plugins/imageformats/qtiff4.dll'

    ])]
packs = []
setup(
 	data_files=Mydata_files,
  options = {
    'py2exe' : {
        'compressed': 1,
        'optimize': 2,
        'packages':packs,
        'bundle_files': 3, #Options 1 & 2 do not work on a 64bit system
        'dist_dir': 'dist',  # Put .exe in dist/
        'xref': False,
        'skip_archive': False,
        'ascii': False,
        }
        },
windows = [{
    "script": "main_app.py",
    "icon_resources": [(1, "logo.ico")],
    "dest_base": "QTerminal"

}],
  zipfile=r"lib\shardlib",
)
