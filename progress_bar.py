'''
****** This is Python Code...*****
import time
import sys
from tqdm import tqdm


class Project2:
    def __init__(self, task=None, finished=None):
        self.task = task
        self.finished = finished

    def shubham(self, task=None, finished=None):

        print("Here is your Progress bar... ")
        print(f"Enter your Task here ↓ \n Once you Have completed the task type {"Done"} this wont add to Your Data...")

        storage = []

        if not task:
            task = input("Enter Your task : ")
        self.task = task

        while task != "Done":
            task = input("Enter Your task : ")
            storage.append(task)

        bar_ini = len(storage)
        length = len(storage)

        if not finished:
            finished = int(input("How many of these have you Completed ? "))
        self.finished = finished

        with tqdm(
            total=length, desc=f"Your Work Progress Bar is here -->", unit="unit"
        ) as pbar:
            
            for i in range(finished):
                time.sleep(0.1)
                pbar.update(1)
        print(f"You have completed your {finished/length * 100} % of work.")
        sys.exit()


def main():
    A = Project2()
    A.shubham()

if __name__ == "__main__":
    main()
'''

import streamlit as st
import time

class Project2:
    def __init__(self, task=None, finished=None):
        self.task = task
        self.finished = finished

    def shubham(self, task=None, finished=None):
        # Initialize session state
        if 'storage' not in st.session_state:
            st.session_state.storage = []  # Initialize with empty list
        if 'input_complete' not in st.session_state:
            st.session_state.input_complete = False
        if 'celebration_triggered' not in st.session_state:
            st.session_state.celebration_triggered = False  # Track if celebration has been triggered
        
        with st.sidebar:
            st.header("Task Input")
            st.write("Enter your Task here ↓")
            st.write("Click 'Finish' or type 'Done' to complete task entry...")
            
            if not st.session_state.input_complete:
                with st.form("task_form", clear_on_submit=True):
                    task_input = st.text_input("Enter Your task:")
                    # Create columns for side-by-side buttons with adjusted widths
                    col1, col2 = st.columns([1, 1.2])  # Slightly wider column for "Finish" button
                    with col1:
                        add_submitted = st.form_submit_button("Add")
                    with col2:
                        finish_submitted = st.form_submit_button("Finish")
                    
                    if add_submitted and task_input:
                        if task_input != "Done":
                            st.session_state.storage.append(task_input)
                            st.success(f"Added: {task_input}")
                        else:
                            st.session_state.input_complete = True
                            st.rerun()
                    
                    if finish_submitted:
                        st.session_state.input_complete = True
                        st.rerun()
            else:
                st.success("Task input completed!")
                if st.button("Add More Tasks"):
                    st.session_state.input_complete = False
                    st.session_state.celebration_triggered = False  # Reset celebration on adding more tasks
                    st.rerun()
            
            if st.session_state.storage:
                st.write("Current Tasks:")
                for i, task in enumerate(st.session_state.storage, 1):
                    st.write(f"{i}. {task}")
            
            if st.button("Reset All"):
                st.session_state.storage = []
                st.session_state.input_complete = False
                st.session_state.celebration_triggered = False  # Reset celebration on reset
                st.rerun()
        
        st.title("Task Progress Tracker")
        st.write("Here is your Progress bar...")
        
        if st.session_state.input_complete and st.session_state.storage:
            length = len(st.session_state.storage)
            
            st.write(f"Total tasks: {length}")
            
            finished = st.number_input(
                "How many of these have you Completed?",
                min_value=0,
                max_value=length,
                value=0,
                key="completed_tasks"
            )
            
            if finished > 0:
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                for i in range(finished + 1):
                    progress_bar.progress(i / length)
                    status_text.text(f'Progress: {i}/{length} tasks completed')
                    time.sleep(0.1)
                
                percentage = (finished / length) * 100
                st.success(f"You have completed {percentage:.1f}% of work.")
                
                # Check if all tasks are completed and celebration hasn't been triggered
                if finished == length and not st.session_state.celebration_triggered:
                    st.balloons()  # Trigger balloon animation
                    st.session_state.celebration_triggered = True  # Prevent repeated triggers
            else:
                st.progress(0)
                st.text('Progress: 0/0 tasks completed')
        
        elif st.session_state.input_complete and not st.session_state.storage:
            st.warning("No tasks were added!")
        else:
            st.info("Please add tasks using the sidebar to get started.")

def main():
    A = Project2()
    A.shubham()

if __name__ == "__main__":
    main()
    