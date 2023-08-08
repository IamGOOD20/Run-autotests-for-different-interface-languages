# Run-autotests-for-different-interface-languages
Implementation of automated testing of various web page interface languages. Using Selenium, Python and PyTest.

## Goal: run autotests for different interface languages
## Tools: Python, PyTest, Seleniuum

### Steps:
1. Create a GitHub repository containing the conftest.py and test_items.py files.
2. Add a handler to the conftest.py file that reads the language parameter from the command line.
3. In the conftest.py file, implement the logic for launching the browser with the specified user language. The browser must be declared in the browser fixture and passed to the test as a parameter.
4. In the test_items.py file, write a test that checks that the product page on the site contains an add to cart button. For example, you can check a product available at http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.
5. The test must be run with the language parameter with the following command:
   pytest --language=es test_items.py


### Verification Criteria
1. The test in the repository can be run with the pytest --language=es command, the test passes successfully.
2. Checking the health of the code for different languages. Add the time.sleep(30) command to the test file immediately
   after opening the link. Run the test with --language=fr and visually check that the phrase on the add to cart button
   looks like this: "Ajouter au panier".
3. The browser must be declared in the browser fixture and passed to the test as a parameter.
4. The test checks for the presence of an add to cart button. The button selector is unique to the page being checked.
   There is assert.
5. The name of the test method inside the test_items.py file corresponds to the task. The name test_something does not
   satisfy the requirements.
