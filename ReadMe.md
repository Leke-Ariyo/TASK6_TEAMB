<div align="center">

![hng](https://res.cloudinary.com/iambeejayayo/image/upload/v1554240066/brand-logo.png)

<br>

</div>

# WEB SCRAPING

## INTRODUCTION
This is Task 6 Submission by Team B of the HNG Internship 6.0, Machine Learning Track. We were assigned to use a web scraping tool like Selenium to get the H-index, names and other informations of Computer Science professors on Google Scholar(Page 1 - 25)

## Getting Started
The Google Scholar Site scraped is https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=Computer+Science+professors&btnG=

### Requirements
- Google Chrome
- Chrome Driver which should be the same version as Your Google Chrome installed
- A compatible Integrated Development Environment(IDE) such as Visual Studio Code(VSCode)
- Selenium
- Pandas

## Installations
- https://www.google.com/chrome/ to install google chrome
- https://sites.google.com/a/chromium.org/chromedriver/home to install webdriver for chrome
- ```pip install selenium``` to install the web scraping tool, make sure you have pip installed
- ```pip install pandas``` to install pandas.

### Configuration

```
# Import the necessary libraries
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
```

```
#This blocks the notification popup generated by the site
OPTIONS = webdriver.ChromeOptions()
OPTIONS.add_argument("--disable-notifications")
```

```
# Define empty list variables in which we will store the different results in
LIST_OF_LINKS = []
TOTAL_NAME = []
TOTAL_BIO = []
TOTAL_H_INDEX = []
H_INDEX_2014 = []
TOTAL_I_10_INDEX = []
I_10_INDEX_2014 = []
TOTAL_CITATIONS = []
```

```
# After collecting the necessary html tags of the urls, begin to scrape each of them to extract the names and H-Index
for each in LIST_OF_LINKS:
    print("collecting data of "+str(int(LIST_OF_LINKS.index(each))+1))
    DRIVER.get(each) #goes to each link
    try:
        name_path = "gsc_prf_in"
        name = DRIVER.find_element_by_id(name_path).text
        #gets the container of name and the text which is the name
        TOTAL_NAME.append(name)
        time.sleep(6)
    except Exception as _e:
        TOTAL_NAME.append("No Data")
# Next catch various possible errors using "try" and "except"
```

```
#print the results of each list

print(TOTAL_NAME)
print(TOTAL_BIO)
print(TOTAL_H_INDEX)
print(H_INDEX_2014)
print(TOTAL_I_10_INDEX)
print(I_10_INDEX_2014)
print(TOTAL_CITATIONS)
```

```
#Store these results in Pandas Dataframe

DF = pd.DataFrame({'Names': TOTAL_NAME,
                   'Bio Data': TOTAL_BIO,
                   'H Index': TOTAL_H_INDEX,
                   'H Index sice 2014': H_INDEX_2014,
                   'I-10 Index': TOTAL_I_10_INDEX,
                   'I-10 Index since 2014': I_10_INDEX_2014,
                   'Citation': TOTAL_CITATIONS,
                   })  
```    

```
#Output the dataframe into a csv file

DF.to_csv('output.csv') 
```

## How to Use it
- After installing the necessary applications and packages, proceed to run the `scraper.py` file, that is, run `python3 scraper.py` in the terminal. Make sure it is in the same directory as the chromedriver installed.
- In order to avoid the existence of duplicate files, please rename the "output.csv" file located on the last line of `scraper.py` file.

### Important Precautions to Take
-  Please wait patiently for the code to finish running, it might take a while.
The reason for delay is the `time.sleep()` function which will prevent a flagdown from google as a result of the frequent actions occuring in the site.
-  Sometimes a fluctuating network might cause a break in code, so if it is stuck at a
point for too long, please refresh the browser.


## Conclusion
Following the above instructions will give an output of the names of 250 Computer Science Professors and their H-Index in csv format.



## Built with Visual Studio Code by members of TEAM B, Task 6.
