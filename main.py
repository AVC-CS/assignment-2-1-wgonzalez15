def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    # Taking user input for the number of males and females
    num_males = int(input("Enter the number of male students: "))
    num_females = int(input("Enter the number of female students: "))

    # Calculating the total number of students
    total_students = num_males + num_females

    # Calculating the percentages
    m_perc = (num_males / total_students) * 100
    f_perc = (num_females / total_students) * 100

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    # Displaying the percentages
    print(f"Total number of students: {total_students}")
    print(f"Percentage of male students: {m_perc:.2f}%")
    print(f"Percentage of female students: {f_perc:.2f}%")
    return m_perc, f_perc


if __name__ == '__main__':
    main()
