page类命名规范：
1.每一个页面封装为一个模块，模块名首字母小写，用_连接；比如：home_page.py
2.每一个页面只包含一个类，类名英文首字母大写，不用_符号，比如 class HomePage(self):

3.每一个类有两层封装，元素封装规范：
①元素封装，返回类型统一为element，定位器分离，需要添加注释；比如：

    #"我的"按钮  元素
    @property
    def el_my_btn(self):
        return self.new_find_element(By.NAME,u'我的')
②元素封装的方法名，以el_开头,如果是button型元素就用btn后缀，如果是输入框型元素就用_text_input后缀
③元组封装统一加@property装饰器

4.第二层封装，逻辑封装：
    def logic_login(self,phone,pwd):
        self.el_my_btn.click()
        self.el_phone_text_input.send_keys(phone)
        self.el_pwd_text_input.send_keys(pwd)
        self.el_login_btn.click()
        return MyPage(self.driver)
①该页面的常用操作都 封装在业务逻辑方法里.
②逻辑封装的方法名，都以 logic_开头命名。
*③ 如果跳转到另一个页面，返回值是另一个页面类的实例，入参self.driver




