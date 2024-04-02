from solutions.CHK import checkout_solution

class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout(None) == -1
        assert checkout_solution.checkout('None') == -1
        assert checkout_solution.checkout(0) == -1
        assert checkout_solution.checkout('EFG') == -1


        assert checkout_solution.checkout('AABBAABCD') == 290
