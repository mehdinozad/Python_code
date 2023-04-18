#The absolute address of the Python file content package
#The  address of the Python file content package name

from pathlib import Path
import os

x= Path(__file__).parent
print(x)

x = os.path.basename(os.path.dirname(__file__))
print(x)