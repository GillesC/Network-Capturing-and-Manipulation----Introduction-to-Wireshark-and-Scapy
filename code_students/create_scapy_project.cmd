::navigate to project directory
C:\Users\Calle>cd C:\Users\Calle\Documents\labo-scapy
::check python version is 3.X
C:\Users\Calle\Documents\labo-scapy>python --version
Python 3.8.0

::check which python.exe location we will use
C:\Users\Calle\Documents\labo-scapy>where python
    C:\Users\Calle\AppData\Local\Programs\Python\Python38\python.exe
    C:\Users\Calle\AppData\Local\Microsoft\WindowsApps\python.exe

::create virtual environment .venv
C:\Users\Calle\Documents\labo-scapy>python -m venv .venv

::activate that environment
C:\Users\Calle\Documents\labo-scapy>.venv\Scripts\activate

::install scapy in the venv
(.venv) C:\Users\Calle\Documents\labo-scapy>pip install scapy
Collecting scapy
  Using cached https://files.pythonhosted.org/packages/52/e7/46aa46a7907d/scapy-2.4.3.tar.gz
Installing collected packages: scapy
  Running setup.py install for scapy ... done
Successfully installed scapy-2.4.3

::run scapy to check if working
(.venv) C:\Users\Calle\Documents\labo-scapy>scapy
