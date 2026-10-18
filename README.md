#  FindIt Campus – Smart Lost and Found System

##  Overview

FindIt Campus is a smart, web-based Lost and Found System designed to help college students report, search, and recover lost belongings efficiently. It provides a centralized platform to report lost and found items, upload images to cloud storage, and identify potential matches using a smart matching algorithm.

##  Problem Statement

Students frequently lose personal belongings such as ID cards, books, wallets, keys, and electronic devices on campus. Finding these items is difficult because there is no centralized platform to report, track, and match lost and found items efficiently.

##  Solution

FindIt Campus provides a centralized digital platform where students can report lost or found items, upload images, search and filter reports, and identify potential matches. The system aims to simplify item recovery and improve communication between students.

##  Features

- 📝 Report lost items.
- 📦 Report found items.
- 🖼️ Upload and store item images using Supabase Storage.
- 🔎 Search and filter items by name, category, location, and report type.
- 🤖 Identify potential matches using a Python-based matching algorithm.
- 🔐 User authentication using Supabase Auth.
- 📊 Admin dashboard for managing reports.
- ✅ Track item recovery and report status.

##  Technology Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **Database:** Supabase PostgreSQL
- **Cloud Image Storage:** Supabase Storage
- **Authentication:** Supabase Auth
- **Matching Algorithm:** Python
- **Version Control:** Git and GitHub

##  System Architecture

The system follows a layered architecture:

1. **Presentation Layer:** Streamlit provides the user interface.
2. **Application Layer:** Python handles requests, validation, and business logic.
3. **Matching Layer:** Compares lost and found item details to identify potential matches.
4. **Database Layer:** Supabase PostgreSQL stores user profiles, item reports, and matching records.
5. **Cloud Storage Layer:** Supabase Storage stores uploaded item images.
6. **Security Layer:** Supabase Auth and Row Level Security (RLS) control authentication and data access.

### Workflow

Student → Streamlit Interface → Python Backend → Supabase Database and Storage → Smart Matching → Potential Matches → Item Recovery

## 📁 Project Structure

```text
FindIt-Campus/
├── app.py
├── requirements.txt
├── config.py
├── supabase_client.py
├── matching.py
├── pages/
│   ├── 1_Login.py
│   ├── 2_Report_Item.py
│   ├── 3_Browse_Items.py
│   ├── 4_My_Reports.py
│   └── 5_Admin_Dashboard.py
├── services/
│   ├── __init__.py
│   ├── auth_service.py
│   ├── item_service.py
│   ├── image_service.py
│   └── matching_service.py
├── .streamlit/
│   └── secrets.toml
└── .gitignore
