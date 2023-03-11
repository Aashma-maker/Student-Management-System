from Computing import *
import unittest


class TestComputing(unittest.TestCase):
    def test_quick_sort(self):
        # test of quick sort that sort the array in the ascending order
        array_to_sort = [(1, 'Sanjit', 'Lama', '9810310691', 'Jorpati', datetime.date(2002, 11, 23), 'Male',
                          'BSc. Computing'),
                         (2, 'Reema', 'Lama', '9840274493', 'Jorpati', datetime.date(2000, 10, 4), 'Female',
                          'BSc. Ethical Hacking'),
                         (3, 'Shila', 'Lama', '98013754888', 'Dhumbarahi', datetime.date(1998, 3, 5), 'Female',
                          'BSc. Ethical Hacking')]

        user.combo_sort.set('Id')
        user.quick_sort(array_to_sort, 0, len(array_to_sort) - 1)
        expected_result = [(1, 'Sanjit', 'Lama', '9810310691', 'Jorpati', datetime.date(2002, 11, 23), 'Male',
                            'BSc. Computing'),
                           (2, 'Reema', 'Lama', '9840274493', 'Jorpati', datetime.date(2000, 10, 4), 'Female',
                            'BSc. Ethical Hacking'),
                           (3, 'Shila', 'Lama', '98013754888', 'Dhumbarahi', datetime.date(1998, 3, 5), 'Female',
                            'BSc. Ethical Hacking')]
        self.assertEqual(array_to_sort, expected_result)

        user.combo_sort.set('First Name')
        user.quick_sort(array_to_sort, 0, len(array_to_sort) - 1)
        expected_result = [(1, 'Sanjit', 'Lama', '9810310691', 'Jorpati', datetime.date(2002, 11, 23), 'Male',
                            'BSc. Computing'),
                           (3, 'Shila', 'Lama', '98013754888', 'Dhumbarahi', datetime.date(1998, 3, 5), 'Female',
                            'BSc. Ethical Hacking'),
                           (2, 'Reema', 'Lama', '9840274493', 'Jorpati', datetime.date(2000, 10, 4), 'Female',
                            'BSc. Ethical Hacking')]
        self.assertEqual(array_to_sort, expected_result)

        user.combo_sort.set('Last Name')
        user.quick_sort(array_to_sort, 0, len(array_to_sort) - 1)
        expected_result = [(2, 'Reema', 'Lama', '9840274493', 'Jorpati', datetime.date(2000, 10, 4), 'Female',
                            'BSc. Ethical Hacking'),
                           (3, 'Shila', 'Lama', '98013754888', 'Dhumbarahi', datetime.date(1998, 3, 5), 'Female',
                            'BSc. Ethical Hacking'),
                           (1, 'Sanjit', 'Lama', '9810310691', 'Jorpati', datetime.date(2002, 11, 23), 'Male',
                            'BSc. Computing'),]
        self.assertEqual(array_to_sort, expected_result)

        user.combo_sort.set('Contact')
        user.quick_sort(array_to_sort, 0, len(array_to_sort) - 1)
        expected_result = [(3, 'Shila', 'Lama', '98013754888', 'Dhumbarahi', datetime.date(1998, 3, 5), 'Female',
                           'BSc. Ethical Hacking'),
                           (1, 'Sanjit', 'Lama', '9810310691', 'Jorpati', datetime.date(2002, 11, 23), 'Male',
                            'BSc. Computing'),
                           (2, 'Reema', 'Lama', '9840274493', 'Jorpati', datetime.date(2000, 10, 4), 'Female',
                            'BSc. Ethical Hacking')]
        self.assertEqual(array_to_sort, expected_result)

        user.combo_sort.set('Address')
        user.quick_sort(array_to_sort, 0, len(array_to_sort) - 1)
        expected_result = [(2, 'Reema', 'Lama', '9840274493', 'Jorpati', datetime.date(2000, 10, 4), 'Female',
                           'BSc. Ethical Hacking'),
                           (3, 'Shila', 'Lama', '98013754888', 'Dhumbarahi', datetime.date(1998, 3, 5), 'Female',
                            'BSc. Ethical Hacking'),
                           (1, 'Sanjit', 'Lama', '9810310691', 'Jorpati', datetime.date(2002, 11, 23), 'Male',
                            'BSc. Computing'),]
        self.assertEqual(array_to_sort, expected_result)

        user.combo_sort.set('Date of Birth')
        user.quick_sort(array_to_sort, 0, len(array_to_sort) - 1)
        expected_result = [(3, 'Shila', 'Lama', '98013754888', 'Dhumbarahi', datetime.date(1998, 3, 5), 'Female',
                           'BSc. Ethical Hacking'),
                           (1, 'Sanjit', 'Lama', '9810310691', 'Jorpati', datetime.date(2002, 11, 23), 'Male',
                            'BSc. Computing'),
                           (2, 'Reema', 'Lama', '9840274493', 'Jorpati', datetime.date(2000, 10, 4), 'Female',
                            'BSc. Ethical Hacking')]
        self.assertEqual(array_to_sort, expected_result)

        user.combo_sort.set('Gender')
        user.quick_sort(array_to_sort, 0, len(array_to_sort) - 1)
        expected_result = [(3, 'Shila', 'Lama', '98013754888', 'Dhumbarahi', datetime.date(1998, 3, 5), 'Female',
                           'BSc. Ethical Hacking'),
                           (2, 'Reema', 'Lama', '9840274493', 'Jorpati', datetime.date(2000, 10, 4), 'Female',
                            'BSc. Ethical Hacking'),
                           (1, 'Sanjit', 'Lama', '9810310691', 'Jorpati', datetime.date(2002, 11, 23), 'Male',
                            'BSc. Computing')]
        self.assertEqual(array_to_sort, expected_result)

        user.combo_sort.set('Degree')
        user.quick_sort(array_to_sort, 0, len(array_to_sort) - 1)
        expected_result = [(1, 'Sanjit', 'Lama', '9810310691', 'Jorpati', datetime.date(2002, 11, 23), 'Male',
                           'BSc. Computing'),
                           (2, 'Reema', 'Lama', '9840274493', 'Jorpati', datetime.date(2000, 10, 4), 'Female',
                            'BSc. Ethical Hacking'),
                           (3, 'Shila', 'Lama', '98013754888', 'Dhumbarahi', datetime.date(1998, 3, 5), 'Female',
                            'BSc. Ethical Hacking')]
        self.assertEqual(array_to_sort, expected_result)

        # test of quick sort that sort the array in the descending order
        array_to_sort = [(1, 'Sanjit', 'Lama', '9810310691', 'Jorpati', datetime.date(2002, 11, 23), 'Male',
                          'BSc. Computing'),
                         (2, 'Reema', 'Lama', '9840274493', 'Jorpati', datetime.date(2000, 10, 4), 'Female',
                          'BSc. Ethical Hacking'),
                         (3, 'Shila', 'Lama', '98013754888', 'Dhumbarahi', datetime.date(1998, 3, 5), 'Female',
                          'BSc. Ethical Hacking')]

        user.combo_sort.set('Id')
        user.radio_descending.invoke()
        user.quick_sort(array_to_sort, 0, len(array_to_sort) - 1)
        expected_result = [(3, 'Shila', 'Lama', '98013754888', 'Dhumbarahi', datetime.date(1998, 3, 5), 'Female',
                           'BSc. Ethical Hacking'),
                           (2, 'Reema', 'Lama', '9840274493', 'Jorpati', datetime.date(2000, 10, 4), 'Female',
                            'BSc. Ethical Hacking'),
                           (1, 'Sanjit', 'Lama', '9810310691', 'Jorpati', datetime.date(2002, 11, 23), 'Male',
                            'BSc. Computing'),]
        self.assertEqual(array_to_sort, expected_result)

        user.combo_sort.set('First Name')
        user.quick_sort(array_to_sort, 0, len(array_to_sort) - 1)
        expected_result = [(2, 'Reema', 'Lama', '9840274493', 'Jorpati', datetime.date(2000, 10, 4), 'Female',
                            'BSc. Ethical Hacking'),
                           (3, 'Shila', 'Lama', '98013754888', 'Dhumbarahi', datetime.date(1998, 3, 5), 'Female',
                            'BSc. Ethical Hacking'),
                           (1, 'Sanjit', 'Lama', '9810310691', 'Jorpati', datetime.date(2002, 11, 23), 'Male',
                            'BSc. Computing')]
        self.assertEqual(array_to_sort, expected_result)

        user.combo_sort.set('Last Name')
        user.quick_sort(array_to_sort, 0, len(array_to_sort) - 1)
        expected_result = [(1, 'Sanjit', 'Lama', '9810310691', 'Jorpati', datetime.date(2002, 11, 23), 'Male',
                           'BSc. Computing'),
                           (3, 'Shila', 'Lama', '98013754888', 'Dhumbarahi', datetime.date(1998, 3, 5), 'Female',
                           'BSc. Ethical Hacking'),
                           (2, 'Reema', 'Lama', '9840274493', 'Jorpati', datetime.date(2000, 10, 4), 'Female',
                            'BSc. Ethical Hacking')]
        self.assertEqual(array_to_sort, expected_result)

        user.combo_sort.set('Contact')
        user.quick_sort(array_to_sort, 0, len(array_to_sort) - 1)
        expected_result = [(2, 'Reema', 'Lama', '9840274493', 'Jorpati', datetime.date(2000, 10, 4),'Female',
                            'BSc. Ethical Hacking'),
                           (1, 'Sanjit', 'Lama', '9810310691', 'Jorpati', datetime.date(2002, 11, 23), 'Male',
                            'BSc. Computing'),
                           (3, 'Shila', 'Lama', '98013754888', 'Dhumbarahi', datetime.date(1998, 3, 5), 'Female',
                            'BSc. Ethical Hacking')]
        self.assertEqual(array_to_sort, expected_result)

        user.combo_sort.set('Address')
        user.quick_sort(array_to_sort, 0, len(array_to_sort) - 1)
        expected_result = [(1, 'Sanjit', 'Lama', '9810310691', 'Jorpati', datetime.date(2002, 11, 23), 'Male',
                           'BSc. Computing'),
                           (3, 'Shila', 'Lama', '98013754888', 'Dhumbarahi', datetime.date(1998, 3, 5), 'Female',
                            'BSc. Ethical Hacking'),
                           (2, 'Reema', 'Lama', '9840274493', 'Jorpati', datetime.date(2000, 10, 4), 'Female',
                            'BSc. Ethical Hacking')]
        self.assertEqual(array_to_sort, expected_result)

        user.combo_sort.set('Date of Birth')
        user.quick_sort(array_to_sort, 0, len(array_to_sort) - 1)
        expected_result = [(2, 'Reema', 'Lama', '9840274493', 'Jorpati', datetime.date(2000, 10, 4),'Female',
                            'BSc. Ethical Hacking'),
                           (1, 'Sanjit', 'Lama', '9810310691', 'Jorpati', datetime.date(2002, 11, 23), 'Male',
                            'BSc. Computing'),
                           (3, 'Shila', 'Lama', '98013754888', 'Dhumbarahi', datetime.date(1998, 3, 5), 'Female',
                            'BSc. Ethical Hacking')]
        self.assertEqual(array_to_sort, expected_result)

        user.combo_sort.set('Gender')
        user.quick_sort(array_to_sort, 0, len(array_to_sort) - 1)
        expected_result = [(1, 'Sanjit', 'Lama', '9810310691', 'Jorpati', datetime.date(2002, 11, 23), 'Male',
                           'BSc. Computing'),
                           (2, 'Reema', 'Lama', '9840274493', 'Jorpati', datetime.date(2000, 10, 4), 'Female',
                            'BSc. Ethical Hacking'),
                           (3, 'Shila', 'Lama', '98013754888', 'Dhumbarahi', datetime.date(1998, 3, 5), 'Female',
                            'BSc. Ethical Hacking')]
        self.assertEqual(array_to_sort, expected_result)

        user.combo_sort.set('Degree')
        user.quick_sort(array_to_sort, 0, len(array_to_sort) - 1)
        expected_result = [(2, 'Reema', 'Lama', '9840274493', 'Jorpati', datetime.date(2000, 10, 4),'Female',
                            'BSc. Ethical Hacking'),
                           (3, 'Shila', 'Lama', '98013754888', 'Dhumbarahi', datetime.date(1998, 3, 5), 'Female',
                            'BSc. Ethical Hacking'),
                           (1, 'Sanjit', 'Lama', '9810310691', 'Jorpati', datetime.date(2002, 11, 23), 'Male',
                            'BSc. Computing')]
        self.assertEqual(array_to_sort, expected_result)

    def test_search(self):
        user.radio_ascending.invoke()
        user.combo_sort.set('Id')
        array_containing_data = [(1, 'Sanjit', 'Lama', '9810310691', 'Jorpati', datetime.date(2002, 11, 23), 'Male',
                                  'BSc. Computing'),
                                 (2, 'Reema', 'Lama', '9840274493', 'Jorpati', datetime.date(2000, 10, 4),'Female',
                                  'BSc. Ethical Hacking'),
                                 (3, 'Shila', 'Lama', '98013754888', 'Dhumbarahi', datetime.date(1998, 3, 5), 'Female',
                                  'BSc. Ethical Hacking'),
                                 (4, 'Ashish', 'Lama', '9849651205', 'Gyaneshwor', datetime.date(1993, 12, 23), 'Male',
                                  'Medical IT'),
                                 (5, 'Shahil', 'Tamang', '9808283763', 'Sikim', datetime.date(1997, 5, 4), 'Male',
                                  'Doctor'),
                                 (6, 'Bikash', 'Lama', '9854210234', 'Harion', datetime.date(1999, 9, 2), 'Male',
                                  'BSc. Computing'),
                                 (7, 'Bijay', 'Lama', '9808001106', 'Hadigaun', datetime.date(1990, 5, 2), 'Male',
                                  'Commerce'),
                                 (8, 'Anishma', 'Lama', '9841378042', 'Bouddha', datetime.date(1989, 4, 10), 'Female',
                                  'Nurse'),
                                 (9, 'Sidhant', 'Ghising', '9808168899', 'Balaju', datetime.date(1999, 10, 7), 'Male',
                                  'Computer Science')]
        # Searching through ID
        user.entry_search.delete(0, END)
        user.entry_search.insert(0, 4)
        user.combo_search.set('Id')
        final = user.search(array_containing_data)
        expected_result = [(4, 'Ashish', 'Lama', '9849651205', 'Gyaneshwor', datetime.date(1993, 12, 23), 'Male',
                            'Medical IT')]
        self.assertEqual(final, expected_result)

        # Searching through Last Name
        user.entry_search.delete(0, END)
        user.entry_search.insert(0, 'Lama')
        user.combo_search.set('Last Name')
        final = user.search(array_containing_data)
        expected_result = [(1, 'Sanjit', 'Lama', '9810310691', 'Jorpati', datetime.date(2002, 11, 23), 'Male',
                           'BSc. Computing'),
                           (2, 'Reema', 'Lama', '9840274493', 'Jorpati', datetime.date(2000, 10, 4),
                            'Female', 'BSc. Ethical Hacking')]
        self.assertEqual(final, expected_result)

        # Searching through First Name
        user.entry_search.delete(0, END)
        user.entry_search.insert(0, 'Shahil')
        user.combo_search.set('First Name')
        final = user.search(array_containing_data)
        expected_result = [(5, 'Shahil', 'Tamang', '9808283763', 'Sikim', datetime.date(1997, 5, 4), 'Male',
                            'Doctor')]
        self.assertEqual(final, expected_result)

        # Searching through ID
        user.entry_search.delete(0, END)
        user.entry_search.insert(0, '')
        user.combo_search.set('Id')
        final = user.search(array_containing_data)
        expected_result = None
        self.assertEqual(final, expected_result)

        # Searching through Contact
        user.entry_search.delete(0, END)
        user.entry_search.insert(0, '9808001106')
        user.combo_search.set('Contact')
        final = user.search(array_containing_data)
        expected_result = [(7, 'Bijay', 'Lama', '9808001106', 'Hadigaun', datetime.date(1990, 5, 2), 'Male',
                            'Commerce')]
        self.assertEqual(final, expected_result)

        # Searching through Gender
        user.entry_search.delete(0, END)
        user.entry_search.insert(0, 'Male')
        user.combo_search.set('Gender')
        final = user.search(array_containing_data)
        expected_result = [(1, 'Sanjit', 'Lama', '9810310691', 'Jorpati', datetime.date(2002, 11, 23), 'Male',
                           'BSc. Computing'),
                           (4, 'Ashish', 'Lama', '9849651205', 'Gyaneshwor', datetime.date(1993, 12, 23), 'Male',
                            'Medical IT'),
                           (5, 'Shahil', 'Tamang', '9808283763', 'Sikim', datetime.date(1997, 5, 4), 'Male',
                            'Doctor'),
                           (6, 'Bikash', 'Lama', '9854210234', 'Harion', datetime.date(1999, 9, 2), 'Male',
                            'BSc. Computing'),
                           (7, 'Bijay', 'Lama', '9808001106', 'Hadigaun', datetime.date(1990, 5, 2), 'Male',
                            'Commerce'),
                           (9, 'Sidhant', 'Ghising', '9808168899', 'Balaju', datetime.date(1999, 10, 7), 'Male',
                            'Computer Science')]
        self.assertEqual(final, expected_result)

        # Searching through Degree
        user.entry_search.delete(0, END)
        user.entry_search.insert(0, 'Commerce', 'Computer Science')
        user.combo_search.set('Degree')
        final = user.search(array_containing_data)
        expected_result = [(7, 'Bijay', 'Lama', '9808001106', 'Hadigaun', datetime.date(1990, 5, 2), 'Male',
                            'Commerce'),
                           (9, 'Sidhant', 'Ghising', '9808168899', 'Balaju', datetime.date(1999, 10, 7), 'Male',
                            'Computer Science')]
        self.assertEqual(final, expected_result)

        # Searching through Date of birth
        user.entry_search.delete(0, END)
        user.entry_search.insert(0, f'{datetime.date(1998, 3, 5)}')
        user.combo_search.set('Date of Birth')
        final = user.search(array_containing_data)
        expected_result = [(3, 'Shila', 'Lama', '98013754888', 'Dhumbarahi', datetime.date(1998, 3, 5), 'Female',
                           'BSc. Ethical Hacking')]
        self.assertEqual(final, expected_result)

    def test_clear(self):
        user.entry_id.insert(0, 4999)
        user.entry_f_name.insert(0, 'Kushal')
        user.entry_l_name.insert(0, 'Tamang')
        user.entry_address.insert(0, 'Gongabu')
        user.entry_contact.insert(0, '9810286286')
        user.radio_custom.invoke()
        user.combo_degree.set('BSc. Computing')
        user.combo_day.set(5)
        user.combo_month.set(11)
        user.combo_year.set(1993)

        user.clear()

        self.assertEqual(user.entry_id.get(), '')
        self.assertEqual(user.entry_f_name.get(), '')
        self.assertEqual(user.entry_l_name.get(), '')
        self.assertEqual(user.entry_address.get(), '')
        self.assertEqual(user.entry_contact.get(), '')
        self.assertEqual(user.gender.get(), 'Male')
        self.assertEqual(user.combo_degree.get(), 'BSc. Computing')
        self.assertEqual(user.combo_day.get(), str(user.dt.day))
        self.assertEqual(user.combo_month.get(), str(user.dt.month))
        self.assertEqual(user.combo_year.get(), str(user.dt.year))


if __name__ == '__main__':
    user = User()
    unittest.main()

