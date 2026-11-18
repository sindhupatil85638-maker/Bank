from bank import bankoper

def test_deposit():
    totalBalance,updatedBalance = banloper(20000,30000,0)

    assert totalBalance ==230000
    assert updatedBalance ==230000

def test_withdraw():
    totalBalance,updatedBalance = bankoper(10000,4000.10000)

    assert totalBalance == 140000
    assert updatedBalance ==130000

    def test_anyamount():
        totalBalance ,updatedBalance = banloper(150000,0,15000)

        assert totalBalance == 150000
        assert updatedBalance == 13500