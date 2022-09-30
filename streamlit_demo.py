import streamlit as st
# st.write("Hello **ATHEX** team!")
import pandas as pd
from datetime import datetime, timedelta
                 
# import matplotlib.pyplot as plt      

import plotly.express as px
import plotly.graph_objects as go

# st.set_page_config(
#     page_title="My Demo App",
#     page_icon=":shark:",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

df = pd.DataFrame({"area": [131957, 301338, 498511, 551695, 91568, 110994],
                    "population": [10768193, 60390560, 46733038, 67372000, 10276617, 7000039]},
                    index=['Greece', 'Italy', 'Spain', 'France', 'Portugal', 'Bulgaria'])

st.markdown("""# Introduction to Data Analysis with Python
#### Copyright &copy; 2022 Nick Christodoulopoulos - All rights reserved
## Introduction to [Streamlit](https://streamlit.io)
### Create web-based data-driven apps!
- [Documentation](https://docs.streamlit.io)""")


st.subheader("✔️ Installation")

st.code("""
# From Anaconda Prompt
pip install streamlit
"""
,  language="python")       

st.subheader("✔️ Running")
st.code("""
# From Anaconda Prompt
streamlit run your_script.py
"""
,  language="python")       

st.subheader("✔️ Page config ")
st.code("""
import streamlit as st

st.set_page_config(
   page_title="My Demo App", # str
   page_icon=":shark:", # image or emoji string or shortcode
   layout="wide", # (Default:"centered" or "wide")
   initial_sidebar_state="expanded") # (D:"auto"[ie responsive] or "expanded" or "collapsed")
"""
,  language="python")       

st.subheader("✔️ Write / Magic ")

with st.echo():    
    # Write
    st.write('It can write anything on the webpage')
    st.write(111132.456) 
    st.write(["an", "entire", "list"]) 
    st.write(("an", "entire", "tuple"))  
    st.write({"it":"can", "also":"write", "a":"dict"})        
    st.write(df)      
    st.write('Below is a DataFrame:', df, 'Above is a dataframe.')  
    st.write('<b>HTML</b> tags in strings will be escaped. You can use unsafe_allow_html=<span style="color:red;">True</span> to use HTML.<br/><b>Not advised for security reasons!</b>', unsafe_allow_html=True) 
st.markdown("---")      

st.code("""
# "Magic" (streamlit automatically detects & prints the object)

df = pd.DataFrame({
    'colA': [1, 2, 3, 4],
    'colB': [10, 20, 30, 40],
    'colC': ['John', 'Maria', 'Max', 'Mary'],    
    }) 
df 

"""
,  language="python")   
st.dataframe(df)

st.subheader("✔️ Typography")
with st.echo():
    st.title("This is a title")
    st.header('This is a header')   
    st.subheader('This is a subheader')  
    st.caption('This is a caption')     
    st.text('This is fixed-width text')      
    st.latex(r'''
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')        
    st.markdown("*Markdown* is **fully** supported :sunglasses:") 
    st.write("""
        ### Want to learn more?
        - Check out [streamlit.io](https://streamlit.io)
        - See the [documentation](https://docs.streamlit.io)
    """)   
    st.error('This is an error' )
    st.warning('This is a warning')
    st.info('This is an info message')
    st.success('This is a success message!')
    st.code("print('format python code')", language="python")               
st.markdown("---")

with st.echo():
    # Images

    st.image('https://www.athexgroup.gr/image/company_logo?img_id=41211&t=1662469618474',
    caption="This is an image",
    width=150) 
st.markdown("---")

## Data Display
st.subheader("✔️ Data Display ")
# Pandas DataFrame
with st.echo(): 
    st.dataframe(df) # Same as st.write(df)
    # - Interactive features!
    # - Col sorting
    # - Col & table resizing
    # - Copy to clipboard and paste to any spreadsheet    
    st.dataframe(df, width=115, height=300) # numbers in pixels
    
st.markdown("---")   

with st.echo(): 
    st.table(df) # full width table with no interactive features
st.markdown("---")

with st.echo(): 
    # Metric

    st.metric(label="Sales", 
            value="€3.6m", 
            delta="€0.2m", 
            delta_color="normal",  # "inverse" or "off"
            help="help text")

st.markdown("---")

st.subheader("✔️ Input widgets")

with st.echo():
    # Button
     
    mybutton = st.button(label="This is a button", help="Please click me!") 
    # Returns True if the button gets clicked

    if mybutton:
        st.write('Thank you for clicking me!') 
    else:
        st.write('I would appreciate if you could click me!')
st.markdown("---")

with st.echo(): 
    # Checkbox

    mycheckbox = st.checkbox('I agree')
    # value=True, help="Help text", disabled=False
    # Can be used to toggle data visibility
    if mycheckbox:
        st.write('Thank you for agreeing. Have a look at this DataFrame:')
        st.write(df)
st.markdown("---")

def title_case(option):
    return option.title()
st.code("""

def title_case(option):
    return option.title()

"""
,  language="python")       
with st.echo(): 
    # Radio button

    myradio = st.radio(label="What is your favorite color?", 
                    options=['red', 'blue', 'green'], 
                    index=1, # selected value
                    format_func=title_case, # modifies the display of radio options but... 
                    # ...has no impact on the return value of the radio!
                    horizontal=False)
    st.write('You selected:', myradio) # notice the lower case                
st.markdown("---")


with st.echo(): 
    # SelectBox (dropdown menu)

    option = st.selectbox(label="What is your favorite color?", 
                        options=['red', 'blue', 'green'], #list, tuple, series, df
                        index=1, # selected value
                        help="Help text goes here")
    st.write('You selected:', option) 
st.markdown("---")

with st.echo(): 
    # Multiselect

    option = st.multiselect(label="What is your favorite color?", 
                        options=['red', 'blue', 'green'], 
                        default=['red'], 
                        format_func=title_case,
                        help="Help text goes here")
    if option:
        st.write('You selected:', option)
st.markdown("---")    

with st.echo(): 
    # Slider

    option = st.slider(label="Slideme", 
                    min_value=1, #Default: 0
                    max_value=10, #D: 100
                    value=(5, 8), # use a tuple/list to turn it into a range slider!
                    step=1) 
    
    # Works with Dates as well!
    dataslider = st.slider(label="DateSlider",
                    min_value=datetime(2022, 9, 1),
                    max_value=datetime(2022, 9, 30),
                    step=timedelta(days=1))  
    if dataslider:
        st.write('You selected:', dataslider)                      
st.markdown("---")    

with st.echo(): 
    # Select_slider

    option = st.select_slider(label="Select Slider",
                options=["Very bad", "bad", "ok", "good", "very good"], 
                value="good")
    if option:
        st.write('You selected:', option)
st.markdown("---")    

with st.echo(): 
    # Text Input  

    title = st.text_input('Please type your favorite color', 
                    value='Red',
                    max_chars=20,
                    type="default", #D:"default", "password"
                    placeholder="Optional string if text input is empty ")  
    st.write('You typed: ', title)
st.markdown("---")  

with st.echo():
    # Number Input
    
    number = st.number_input('Insert a number',
                            min_value=None,
                            max_value=None,
                            value=1,
                            step=1)
    if number:
        st.write('The current number is ', number)
st.markdown("---")  

with st.echo():
    # Text area 

    txt = st.text_area('Text area', 
    value="""
    This
    is 
    a multi-line
    text""", max_chars=200)

st.markdown("---")  

with st.echo():
    # Date input   
    
    d = st.date_input(
        "When is your birthday?",
        datetime.now(),
        min_value=datetime.now()+timedelta(days=-30),
        max_value=datetime(2023, 12, 31 ))
    st.write('Your birthday is:', d)
st.markdown("---")     

st.subheader("✔️ Charts")

df
# fig, ax = plt.subplots(figsize=(8,2))
# ax.plot(df.index, df['colA'])
# st.pyplot(fig)    
with st.echo():
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(8,2))
    ax.bar(df.index, df['area'])
    st.pyplot(fig)

with st.echo():
    import plotly.express as px
    fig = px.bar(df, x=df.index, y='area')
    st.plotly_chart(fig, use_container_width=True)    

st.subheader("✔️ Layout Utilities")


st.code("""
# Sidebar

# just add "sidebar" before each element to place it on the sidebar
st.sidebar.write("Hello sidebar!")
# Sidebar is resizable!
"""
,  language="python")   
st.markdown("---") 
with st.echo():
    # Tabs

    tab1, tab2, tab3 = st.tabs(["Error", "Dog", "Owl"])

    with tab1:
        st.subheader("This is the error tab")
        st.error('This is an error messsage' )
    with tab2:
        st.subheader("This is the warning tab")
        st.warning('This is a warning message')
    with tab3:
        st.subheader("This is the info tab")        
        st.info('This is an info message')  
st.markdown("---")



with st.echo():
    # Columns

    col1, col2, col3 = st.columns(3, gap="small") # D:"small", "medium", "large"
    # use something like st.columns([3, 1, 2]) to provide a ratio for uneven cols

    with col1:
        st.error('This is an error messsage' )
    with col2:
        st.warning('This is a warning message')        
    with col3:
        st.info('This is an info message')
st.subheader("✔️ Optimize performance with st.cache")

with st.echo():
    @st.cache  # 👈 Add this!
    def complex_and_slow_function(a, b):
        # Complex and slow computations...
        return result

st.write("""
When you mark a function with the **@st.cache** decorator, Streamlit will check the following:

- The input parameters
- The value of any external variable used in the function
- The body of the function
- The body of any function used inside the cached function

If this is the first time Streamlit has seen these four components with these exact values and in this exact combination and order, it runs the function and stores the result in a local cache. 
Then, next time the cached function is called, if none of these components changed, Streamlit will just skip executing the function altogether and, instead, return the output previously stored in the cache.

""")


