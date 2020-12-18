@ECHO OFF

::CHECK FOR VIRTUAL ENV AND CREATE
IF EXIST env (
    ECHO Virtual Environment Found.
) ELSE (
    ECHO No Environment Found.
    ECHO Installing Virtual Environment...
    CALL python -m venv env
)

CALL env\Scripts\activate.bat
CALL pip install discord.py
ECHO Virtual Environment and Library Installed.