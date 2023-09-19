#! /usr/bin/env sh
echo "##########################"
echo "### Running e2e tests! ###"
echo "##########################\n"
count = 0 # number of test cases run so far

# Assume all `.in` and `.out` files are located in a separate `e2e_tests` directory

# Loops through all folders in e2e_tests directory
for folder in `ls -d e2e_tests/*/ | sort -V`; do
    name=$(basename "$folder")
    
    echo Running test $name.

    config_file=e2e_tests/$name/$name.config
    expected_file=e2e_tests/$name/$name.out
    in_file=e2e_tests/$name/$name.in

    # Runs the run.py script with the <number>.config board and <number>.in as input. 
    # The output is then compared to <number>.out
    python3 run.py $config_file < $in_file | diff - $expected_file || echo "Test $name: failed!\n"

    count=$((count+1))
done

echo Running test 11.
python3 run.py | diff - e2e_tests/11.out

echo "Finished running $((count+1)) tests!"
