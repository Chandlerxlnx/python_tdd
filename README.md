# python_tdd
  This repository is note book during my learning Test Driven Development

## tools

* Firefox web explorer
* git
* python 3.x
* Geckodriver
  - the driver that selenium used to remote control Firefox.

### Firefox and Geckodriver
* Firfox url: https://wwww.mozila.org/fiefox
* Geckodriver url: https://github.com/mozilla/geckodriver/releases
  - macOs, Linux: 
    + put it at ~/.local/bin
    + add the path to $path.
    ``` 
    echo 'PATH=~/.local/bin:$PATH' >> ~/.bashrc
    ```
  - window
    + put is at Scripts of python or anaconda if anaconda is installed.
### virtualenv
  Virtual environment allows different version installed in different virtualenv.

#### install
  * **window cmd**
  ``` BASH
     pip install virtualenvwrapper
  ```
  * **macOs, Linux cmd**
  ``` BASH
     pip install --user virtualenvwrapper
  ```
#### create virtal env
```
  # macOS Linux
  mkvirtualenv --python=python3.6 superlists

  #windows
  mkvirtualenv --python='py -3.6 -c"import sys: print(sys.executalbe)"' superlists
```
#### activate virtual env
```
 $ workon superlists
 (superlists) $ which python
 /home/chandler/.virtualenv/superlists/bin/python
```
#### stop virtual env
```
(superlist)$ deactivate
$
```

## Django and Selenium
* **install CMD**
```
  pip install "django <1.12" “selenium"
```