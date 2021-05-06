# Django and TDD basic

## step1 create function test
1. create function_test.py
2. check the error running function_test.py
  the error message in spyder is:
```
WebDriverException: Reached error page: about:neterror?e=connectionFailure&u=http%3A//localhost%3A8000/&c=UTF-8&d=Firefox%20%E6%97%A0%E6%B3%95%E5%BB%BA%E7%AB%8B%E5%88%B0%20localhost%3A8000%20%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%9A%84%E8%BF%9E%E6%8E%A5%E3%80%82
```
3. start a Django project
  - cmd
  ```
  $ django-admin.py startproject superlists
  ```
4. 启动Django服务器
  - cmd
  ```C
  python manage.py runserver
  ```
5. 跑功能测试
  - cmd
  ```C
  python function_test.py
  ```
## step2 create unit test
1. create application with django
  - cmd
  ```
  $ python manage.py startup lists
  ```
> **difference between functional test and unit test**
> - functional test define test from user point of view
> - unit test defines tests from programmer point of view

> 通常 功能测试 和单元测试在TDD中同时使用，大致流程
> 1. 先写`功能测试`，从用户角度描述应用的新功能
> 2. 先想办法让`功能测试`通过。
> 3. 使用1个或多个`单元测试`定义代码实现的效果。保证为应用的每一行代码(至少)编写一个单元测试。
> 4. 单元测试失败，编写最少量应用代码，刚好让单元测试通过。在2~4步之间反复多次
> 5. 然后，再次运行功能测试，看能否通过。

### test chapter3
with 
```
File "C:\xxx\python_tdd\chapter01\superlists\superlists\urls.py", line 20, in <module>
    url(r'^$', views.home_page, name='home'),
  File "C:\xxxx\anaconda3\lib\site-packages\django\conf\urls\__init__.py", line 85, in url
    raise TypeError('view must be a callable or a list/tuple in the case of include().')
TypeError: view must be a callable or a list/tuple in the case of include().
```

## 为视图编写单元测试
