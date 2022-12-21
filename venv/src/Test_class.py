'''
To run test using command:
    pytest Test_class.py
    or
    pytest Test_class.py -v
'''
class Test_string:
    def test_char_in_string(self):
        str = "Test char in string"
        assert 't' in str

    def test_substring_in_string(self):
        str = "Test sub string in string"
        assert "sub" in str

    def test_number_in_string(self):
        str = "Test number in string"
        assert "10" in str