# Question 1

def hello_name(user_name):
    print("hello_" + user_name + "!")

hello_name("USERNAME")

# Question 2

def first_odds():
    print(list(range(1,101,2)))

first_odds()

# Question 3

def max_num_in_list(a_list):
    a_list = [7, 35, 21, 16, 8, 34]
    print(max(a_list))

max_num_in_list(list)

# Question 4

def is_leap_year(a_year):
    if a_year % 4 == 0:
        return True
    elif a_year % 100 == 0:
        return False
    elif a_year % 400 == 0:
        return True


# Question 5

def is_consecutive(a_list):
    a_list = [20, 24, 22, 23, 21, 25]
    print(sorted(a_list))

is_consecutive(list)
