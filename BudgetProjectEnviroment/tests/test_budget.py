#This doesn't get imported. See Future Improvement in the README file

from budget import Category


def test_when_tracking_expense_that_does_not_exceed_limit_then_amount_spent_is_updated():
    # Given
    category = Category("leisure", 25, 20)
    # When
    category.track_amount_spent(10)
    # Then
    assert category.amount_spent == 10

def test_when_tracking_expense_that_does_exceed_limit_amount_spent_is_updated():
    # Given
    category = Category("leisure", 25, 20)
    # When
    category.track_amount_spent(30)
    # Then
    assert category.amount_spent == 30

def test_when_tracking_expense_that_does_not_exceed_limit_returns_true():
    # Given
    category = Category("leisure", 25, 20)
    # When
    is_amount_spent_smaller_or_equal_to_max_allowed_spending = category.track_amount_spent(10)
    # Then
    assert is_amount_spent_smaller_or_equal_to_max_allowed_spending == True

def test_when_tracking_expense_that_does_exceed_limit_returns_false():
    # Given
    category = Category("leisure", 25, 20)
    # When
    is_amount_spent_smaller_or_equal_to_max_allowed_spending = category.track_amount_spent(30)
    # Then
    assert is_amount_spent_smaller_or_equal_to_max_allowed_spending == False
