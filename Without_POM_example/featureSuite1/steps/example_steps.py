# -- FILE: Without_POM_example/steps/example_steps.py
from behave import given, when, then, step, model
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement {number:d} Without_POM_example')
def step_impl(context, number):  # -- NOTE: number is converted into integer
    assert number > 1 or number == 0
    context.tests_count = number

@then('behave will test them for us!')
def step_impl(context):
    assert context.failed is False
    assert context.tests_count >= 0



@given("user open the url")
def step_impl(context):
    path = "C:/Users/Juhi/PycharmProjects/pythonProject/drivers/chromedriver.exe"
    context.driver = webdriver.Chrome(executable_path=path)
    context.driver.maximize_window()
    context.driver.get("http://www.google.com/")
    print(dir(context))
    assert "Google" in context.driver.title
    print("title is : " + context.driver.title)




@when("user search for python")
def step_impl(context):

    'scenario' in context
    context.driver.find_element_by_name("q").click()
    context.driver.find_element_by_xpath("//*[@name='q']").click()
    context.driver.find_element_by_xpath("//*[@name='q']").send_keys("python")
    context.driver.find_element_by_xpath("//*[@name='q']").send_keys(Keys.ENTER)




@step("user select python.or site link")
def step_impl(context):
    context.driver.find_element_by_xpath("//a[@href='https://www.python.org/']").click()


@then('user will be on python.or site and the title should be "Welcome to Python.org"')
def step_impl(context):
    assert "Welcome to Python.org" in context.driver.title
    print("title is : " + context.driver.title)





@given('user open the {url}')
def step_impl(context, url):
    path = "C:/Users/Juhi/PycharmProjects/pythonProject/drivers/chromedriver.exe"
    context.driver = webdriver.Chrome(executable_path=path)
    context.driver.maximize_window()
    context.driver.get(url)
    assert "Google" in context.driver.title
    print("title is : " + context.driver.title)


@when('user search for "{search_text}"')
def step_impl(context, search_text):
    context.driver.find_element_by_name("q").click()
    context.driver.find_element_by_xpath("//*[@name='q']").click()
    context.driver.find_element_by_xpath("//*[@name='q']").send_keys(search_text)
    context.driver.find_element_by_xpath("//*[@name='q']").send_keys(Keys.ENTER)


@step('user select "{link}" site link')
def step_impl(context,link):
    if(link=="wikipedia"):
        context.driver.find_element_by_xpath("//a[@href='https://en.wikipedia.org/wiki/India']").click()
    elif(link=="python.org"):
        context.driver.find_element_by_xpath("//a[@href='https://www.python.org/']").click()


@then('the title should be "{Title}"')
def step_impl(context, Title):
    assert Title in context.driver.title
    print("title is : " + context.driver.title)


# --------------------**************************-------------------------
#----------------------------------------------------------------------------------------------------------------------#
@given('Creating a new variable and assign a value to it')
def find_order_from_db(context):
    print("Creating a new variable and assign a value to it....")
    context.username = 'ABC'
    print("username is: {}".format(context.username))

#----------------------------------------------------------------------------------------------------------------------#
@when('Trying to access the value of userName in second step')
def issue_refund(context):
    print("Trying to access the value of userName in second step: {}".format(context.username))

#----------------------------------------------------------------------------------------------------------------------#
@then('payment should get processed for the user')
def payment_should_process(context):
    print("Payment successfully processed")
    print("Payment is for refund of order number: {}".format(context.order_num))

#----------------------------------------------------------------------------------------------------------------------#
@when('I issue a refund on the same order')
def issue_repeat_refund(context):
    print("Trying to issue refund on same order: {}".format(context.order_num))

#----------------------------------------------------------------------------------------------------------------------#
@then('previous step should fail')
def refund_fails(context):
    print("previous step should fail")


@step("Now I try to update the value of username")
def step_impl(context):
    print("Trying to update the value of userName: {}")
    context.username= 'XYZ'



@then("Updated value of user name is XYZ")
def step_impl(context):
    print("Updated value of user name is : {}".format(context.username))