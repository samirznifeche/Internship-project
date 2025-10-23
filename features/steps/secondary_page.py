from behave import given, when, then


@then('Verify the Secondary page opens')
def verify_page(context):
    context.app.secondary_page.verify_page()

@when('Click on Filters')
def click_filters(context):
    context.app.secondary_page.click_filters()

@when('Filer the products by "want to sell"')
def filter_by_want_to_sell(context):
    context.app.secondary_page.filter_by_want_to_sell()

@when('Click on Apply Filter')
def click_apply_filter(context):
    context.app.secondary_page.click_apply_filter()

@then('Verify all cards have "for sale" tag')
def verify_sell_tag(context):
    context.app.secondary_page.verify_sell_tag()