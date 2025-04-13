import streamlit as st

# Set page config
st.set_page_config(
    page_title="Unit Converter",
    page_icon="📐",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        background-color: #4a8af4;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #3a7ae4;
        color: white;
    }
    .result-box {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-top: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Conversion functions (same as before)
def convert_length(value, from_unit, to_unit):
    conversions = {
        'mm': 0.001, 'cm': 0.01, 'm': 1.0, 'km': 1000.0,
        'in': 0.0254, 'ft': 0.3048, 'yd': 0.9144, 'mi': 1609.34
    }
    meters = value * conversions[from_unit]
    return meters / conversions[to_unit]

def convert_weight(value, from_unit, to_unit):
    conversions = {
        'mg': 0.000001, 'g': 0.001, 'kg': 1.0,
        'oz': 0.0283495, 'lb': 0.453592, 'ton': 907.185
    }
    kg = value * conversions[from_unit]
    return kg / conversions[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == '°C':
        if to_unit == '°F': return (value * 9/5) + 32
        elif to_unit == 'K': return value + 273.15
    elif from_unit == '°F':
        if to_unit == '°C': return (value - 32) * 5/9
        elif to_unit == 'K': return (value - 32) * 5/9 + 273.15
    elif from_unit == 'K':
        if to_unit == '°C': return value - 273.15
        elif to_unit == '°F': return (value - 273.15) * 9/5 + 32

# App title
st.title("📐 Unit Converter")
st.markdown("Convert between different measurement units")

# Rest of the app remains the same...
category = st.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])

col1, col2 = st.columns(2)
with col1:
    value = st.number_input("Enter value", min_value=0.0, value=1.0, step=0.1)
with col2:
    if category == "Length":
        units = ['mm', 'cm', 'm', 'km', 'in', 'ft', 'yd', 'mi']
        from_unit = st.selectbox("From", units, index=2)
        to_unit = st.selectbox("To", units, index=1)
        result = convert_length(value, from_unit, to_unit)
    elif category == "Weight":
        units = ['mg', 'g', 'kg', 'oz', 'lb', 'ton']
        from_unit = st.selectbox("From", units, index=2)
        to_unit = st.selectbox("To", units, index=1)
        result = convert_weight(value, from_unit, to_unit)
    elif category == "Temperature":
        units = ['°C', '°F', 'K']
        from_unit = st.selectbox("From", units, index=0)
        to_unit = st.selectbox("To", units, index=1)
        result = convert_temperature(value, from_unit, to_unit)

if st.button("Convert", type="primary"):
    st.markdown(
        f"""
        <div class="result-box">
            <h3 style="color: #4a8af4; margin-bottom: 0.5rem;">Conversion Result</h3>
            <p style="font-size: 1.2rem; margin-bottom: 0; color: #333333;">
                {value:.2f} {from_unit} = <strong>{result:.4f} {to_unit}</strong>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
st.markdown("---")
st.markdown("Made by Aiman Rizwan")