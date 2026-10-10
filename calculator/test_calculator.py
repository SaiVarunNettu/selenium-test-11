import unittest
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By


class CalculatorTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.set_window_size(1280, 1050)

        # Correctly locate index.html in the same folder
        cls.url = Path(__file__).with_name("index.html").resolve().as_uri()

    def setUp(self):
        self.driver.get(self.url)

    def calc(self, a, b, op):
        d = self.driver
        d.find_element(By.ID, "num1").send_keys(str(a))
        d.find_element(By.ID, "num2").send_keys(str(b))
        d.find_element(By.ID, op).click()
        return d.find_element(By.ID, "result").text

    def test_1_page_title(self):
        self.assertEqual(self.driver.title, "Simple Calculator")

    def test_2_addition(self):
        self.assertEqual(self.calc(12, 8, "add"), "Result: 20")

    def test_3_subtraction(self):
        self.assertEqual(self.calc(20, 5, "sub"), "Result: 15")

    def test_4_multiplication(self):
        self.assertEqual(self.calc(6, 7, "mul"), "Result: 42")

    def test_5_division(self):
        self.assertEqual(self.calc(15, 4, "div"), "Result: 3.75")

    def test_6_divide_by_zero(self):
        self.assertEqual(
            self.calc(10, 0, "div"),
            "Error: Cannot divide by zero"
        )

    def test_7_empty_input(self):
        self.driver.find_element(By.ID, "add").click()
        self.assertEqual(
            self.driver.find_element(By.ID, "result").text,
            "Please enter both numbers"
        )

    def test_8_clear_button(self):
        self.calc(3, 4, "add")
        self.driver.find_element(By.ID, "clear").click()

        self.assertEqual(
            self.driver.find_element(By.ID, "num1").get_attribute("value"),
            ""
        )
        self.assertEqual(
            self.driver.find_element(By.ID, "result").text,
            ""
        )

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)