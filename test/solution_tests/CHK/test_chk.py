from solutions.CHK import checkout_solution

class TestCheckout():
    def test_checkout(self):
        # assert checkout_solution.checkout('None') == -1
        # assert checkout_solution.checkout('') == 0

        assert checkout_solution.checkout('SXZ') == 45
        assert checkout_solution.checkout('STXSTX') == 90
        assert checkout_solution.checkout('STXSTXZ') == 21

        assert checkout_solution.checkout('EEB') == 80
        assert checkout_solution.checkout('EEEB') == 120
        # assert checkout_solution.checkout('EEEEBB') == 160
        # assert checkout_solution.checkout('BEBEEE') == 160

        # assert checkout_solution.checkout('AABBAABCD') == 290
        # assert checkout_solution.checkout('AABBAABCDEE') == 340
        # assert checkout_solution.checkout('AABBAAABCDEE') == 360
        # assert checkout_solution.checkout('AABBAAAABCDEE') == 410
        # assert checkout_solution.checkout('AABBAAAAAABCDEE') == 490

        # assert checkout_solution.checkout('QQ') == 60
        # assert checkout_solution.checkout('QQQ') == 80

        # assert checkout_solution.checkout('RRR') == 150
        # assert checkout_solution.checkout('RRRQV') == 200
        # assert checkout_solution.checkout('RRRQVV') == 240
        # assert checkout_solution.checkout('RRRQVVV') == 280

        # assert checkout_solution.checkout('FF') == 20
        # assert checkout_solution.checkout('FFF') == 20
        # assert checkout_solution.checkout('FFFF') == 30
        # assert checkout_solution.checkout('FFFFF') == 40
        # assert checkout_solution.checkout('FFFFFF') == 40
        # assert checkout_solution.checkout('FFFFFFF') == 50

        # assert checkout_solution.checkout('AABBAABCDFF') == 310
        # assert checkout_solution.checkout('AABBAABCDEEFFF') == 360
        # assert checkout_solution.checkout('AABBAAABCDEEFFFF') == 390
        # assert checkout_solution.checkout('AABBAAAABCDEEFFFFF') == 450
        # assert checkout_solution.checkout('AABBAAAAAABCDEEFFFFFF') == 530

        # assert checkout_solution.checkout('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 853
        # assert checkout_solution.checkout('U') == 40

        



