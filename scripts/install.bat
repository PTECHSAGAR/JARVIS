@echo off
echo Installing JARVIS Python dependencies...
python -m venv venv
call venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
echo JARVIS installation complete!
pause
