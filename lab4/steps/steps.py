from behave import given, when, then
from qr import get_roots


@given("I have the coefficients {number1:g}, {number2:g} and {number3:g}")
def have_numbers(context, number1, number2, number3):
    context.number1 = number1
    context.number2 = number2
    context.number3 = number3

@when("I calculate them")
def calculate_roots(context):
    context.result = get_roots(context.number1, context.number2, context.number3)

@then("I expect the result to be {result}")
def expect_result(context, result):
    assert context.result == list(map(int, result.split(',')))
