import streamlit as st

# ユーザ情報を保持する辞書
users = {"test": "test123"}

def verify_credentials(username, password):
    if username in users and users[username] == password:
        return True
    else:
        return False

def change_password(username, new_password):
    users[username] = new_password

def main():
    menu = ["Home", "Login", "Change Password"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
    elif choice == "Login":
        st.subheader("Login Section")
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password", type='password')
        if st.sidebar.checkbox("Login"):
            if verify_credentials(username, password):
                st.success("Logged In Successfully")
                st.write("Proceed to do actions")
            else:
                st.warning("Incorrect Username/Password")
    elif choice == "Change Password":
        st.subheader("Change Password Section")
        username = st.text_input("User Name")
        old_password = st.text_input("Old Password", type='password')
        new_password = st.text_input("New Password", type='password')
        if st.button("Change Password"):
            if verify_credentials(username, old_password):
                change_password(username, new_password)
                st.success("Password Changed Successfully")
            else:
                st.warning("Incorrect Username/Old Password")

if __name__ == "__main__":
    main()

