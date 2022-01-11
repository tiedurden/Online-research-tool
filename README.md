# Online-research-tool
A selenium script that scans a list of websites from for an arbitrary number of searchterms and pushes results into an csv file

# Setup
0) You need to have python 3 installed 

2) Install the package manager for Python <br>  
  $ python get-pip.py 
(Windows is different: https://pip.pypa.io/en/stable/installation/)

3) Create a virtual environment for this script <br> 
  $ python3 -m venv nameofvenv
(Windows is very different: https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html#where-is-python)
  
4) Activate virtual environment <br> 
  $ source nameofvenv/bin/activate 

5) Install the required packages for this script(just in the venv, not globally) <br> 
  $ pip install -r requirements.txt

6) Add path to your browser in row 9 of script <br> 
  driver = webdriver.Chrome('path/to/browser')
  
if you want to use Chromium you can choose the location for the chromedriver<br> 
Downloadlink for Chromium 'chromedriver': <br> 
https://chromedriver.chromium.org/downloads
  
# Runscript
$ python research_tool.py 
  
if you want to see the "action" happening comment out row 7 <br>
and make the selenium test not headless
  <br> change 
  <br> chrome_options.add_argument('headless')
  <br> to
  <br> \# chrome_options.add_argument('headless')

