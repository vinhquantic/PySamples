# The below command is not worked
pip install -r requirements.txt


# If run the command "pip install beautifulsoup4" : It only install the libs into "c:\python312\lib\site-packages",
# this is not worked for blog project. So we have to install libs by the below way on PyCharm Community Edition.

# Insert the lines below, then hover mouse on the lib name (such as: beautifulsoup4), click "Install package beautifulsoup4"
# This way will install the libs into "D:\Drive_E\Workspace_Python\PySamples\venv\Lib\site-packages"
from beautifulsoup4 import BeautifulSoup
from Pygments import Pygments


