# Django template reconstruction

> code tags: \*chapter4.x

## template in django
1. create folder lists/templates
2. create file home.html in folder templates created above
3. add lists to var `INSTALLED_APPS` in setting.py
```C
INSTALLED_APPS = [
    'django.contrib.admin',
    .....
    'lists'
]
 
```

## 保存用户输入，测试数据库
* 编写表单，发送post请求
  1. 给\<input\>元素指定name=属性
  2. 把它放在<form>标签中，并为标签指定method="post"属性

* 这时跑function_test会报错误
```
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: [id="id_list_table"]
```
* fix `CSRF\(Cross-Site Request Forgery\)`
   + 错误信息
   ![CSRF_FAILURE_VIEW](./doc/csrf_fail.png)
   + Django 针对CSRF保护措施是在每个生成的表单中放置自动生成的令牌，使用模板标签(template tag)
     + syntax: {% ... %}
     + example:
     ```
     <form method="POST">
       <input name="item_text" id="id_new_item" placeholder="Enter a to-do item">
       {% csrf_token %}
     </form>
     ```
 ## 在服务器中处理post 请求
