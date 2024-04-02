from solutions.CHK import checkout_solution

class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout('None') == -1
        assert checkout_solution.checkout('EFG') == -1
        assert checkout_solution.checkout('') == 0
        print(checkout_solution.checkout('AABBAABCDEE'))

        assert checkout_solution.checkout('AABBAABCD') == 290
        assert checkout_solution.checkout('AABBAABCDEE') == 340
        assert checkout_solution.checkout('AABBAAABCDEE') == 360
        assert checkout_solution.checkout('AABBAAAABCDEE') == 410
        assert checkout_solution.checkout('AABBAAAAAABCDEE') == 540


