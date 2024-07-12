from project import check_length_alpha, round_tries, validate
import pytest


def test_check_length_alpha():
   assert check_length_alpha("apple") == True
   assert check_length_alpha("toolong") == False
   assert check_length_alpha("guess") == True
   assert check_length_alpha("appl?") == False
   assert check_length_alpha("12345") == False
   assert check_length_alpha("tooshort") == False

def test_round_tries():
   assert round_tries(1) == 2
   assert round_tries(2) == 3
   assert round_tries(3) == 4
   assert round_tries(4) == 5

def test_validate():
   assert validate("words", "words") == "🟢🟢🟢🟢🟢"
   assert validate("worst", "words") == "🟢🟢🟢🟡🔴"
   assert validate("apple", "words") == "🔴🔴🔴🔴🔴"
   assert validate("sword", "words") == "🟡🟡🟡🟡🟡"
