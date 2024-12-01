# Budget Project

This project is an app where the user can set different categories, search their information and track their expenses in each one.

In order to do so, I created three different but connected files:
- **budget**: where the structure of the project is defined
- **budget.project**: where the functionality of the project is (specific behaviours are added) 
- **test_budget**: where the code is tested (this file has just a few lines, see "Future improvements")

## Future improvements:
- Create error handling and exceptions in order to consider that the user might enter a float instead of an integer
- Add a functionality to **spending_limit_for_alert** where the user gets a print statement if they spent more or equal money to it in the corresponding  category
- I still can not get my **test_budget** to work. I structured everything based on this: https://doc.pytest.org/en/latest/explanation/goodpractices.html#tests-outside-application-code but it still doesn't work.
- Add tests to the **test_budget** file to test all the code
