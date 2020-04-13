Rewrite the original readme with a  compact version

## Usage

* Install dependencies (```$ pip install -r requirements.txt```)
* Launch the script with python2
* Proceed to the page that is intended to be refreshed
* Wait until the beeping (using `say` for MAC)

## Principles

* Initialize a webdriver (https://chromedriver.chromium.org/ for Chrome and https://github.com/mozilla/geckodriver/releases for FireFox) with the installed path (e.g., ```python driver = webdriver.Chrome(executable_path="<your-webdriver-path>")```)
* 

## MISC

For windows, you'll have to install an additional package ```winsound``` for the beeping

```python
import winsound

duration = 1000
freq = 440
winsound.Beep(freq, duration)
```