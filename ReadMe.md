<div align="center">

![hng](https://res.cloudinary.com/iambeejayayo/image/upload/v1554240066/brand-logo.png)

<br>

</div>

# WEB SCRAPING

## INTRODUCTION
This is Task 6 Submission by Team B of the HNG Internship 6.0, Machine Learning Track. We were assigned to use a web scraping tool like Selenium to get the H-index, names and other informations of Computer Science professors on Google Scholar(Page 1 - 25)

## Getting Started
The Google Scholar Site scraped is "https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=Computer+Science+professors&btnG="

### Requirements
- Google Chrome
- Chrome Driver which should be the same version as Your Google Chrome installed
- Compatible Integrated Development Environment(IDE) such as Visual Studio Code(VSCode)

## Installations
- https://www.google.com/chrome/ to install google chrome
- https://sites.google.com/a/chromium.org/chromedriver/home to install webdriver for chrome
- pip install selenium to install the web scraping tool, make sure you have pip installed
- pip install pandas to install pandas.

### Configuration
`import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys`

## How to Use it
- After installing the necessary applications and packages, proceed to run the `scraper.py` file, that is, run `python3 scraper.py` in the terminal. Make sure it is in the same directory as the chromedriver installed.
- In order to avoid the existence of duplicate files, please rename the the "output.csv" file located on the last line of `scraper.py`

### Important Precautions to Take
-  Please wait patiently for the code to finish running, it might take a while
The reason for delay is the `time.sleep()` function which will prevent a flagdown from google as a result of the frequent action on the site.
-  Sometimes a fluctuating network might cause a break in code, so if it is stuck at a
point for too long, please refresh the browser.


## Conclusion
Following the above instructions will give an output of the names of 250 Computer Science Professors and their H-Index in csv format.



## Built with Visual Studio Code by TEAM B, Task 6.
