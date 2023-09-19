End to end Tests for Run.py
For each test there is a folder <number>, which contains:
- <number>.config
- <number>.in
- <number>.out

These tests are run in the tests_e2e.sh script, which is run in the test_all.py script.


Tests
1. Basic board with no special features (testing wsade)

2. Board with equal fire and water 

3. Board with more fire than water (tests losing)

4. Board with more water than fire

5. Board with teleport (test travelling and e)

6. Board with way of leaving map on all sides (water buckets had to be used as a blank row can’t be read in properly by python).

7. Everything together

8. Capital moves (checking you can input capital moves and that the moves list is lowercase regardless)

9. Invalid moves (enters invalid inputs for moves and tests the quit (“q”) functionality)

10. File does not exist

11. No system arguments 


