import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(page_title="Customizable Jute Bags", page_icon=":purse:", layout="wide")

# Landing Page Title and Tagline
st.title("Eco-Friendly & Stylish Customizable Jute Bags")
st.subheader("Personalize your bag, save the planet!")

# Display two smaller images side by side in columns
col1, col2 = st.columns(2)

with col1:
    # First image
    image1 = Image.open("photo1.jpg")  # Replace with your actual image
    st.image(image1, caption="Stylish Custom Jute Bag", use_column_width=True)

with col2:
    # Second image
    image2 = Image.open("photo2.jpg")  # Replace with your actual image
    st.image(image2, caption="Eco-Friendly Jute Bag", use_column_width=True)


# Introduction Section
st.write("""
### Why Choose Our Jute Bags?
At Earthy Essentials, we combine eco-friendliness with style by offering **customizable jute bags**. 
These bags are made from sustainable materials and allow you to create a personalized design.
Whether you're looking for a trendy fashion accessory or a unique promotional item, 
we have the perfect bag for you!
""")

# Benefits of the Business Model
st.write("""
#### Why Our Jute Bags Stand Out:
- 🌍 **Eco-Friendly**: 100% biodegradable and sustainable.
- 🎨 **Fully Customizable**: Choose colors, prints, and logos to make it your own.
- 💼 **Business Promotions**: Perfect for corporate branding and giveaways.
- 🎁 **Unique Gift**: A thoughtful and stylish eco-gift option.
""")

# Call-to-Action Buttons
st.write("Ready to get started?")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Explore Designs"):
        st.write("Redirecting to design gallery...")  # Replace with actual URL
        # st.experimental_rerun() for redirect

with col2:
    if st.button("Create Your Own Bag"):
        st.write("Redirecting to the customization tool...")  # Replace with actual URL

with col3:
    if st.button("Contact Us"):
        st.write("Redirecting to the contact page...")  # Replace with actual URL

# Footer with Social Media Links
st.write("---")
st.write("### Follow Us")
st.write("[Instagram](https://www.instagram.com) | [Facebook](https://www.facebook.com) | [Twitter](https://www.twitter.com)")

# Optional Testimonials Section
st.write("""
---
### Hear From Our Customers
"Absolutely love my custom jute bag! It’s eco-friendly and fashionable." – **Alex**  
"Perfect for our corporate event branding. A big hit with the team!" – **Sarah**  
"High-quality and sturdy! I’ve been using my jute bag every day for months." – **Priya**  
"Great concept! I love that I can personalize it to match my style." – **John**  
"Received it as a gift, and now I’m hooked! Will definitely be ordering more." – **Emily**  
"The customization options are fantastic. I got exactly what I wanted!" – **Ravi**  
"Our company’s logo on these eco-friendly bags was a hit at the trade show!" – **Jessica**  
"Amazing product! It’s both sustainable and stylish. My friends are asking where I got it!" – **Maya**  
"These bags are perfect for my grocery shopping – no more plastic bags!" – **Arun**  
"Great service and attention to detail. Highly recommend for businesses and personal use." – **Olivia**
""")

# Footer Copyright
st.write("© 2024 YourBrand. All rights reserved.")
