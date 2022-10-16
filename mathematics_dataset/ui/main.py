import streamlit as st
import random
import time
from fractions import Fraction
import os
from decimal import Decimal
import re

def main():
    file  = open('../output/extrapolate/probability__swr_p_sequence_more_samples.txt','r')

    lines = file.readlines()

    count = 0

    for line in lines:
        count+=1

    odd_lines = []
    even_lines = []

    for i in range(0,count):
        if i%2==0:
            even_lines.append(lines[i])
        else:
            odd_lines.append(lines[i])

    rand = random.randrange(0, count/2)

    st.title('DeepMathematics - Machine Generated Probability Questions')
    st.write(even_lines[rand])

    number = st.text_input("Enter the fraction as a/b")
    button = st.button(label="Submit")

        
    correct_frac = (odd_lines[rand].strip('\n'))

    st.session_state.correct_frac = correct_frac
    st.session_state.correct_frac = number

    if not number:
        return st.write("Please enter a fraction")
        

        


    if button:
            if number == st.session_state.correct_frac:
                    st.success("Correct")
                    button_move_on = st.button(label="Next Question")
                    while button_move_on == True:
                        os.system('rm -rf mathematics_dataset/output')
                        os.system('python3 -m mathematics_dataset.generate_to_file --output_dir=mathematics_dataset/output/')
                        file2  = open('../output/extrapolate/probability__swr_p_sequence_more_samples.txt','r')
                        lines2 = file2.readlines()
                        count2 = 0

                        for line2 in lines2:
                            count2+=1

                        odd_lines_2 = []
                        even_lines_2 = []

                        for i in range(0,count2):
                            if i%2==0:
                                even_lines_2.append(lines[i])
                            else:
                                odd_lines_2.append(lines[i])

                        rand2 = random.randrange(0, count2/2)
                        st.write(even_lines_2[rand2])
                        number_2 = st.text_input("Enter the fraction as a/b")
                        button_2 = st.button(label="Submit")
                        correct_frac_2 = (odd_lines_2[rand2].strip('\n'))
                        st.session_state.correct_frac_2 = correct_frac_2
                        st.session_state.correct_frac_2 = number_2
                        if button_2:
                            if number_2 == st.session_state.correct_frac_2:
                                st.success("Correct")
                                button_move_on = st.button(label="Next Question")
                                return button_move_on
                            else:
                                st.error("Incorrect")
                                st.write("The correct answer is: ", correct_frac_2)
                                break



                        
                        
                        

            else:
                st.write("Incorrect")
                st.stop()


if __name__ == '__main__':
    main()



