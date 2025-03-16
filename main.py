import streamlit as st
from pint import UnitRegistry

def convert_units(value, from_unit, to_unit):
    ureg = UnitRegistry()
    try:
        converted_value = (value * ureg(from_unit)).to(to_unit)
        return converted_value.magnitude, converted_value.units
    except Exception as e:
        return None, str(e)

def main():
    st.set_page_config(page_title="Unit Converter", layout="centered")
    st.title("Unit Converter")
    
    unit_category = st.selectbox("Select Category", ["Length", "Weight", "Temperature"], index=0)
    
    if unit_category == "Length":
        units = ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"]
    elif unit_category == "Weight":
        units = ["gram", "kilogram", "milligram", "pound", "ounce"]
    elif unit_category == "Temperature":
        units = ["celsius", "fahrenheit", "kelvin"]
    
    col1, col2, col3 = st.columns([3, 1, 3])
    with col1:
        value = st.number_input("Enter Value", min_value=0.0, format="%.6f", key="value_input")
        from_unit = st.selectbox("From Unit", units, key="from_unit")
    
    with col2:
        st.write("=")
    
    with col3:
        to_unit = st.selectbox("To Unit", units, key="to_unit")
        converted_value, converted_unit = convert_units(value, from_unit, to_unit)
        if converted_value is not None:
            st.success(f"{converted_value:.6f} {converted_unit}")
        else:
            st.error(f"Error: {converted_unit}")
    
if __name__ == "__main__":
    main()
