ERP Automation Script - README
==============================

Automate login and OTP retrieval for IIT Kharagpur ERP using Selenium and ChromeDriver.

Prerequisites
-------------

1.  **Python**: Install Python 3.x.
    
2.  **Chrome**: Install Google Chrome.
    
3.  **ChromeDriver**: Download the ChromeDriver matching your Chrome version.
    
4.  pip install selenium
    
5.  **constants.py Configuration**: Create a constants.py file:
    

### Example of constants.py

YOUR_ROLL_NUMBER = "<your roll no>"\n
YOUR_PASSWORD = "<your password>"\n
YOUR_SCHOOL = "<answer to security question>"\n
YOUR_FAV_SINGER = "<answer to security question>"\n
YOUR_FAV_SPORT = "<answer to security question>"\n
SELENIUM_DRIVER_PATH = "C:\\path\\to\\chromedriver.exe"\n
CHROME_USER_DATA_DIRECTORY = "C:\\path\\to\\chrome\\user\\data"\n


Setup Instructions by OS
------------------------

### macOS

1.  chmod +x /usr/local/bin/chromedriver
    
2.  Set SELENIUM\_DRIVER\_PATH to /usr/local/bin/chromedriver.
    
3.  Find Chrome profile in ~/Library/Application Support/Google/Chrome.
    
4.  python your\_script.py
    

### Linux

1.  **Install ChromeDriver**: Extract to /usr/bin/ or /usr/local/bin/.
    
2.  Set SELENIUM\_DRIVER\_PATH accordingly.
    
3.  Chrome user data is in ~/.config/google-chrome.
    
4.  python your\_script.py
    

### Windows

1.  **Install ChromeDriver**: Extract to C:\\SeleniumDrivers\\.
    
2.  Set SELENIUM\_DRIVER\_PATH in constants.py.
    
3.  Chrome user data: C:\\Users\\\\AppData\\Local\\Google\\Chrome\\User Data.
    
4.  python your\_script.py
    

Customization
-------------

### Edit Security Questions

In main.py, update conditions for the security questions to match the ERP portal. Use answers from constants.py.

### Profile Selection

1.  Locate profiles in CHROME\_USER\_DATA\_DIRECTORY.
    
2.  Set profile\_name (e.g., Default, Profile 2).
    
3.  Check profile path with chrome://version.
    

Chrome Version and ChromeDriver
-------------------------------

1.  **Find Chrome Version**:
    
    *   Menu > Help > About Google Chrome.
        
2.  **Download ChromeDriver**: [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/).
    
    *   Match major version numbers.
        

Usage
-----

`python your_script.py `

*   **Ensure Gmail is pre-logged in** to the specified profile.
    
*   **Keep ChromeDriver updated** to match Chrome.
    

By following this guide, you can automate ERP login and OTP handling efficiently.
