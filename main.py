import streamlit as st
from few_shots import FewShotPosts
from post_generator import generate_post

def main():
    st.title("LinkedIn Post Generator")
    col1, col2, col3 = st.columns(3)
    fs=FewShotPosts()
    tags = fs.get_tags()
    with col1:
       selected_title=st.selectbox("Title",options=tags) 
       
    with col2:
        selected_length=st.selectbox("Length",options=['Small','Medium','Long'])
    
    with col3:
        selected_lang=st.selectbox("Language",options=['English','Hinglish'])
       
    if st.button("Generate"):
        st.write(f"Generated post for {selected_title}, {selected_length}, {selected_lang}")
        post=generate_post(selected_length,selected_lang,selected_title)
        st.write(post)

if __name__=='__main__':
    main()