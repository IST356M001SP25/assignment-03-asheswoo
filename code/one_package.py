'''
Write a streamlit to input one string of package data. 
It should use the `packaging.py` module to parse the string 
and output the package info as it appears. 
Calculate the total package size and display that.

see one_package.png for a screenshot
'''
import streamlit as st
from packaging import parse_packaging, calc_total_units, get_unit

st.title("Package Data Parser")

package_data = st.text_input("Enter package data (e.g., '12 eggs in 1 carton / 3 cartons in 1 box'):")

if package_data:
    package = parse_packaging(package_data)
    
    st.write("Package Info:")
    for item in package:
        for key, value in item.items():
            st.write(f"{key}: {value}")
    
    total_units = calc_total_units(package)
    unit = get_unit(package)
    st.write(f"Total Size: {total_units} {unit}")