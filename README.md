Inside selenium-lab, create the calculator folder with index.html and calc.js.
Open calculator/index.html in Chrome and try a few calculations manually.
Create test_calculator.py in calculator folder.
Activate the virtual environment python3 -m venv .venv ==> source .venv/bin/activate ==> python -m pip install selenium and run python test_calculator.py.
Observe Chrome opening and running every test; note the summary in the terminal.
To see a failing test, change the expected value in test_2_addition to "Result: 21", rerun, note the FAIL and AssertionError
