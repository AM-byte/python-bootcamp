import streamlit as st
from streamlit_webrtc import webrtc_streamer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from st_aggrid import AgGrid, GridOptionsBuilder
from streamlit_echarts import st_echarts
from streamlit_chat import message

# 1. Title and description
st.title("My First Streamlit App")
st.write("This simple app shows how the script structure works.")

# 2. Input widget
value = st.slider("Pick a number", 0, 100, 50)

# 3. Display result
st.write("You selected:", value)


# Titles and Headers
st.title("Sales Dashboard")

st.header("Quarterly Performance")

st.subheader("Q1 vs Q2 Comparison")


# Free-Form Text
st.write("Welcome to the dashboard! Here you'll find key metrics for sales performance.")

st.markdown("""
- **Revenue:** Total dollars sold  
- **Growth:** Percentage change from previous quarter  
- **Top Product:** Best-selling item  
""")


# Code Snippets and Logs
st.code("df.head()", language="python")

st.caption("Data last updated: April 15, 2025")


# From a URL
st.image(
  "https://upload.wikimedia.org/wikipedia/commons/3/3c/Shaki_waterfall.jpg",
  caption="Example Waterfall",
  use_container_width=True
)

# From a Local File
# st.image("images/chart.png", caption="Sales Chart", use_column_width=True)


# Stream Audio Clips
st.audio(
  "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
  format="audio/mp3"
)


# Stream Videos
st.video("https://www.youtube.com/watch?v=jfKfPfyJRdk")  # from website

# st.video("videos/demo.mp4")  # local file


# Snapping Photos
img = st.camera_input("Take a photo")
if img:
  st.image(img, caption="Captured image", use_column_width=True)


# Video Streaming
# Start the webcam stream
webrtc_streamer(key="live-stream")


# Sidebar
# Put widgets in the sidebar
st.sidebar.title("Controls")
option = st.sidebar.selectbox("Choose a dataset", ["Sales", "Marketing", "Finance"])
threshold = st.sidebar.slider("Threshold", 0, 100, 50)

# Main app content
st.title("Data Viewer")
st.write(f"Showing {option} data with threshold {threshold}")


# Columns
col1, col2 = st.columns(2)

with col1:
  st.header("Chart")
  st.line_chart([10, 20, 30, 40])

with col2:
  st.header("Statistics")
  st.write({"Mean": 25, "Max": 40, "Min": 10})


# Container
with st.container():
  st.subheader("Section 1")
  st.write("This is grouped in one container.")

st.write("This is outside the container.")


# Expanders and Tabs

with st.expander("See more details"):
  st.write("Here are additional metrics and explanations.")

tab1, tab2 = st.tabs(["Overview", "Details"])

with tab1:
  st.write("This is the overview tab.")
with tab2:
  st.write("This is the details tab.")


# On/off switch
show_details = st.checkbox("Show details")

if show_details:
  st.write("Here are the extra details you asked for!")
else:
  st.write("Details are hidden.")


# Radio Buttons
choice = st.radio(
  "Pick a chart type",
  ("Line", "Bar", "Histogram")
)

st.write(f"You selected a {choice} chart.")


# Multiselect

options = st.multiselect(
  "Select one or more fruits",
  ["Apple", "Banana", "Cherry", "Date"]
)

if options:
  st.write("You picked:", options)
else:
  st.write("No fruit selected.")


# Range Slider

start, end = st.slider(
  "Select a range of years",
  2000, 2025, (2010, 2020)
)

st.write(f"You chose years from {start} to {end}.")


# Uploading Files

st.header("Upload Your Data")

# Allow only CSV files
uploaded_file = st.file_uploader(
  label="Choose a CSV file to upload",
  type="csv"
)

if uploaded_file is not None:
  # Read the uploaded CSV into a DataFrame
  df = pd.read_csv(uploaded_file)
  st.write("Here’s a preview of your data:")
  st.dataframe(df.head())


# Downloading Files

# Assume `df` is the DataFrame you want users to download
csv_data = df.to_csv(index=False).encode("utf-8")

st.download_button(
  label="Download Processed Data as CSV",
  data=csv_data,
  file_name="processed_data.csv",
  mime="text/csv"
)


## State

# Click Counter

# 1. Initialize state
if 'count' not in st.session_state:
  st.session_state.count = 0

# 2. Define an action to update state
def increment():
  st.session_state.count += 1

# 3. UI: button that calls the action
st.button("Increment", on_click=increment)

# 4. Display the persistent count
st.write("Count =", st.session_state.count)

# Remembering Form Inputs

# Text input tied to session state key "username"
name = st.text_input("Your name", key="username")

# Use the stored value elsewhere
if name:
  st.write(f"Hello, {st.session_state.username}!")

# Resetting or Clearing State

if st.button("Reset Counter"):
  st.session_state.count = 0

if st.button("Clear Name"):
  del st.session_state['username']


## Integrate Data and Graphs

# Quick Charts from DataFrames

# Create a sample DataFrame
df = pd.DataFrame({
  "Month":    ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
  "Product A":[150,   180,   120,   200,   160,   210],
  "Product B":[100,   130,   160,   140,   190,   170]
})

# Display the table
st.dataframe(df)

# Line chart (months on x-axis)
st.line_chart(df.set_index("Month"))

# Bar chart for the same data
st.bar_chart(df.set_index("Month"))

# Custom Matplotlib Figures

# Sample data
df = pd.DataFrame({
  "Month":    ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
  "Product A":[150,   180,   120,   200,   160,   210],
  "Product B":[100,   130,   160,   140,   190,   170]
})

# Prepare the figure
fig, ax = plt.subplots()
ax.plot(df["Month"], df["Product A"], marker="o", label="Product A")
ax.bar(df["Month"], df["Product B"], alpha=0.5, label="Product B")

# Enhance the plot
ax.set_title("Monthly Sales Comparison")
ax.set_xlabel("Month")
ax.set_ylabel("Units Sold")
ax.legend()

# Display in Streamlit
st.pyplot(fig)


## Community Components

# Interactive Tables with AG Grid

# Sample DataFrame
df = pd.DataFrame({
  "Month":    ["Jan","Feb","Mar","Apr","May","Jun"],
  "Product A":[150, 180, 120, 200, 160, 210],
  "Product B":[100, 130, 160, 140, 190, 170]
})

st.header("Interactive Table with AG Grid")

# Build options from DataFrame
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_default_column(editable=False, groupable=True)
grid_opts = gb.build()

# Display
AgGrid(
  df,
  gridOptions=grid_opts,
  fit_columns_on_grid_load=True,
  enable_enterprise_modules=False
)

# Beautiful Charts with ECharts

# Sample DataFrame
df = pd.DataFrame({
  "Month":    ["Jan","Feb","Mar","Apr","May","Jun"],
  "Product A":[150, 180, 120, 200, 160, 210]
})

st.header("Smooth Line Chart with ECharts")

# Build ECharts options
options = {
  "xAxis": {"type": "category", "data": df["Month"].tolist()},
  "yAxis": {"type": "value"},
  "series": [{
    "data": df["Product A"].tolist(),
    "type": "line",
    "smooth": True,
    "areaStyle": {}      # fills area under the line
  }]
}

# Display
st_echarts(options, height="400px")

# Chatbot Interface with a Community Component

# Initialize a session state list to hold the conversation
if "history" not in st.session_state:
  st.session_state.history = []

st.header("Chat with Your Bot")

# 1. Capture user input
user_input = st.text_input("You:", key="input")

# 2. On submit, append both user and bot messages
if user_input:
  # Simple bot response - no API calls needed
  bot_response = "Hello there!"
  
  st.session_state.history.append({
      "user": user_input,
      "bot": bot_response
  })

# 3. Display the chat history
for i, chat in enumerate(st.session_state.history):
  message(chat["user"], is_user=True, key=f"user_{i}")
  message(chat["bot"],     key=f"bot_{i}")