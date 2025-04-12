
import streamlit as st
import re

# Function to check password strength
def check_password_strength(password):
    criteria = {
        "At least 8 characters": len(password) >= 8,
        "At least one uppercase letter": bool(re.search(r"[A-Z]", password)),
        "At least one lowercase letter": bool(re.search(r"[a-z]", password)),
        "At least one number": bool(re.search(r"[0-9]", password)),
        "At least one special character (@$!%*?&)": bool(re.search(r"[@$!%*?&]", password))
    }

    # Count how many conditions are met
    strength = sum(criteria.values())

    # Determine strength level
    if strength <= 2:
        return "Weak", "red", 0.2, criteria
    elif strength == 3 or strength == 4:
        return "Medium", "orange", 0.6, criteria
    else:
        return "Strong", "green", 1.0, criteria

# Streamlit UI
st.title("🔒 Password Strength Meter")

# Input field for password
password = st.text_input("Enter your password:", type="password")

# Check password strength only if user types
if password:
    strength_text, color, progress, criteria = check_password_strength(password)

    # Display strength text
    st.markdown(f"**Strength:** <span style='color:{color}; font-size:18px;'>{strength_text}</span>", unsafe_allow_html=True)

    # Show progress bar
    st.progress(progress)

    # Show criteria dynamically
    st.write("✅ Password should:")
    for rule, passed in criteria.items(): 
        st.write(f"- {'✅' if passed else '❌'} {rule}")
