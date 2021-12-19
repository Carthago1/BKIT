from behave import given, when, then
from functions import picture_path

@given("I have the conditions {conditions}")
def data(context, conditions):
    context.c = conditions

@when("I find picture_path")
def perform_func(context):
    context.path = picture_path(context.c)

@then("I expect the result to be {path}")
def expect_result(context, path):
    assert context.path == path