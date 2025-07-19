from behave import given, when, then


@then('Verify the right page opens')
def verify_page_opens(context):
    context.app.community_page.verify_page_opens()

@then('Verify the “Contact support” button is available and clickable')
def verify_contact_support(context):
    context.app.community_page.verify_contact_support()