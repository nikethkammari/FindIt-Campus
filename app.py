
import streamlit as st
import sqlite3
import os
from database import create_database

# Page configuration
st.set_page_config(
    page_title="FindIt Campus",
    page_icon="🔎",
    layout="wide"
)

# Create database and upload folder
create_database()
os.makedirs("uploads", exist_ok=True)

st.title("🔎 FindIt Campus")
st.subheader("Smart Campus Lost and Found Platform")
st.write("Lost something on campus? Report it here!")

st.divider()

# Report type
report_type = st.radio(
    "What would you like to report?",
    ["Lost Item", "Found Item"],
    horizontal=True
)

# Item report form
with st.form("item_report_form", clear_on_submit=True):
    st.subheader("Enter Item Details")

    item_name = st.text_input(
        "Item Name",
        placeholder="Example: Black wallet"
    )

    category = st.selectbox(
        "Category",
        [
            "Electronics",
            "Books and Notes",
            "Bags and Wallets",
            "ID Cards",
            "Keys",
            "Clothing",
            "Other"
        ]
    )

    description = st.text_area(
        "Description",
        placeholder="Describe the item, its color, brand, or other details"
    )

    location = st.text_input(
        "Campus Location",
        placeholder="Example: Library, Block A, Canteen"
    )

    contact = st.text_input(
        "Contact Information",
        placeholder="College email or other suitable contact"
    )

    photo = st.file_uploader(
        "Upload Item Photo (optional)",
        type=["jpg", "jpeg", "png"]
    )

    submitted = st.form_submit_button("Submit Report")

    if submitted:
        if not all([
            item_name.strip(),
            description.strip(),
            location.strip(),
            contact.strip()
        ]):
            st.error("Please fill in all required fields.")
        else:
            image_path = None

            if photo is not None:
                safe_name = os.path.basename(photo.name)
                image_path = os.path.join(
                    "uploads",
                    f"{os.urandom(8).hex()}_{safe_name}"
                )

                with open(image_path, "wb") as image_file:
                    image_file.write(photo.getvalue())

            report_value = (
                "Lost" if report_type == "Lost Item" else "Found"
            )

            conn = sqlite3.connect("findit_campus.db")
            conn.execute(
                """
                INSERT INTO items
                (item_name, category, description, location,
                 report_type, contact, image_path)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    item_name.strip(),
                    category,
                    description.strip(),
                    location.strip(),
                    report_value,
                    contact.strip(),
                    image_path
                )
            )
            conn.commit()
            conn.close()

            st.success("Your report was submitted successfully!")
            st.info("You can now browse the report in the next section.")

st.divider()

# Browse submitted reports
st.header("📋 Recent Lost and Found Reports")

conn = sqlite3.connect("findit_campus.db")
items = conn.execute(
    """
    SELECT id, item_name, category, description, location,
           report_type, image_path, status, created_at
    FROM items
    ORDER BY id DESC
    """
).fetchall()
conn.close()

if not items:
    st.info("No reports yet. Submit your first report above!")
else:
    for item in items:
        (
            item_id, name, item_category, item_description,
            item_location, kind, image_path, status, created_at
        ) = item

        with st.container(border=True):
            left, right = st.columns([3, 1])

            with left:
                st.subheader(name)
                st.write(f"**Type:** {kind} | **Category:** {item_category}")
                st.write(f"**Description:** {item_description}")
                st.write(f"**Location:** {item_location}")
                st.write(f"**Status:** {status}")
                st.caption(f"Report ID: {item_id} | {created_at}")

            with right:
                if image_path and os.path.isfile(image_path):
                    st.image(image_path, use_container_width=True)
