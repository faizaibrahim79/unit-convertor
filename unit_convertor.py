import streamlit as st

def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        # Length
        ("meters", "centimeters"): (100, "Multiply the length value by 100"),
        ("centimeters", "meters"): (0.01, "Multiply the length value by 0.01"),
        ("miles", "kilometers"): (1.60934, "Multiply the miles value by 1.60934"),
        ("kilometers", "miles"): (0.621371, "Multiply the km value by 0.621371"),
        # Weight
        ("kilograms", "grams"): (1000, "Multiply the kg value by 1000"),
        ("grams", "kilograms"): (0.001, "Multiply the grams value by 0.001"),
        # Temperature
        ("celsius", "fahrenheit"): (lambda c: (c * 9/5) + 32, "Multiply by 9/5 and add 32"),
        ("fahrenheit", "celsius"): (lambda f: (f - 32) * 5/9, "Subtract 32, then multiply by 5/9"),
        # Speed
        ("kilometers per hour", "miles per hour"): (0.621371, "Multiply the km/h value by 0.621371"),
        ("miles per hour", "kilometers per hour"): (1.60934, "Multiply the mph value by 1.60934"),
        # Time
        ("hours", "minutes"): (60, "Multiply the hours value by 60"),
        ("minutes", "seconds"): (60, "Multiply the minutes value by 60"),
        # Volume
        ("liters", "milliliters"): (1000, "Multiply the liters value by 1000"),
        ("milliliters", "liters"): (0.001, "Multiply the ml value by 0.001"),
    }
    
    if (from_unit, to_unit) in conversion_factors:
        factor, formula = conversion_factors[(from_unit, to_unit)]
        result = factor(value) if callable(factor) else value * factor
        return result, formula
    else:
        return None, "Conversion not available"

st.title("✨:blue[Professional Unit Converter]✨")

categories = {
    "Length": ["meters", "centimeters", "miles", "kilometers"],
    "Weight": ["kilograms", "grams"],
    "Temperature": ["celsius", "fahrenheit"],
    "Speed": ["kilometers per hour", "miles per hour"],
    "Time": ["hours", "minutes", "seconds"],
    "Volume": ["liters", "milliliters"]
}

category = st.selectbox("Select Category", list(categories.keys()))
from_unit = st.selectbox("From", categories[category])
to_unit = st.selectbox("To", categories[category])
value = st.number_input("Enter Value", min_value=0.0, format="%.4f")

if st.button("Convert"):
    result, formula = convert_units(value, from_unit, to_unit)
    if result is not None:
        st.success(f"Converted Value: {result} {to_unit}")
        st.info(f"Formula: {formula}")
    else:
        st.error("Conversion not supported")

