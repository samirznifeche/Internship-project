from behave import given, when, then


@when('Click on the settings option')
def click_settings(context):
    context.app.main_page.click_settings()

@when('Click Menu button')
def click_menu(context):
    context.app.main_page.click_menu()

@when('Click on "Secondary" option at the left side menu')
def click_secondary_option(context):
    context.app.main_page.click_secondary_option()