from behave import given, when, then


@given('Open the sign_in page')
def open_sign_in(context):
    context.app.sign_in_page.open_sign_in()

@when("Log in to the page with valid credentials: '{your_emai}', '{your_password}'")
def log_in(context, your_emai, your_password):
    context.app.sign_in_page.log_in(your_emai, your_password)