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

## resources
  这个代码仓库是`Python 测试驱动开发 - 使用Django,Selenium和JavaScript进行web编程` 学习笔记。
  书中所有代码放在[github](https://github.com/hjwp/book-example). 每个章节的代码放在单独的分支中，各分支采用简短形式命名。比如：chapter_philosophy_and_refactoring.
  所有分支的代码可在http://www.ituring.com.cn/book/2052`随书下载` 处下载。
  > 书的附录J 说明如何使用git比较你我代码。

### 附录J示例源代码

* 将书的代码设为远程仓库：
```C
      #git remote add harry https://github.com/hjwp/book-example.git
      git remote add harry https://github.com/hjwp/Book-TDD-Web-Dev-Python
      git fetch harry
```

* 代码比较方法
  - 列如：对比第四章结束后的代码差异，
  ```C
    git diff harry/chapter_philosophy_and_refactoring
  ```
  > 代码可能顺序不完全一致，导致差异不好读
