from solutions.CHK import checkout_solution

class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout('None') == -1
        assert checkout_solution.checkout('') == 0

        assert checkout_solution.checkout('EEB') == 80
        assert checkout_solution.checkout('EEEB') == 120
        assert checkout_solution.checkout('EEEEBB') == 160
        assert checkout_solution.checkout('BEBEEE') == 160

        assert checkout_solution.checkout('AABBAABCD') == 290
        assert checkout_solution.checkout('AABBAABCDEE') == 340
        assert checkout_solution.checkout('AABBAAABCDEE') == 360
        assert checkout_solution.checkout('AABBAAAABCDEE') == 410
        assert checkout_solution.checkout('AABBAAAAAABCDEE') == 490

        assert checkout_solution.checkout('FF') == 20
        assert checkout_solution.checkout('FFF') == 20
        assert checkout_solution.checkout('FFFF') == 30
        assert checkout_solution.checkout('FFFFF') == 40
        assert checkout_solution.checkout('FFFFFF') == 40
        assert checkout_solution.checkout('FFFFFFF') == 50

        assert checkout_solution.checkout('AABBAABCDFF') == 310
        assert checkout_solution.checkout('AABBAABCDEEFFF') == 360
        assert checkout_solution.checkout('AABBAAABCDEEFFFF') == 390
        assert checkout_solution.checkout('AABBAAAABCDEEFFFFF') == 450
        assert checkout_solution.checkout('AABBAAAAAABCDEEFFFFFF') == 530
        

