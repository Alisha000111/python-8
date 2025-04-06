import streamlit as st


st.title("💛💙📚 My Personal Library")
st.write("A simple app to track my book collection")


if 'books' not in st.session_state:
    st.session_state.books = []

with st.form("add_book"):
    st.subheader("Add a New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    status = st.selectbox("Status", ["Unread", "Reading", "Finished"])
    
    if st.form_submit_button("Add Book"):
        if title and author:  
            new_book = {
                "title": title,
                "author": author,
                "status": status
            }
            st.session_state.books.append(new_book)
            st.success("Book added!")
        else:
            st.warning("Please fill in both title and author")


if st.session_state.books:
    st.subheader("My Book Collection")
    for i, book in enumerate(st.session_state.books):
        col1, col2, col3 = st.columns([1, 2, 3])
        with col1:
            st.write(f"**{book['title']}**")
        with col2:
            st.write(f"by {book['author']}")
        with col3:
            st.write(f"({book['status']})")
        
       
        if st.button(f"Delete {i}", key=f"del_{i}"):
            del st.session_state.books[i]
            st.rerun()
else:
    st.info("Your library is empty. Add some books!")