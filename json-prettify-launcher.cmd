@ECHO OFF
title JSON Prettify Launcher
cls
echo Enter input file name/path (e.g. "C:\temporary\json\transaction.json"):
set /p infile=""
echo.
python json-prettify.py --infile %infile%
echo.
pause