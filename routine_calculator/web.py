import streamlit as st
import routine_calculator.global_resource as gr
import routine_calculator.load as load
import routine_calculator.command as command
import routine_calculator.cmd_cal as cmd_cal
import contextlib
import io
import datetime
import pandas as pd
import altair as alt

st.set_page_config(page_title="Routine Calculator", layout="wide")

# Initialize logic
if 'initialized' not in st.session_state:
    filename = gr.get_savefile_name()
    load.load(filename=filename)
    st.session_state['initialized'] = True

st.title("Routine Calculator")

# Sidebar for navigation
page = st.sidebar.radio("Navigation", ["Dashboard", "Diff", "Calendar"])

if page == "Dashboard":
    st.header("Dashboard")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Time Distribution")
        # Prepare data for chart
        data = []
        for k, v in gr.data_store['variables'].items():
            sec = gr.convert_to_seconds(v)
            data.append({"Activity": k, "Seconds": sec, "Time": v})
        
        if data:
            df = pd.DataFrame(data)
            
            # Create Pie Chart using Altair
            base = alt.Chart(df).encode(
                theta=alt.Theta("Seconds", stack=True),
            )
            
            pie = base.mark_arc(outerRadius=120).encode(
                color=alt.Color("Activity"),
                order=alt.Order("Seconds", sort="descending"),
                tooltip=["Activity", "Time", "Seconds"]
            )
            
            text = base.mark_text(radius=140).encode(
                text="Activity",
                order=alt.Order("Seconds", sort="descending"),
                color=alt.value("white")  # Set the color of the labels to white for dark theme
            )
            
            st.altair_chart(pie + text, use_container_width=True)
        else:
            st.info("No variables defined yet.")

    with col2:
        st.subheader("Summary")
        # Capture output of print_result
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            cmd_cal.print_result()
        output = f.getvalue()
        st.text(output)
        
        st.subheader("Variables")
        st.json(gr.data_store['variables'])

    st.divider()
    st.subheader("Execute Commands")
    
    def process_command():
        cmd = st.session_state.cmd_input
        if cmd:
            f = io.StringIO()
            with contextlib.redirect_stdout(f):
                try:
                    if not command.execute(cmd):
                         print('Error: syntax or format error type "help me"')
                except Exception as e:
                    print('Error: ', e)
            st.session_state.last_cmd_output = f.getvalue()
            st.session_state.cmd_input = ""

    st.text_input("Enter command (e.g., 'eval 1+1', 'set var 10m')", key="cmd_input", on_change=process_command)
    
    if 'last_cmd_output' in st.session_state and st.session_state.last_cmd_output:
        st.code(st.session_state.last_cmd_output)

elif page == "Calendar":
    st.header("Calendar")
    
    import calendar
    
    year = st.number_input("Year", min_value=1900, max_value=2100, value=datetime.datetime.now().year)
    month = st.number_input("Month", min_value=1, max_value=12, value=datetime.datetime.now().month)
    
    cal = calendar.HTMLCalendar(calendar.SUNDAY)
    html_cal = cal.formatmonth(year, month)
    st.markdown(html_cal, unsafe_allow_html=True)

elif page == "Diff":
    st.header("Time Difference")
    
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", value=datetime.date.today())
        start_time = st.time_input("Start Time", value=datetime.time(9, 0))
    
    with col2:
        end_date = st.date_input("End Date", value=datetime.date.today())
        end_time = st.time_input("End Time", value=datetime.time(17, 0))
        
    if st.button("Calculate Difference"):
        start_dt = datetime.datetime.combine(start_date, start_time)
        end_dt = datetime.datetime.combine(end_date, end_time)
        
        diff = end_dt - start_dt
        st.success(f"Difference: {diff}")
        st.info(f"Total Seconds: {diff.total_seconds()}")
