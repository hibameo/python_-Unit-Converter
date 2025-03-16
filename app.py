import streamlit as st

def convert_units(category, value, from_unit, to_unit):
    conversions = {
        "Length": {
            "Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Mile": 0.000621371,
            "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701
        },
        "Weight": {
            "Kilogram": 1, "Gram": 1000, "Milligram": 1e6, "Pound": 2.20462, "Ounce": 35.274
        },
        "Temperature": {
            "Celsius": lambda x: x, "Fahrenheit": lambda x: (x * 9/5) + 32, "Kelvin": lambda x: x + 273.15
        },
        "Time": {
            "Second": 1, "Minute": 1/60, "Hour": 1/3600, "Day": 1/86400
        }
    }
    
    if category == "Temperature":
        if from_unit == "Fahrenheit":
            value = (value - 32) * 5/9
        elif from_unit == "Kelvin":
            value -= 273.15
        
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
        else:
            return value
    
    else:
        return value * (conversions[category][to_unit] / conversions[category][from_unit])

# Streamlit UI
st.title("🔄 Unit Converter Web App")
st.sidebar.header("Select Conversion")

categories = ["Length", "Weight", "Temperature", "Time"]
category = st.sidebar.selectbox("Choose Category", categories)

units = {
    "Length": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"],
    "Weight": ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Time": ["Second", "Minute", "Hour", "Day"]
}

from_unit = st.selectbox("From", units[category])
to_unit = st.selectbox("To", units[category])
value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

if st.button("Convert"):
    result = convert_units(category, value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
