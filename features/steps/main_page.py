from behave import given, when, then


@when('Click on the settings option')
def click_settings(context):
    context.app.main_page.click_settings()