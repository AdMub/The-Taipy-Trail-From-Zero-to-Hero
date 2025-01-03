
""" 
from taipy import Gui

if __name__ == "__main__":
    Gui(page="# Hello, *Taipy*!").run(title="Hello, Taipy") 
    """

""" 
from taipy import Gui
import taipy.gui.builder as tgb

text_value = "# Hello, *Taipy*!"

with tgb.Page() as page:
    tgb.text("{text_value}", mode="md", hover_text="Static Text") # mode: md/markdown, pre, raw

if __name__ == "__main__":
    Gui(page).run(debug=True) 
    """

""" 
import taipy.gui.builder as tgb
from taipy.gui import Gui, notify

# Callback for button actions
def on_button_action(state):
    notify(state, 'info', f'The text is: {state.text}')
    state.text = "Button Pressed"

# Special callback for state changes
def on_change(state, var_name, var_value):
    if var_name == "text" and var_value == "Reset":
        state.text = ""
    elif var_name == "slider_value":
        state.number_value = var_value * 2  # Update number_value based on slider
    elif var_name == "toggle_state":
        notify(state, 'info', f'Toggle is now {"ON" if var_value else "OFF"}')

if __name__ == "__main__":
    # Initial state variables
    text = "Original text"
    slider_value = 50
    number_value = 100
    toggle_state = True
    selected_date = None
    uploaded_file = None

    # Define the UI page
    with tgb.Page() as page:
        tgb.text("# Taipy Input Components", mode="md")
        tgb.text("My text: {text}")
        
        # Input component
        tgb.input("{text}", label="Enter your text")
        
        # Slider component
        tgb.slider("{slider_value}", min=0, max=100, step=5, label="Adjust slider")
        
        # Number component
        tgb.number("{number_value}", label="Number Input")
        
        # Toggle component
        tgb.toggle("{toggle_state}", label="Toggle state")
        
        # Date picker component
        tgb.date("{selected_date}", label="Pick a date")
        
        # File upload component
        tgb.file_selector("{uploaded_file}", label="Upload a file", extensions=".csv,.xlsx")

        # Button component
        tgb.button("Submit", on_action=on_button_action)

    # Run the application
    Gui(page).run(debug=True) 
    """

""" 
from taipy.gui import Gui
import taipy.gui.builder as tgb

with tgb.Page() as page:
    # We will add components here one by one

 # Expandable: Creates a collapsible section to group content
    with tgb.expandable("Expandable Section"):
        tgb.text("This is an expandable section. Click to open or close.")

    # Part: Groups elements and can be conditionally displayed
    with tgb.part(render="{True}"):  # Use render="{False}" to hide this part
        tgb.text("This text is inside a part.")
        tgb.button("Click Me")

    # Layout: Arranges elements in a column-based layout, 2:1 ratio
    with tgb.layout(columns="2 1"):
        with tgb.part():
            tgb.text("Column 1")
        with tgb.part():
            tgb.text("Column 2")
            tgb.text("some text here")
        # Combining layouts
    with tgb.layout(columns="1 2"):
        with tgb.part():
            tgb.text("Column 1: Nested Layout")
        with tgb.expandable("Column 2: Expandable"):
            tgb.text("This expandable is inside a column layout.")

Gui(page).run(debug=True) 
"""

""" 
import taipy.gui.builder as tgb
from taipy.gui import Gui

show_dialog = False

def dialog_action(state, _, payload):
    if payload["args"][0] == 0:
        print("Good to hear!")
    elif payload["args"][0] == 1:
        print("Sorry to hear that.")
    else:
        print("Ok bye.")
    state.show_dialog = False

with tgb.Page() as page:
    with tgb.dialog("{show_dialog}", title="Welcome!", on_action=dialog_action, labels="Couldn't be better;Not my day"):
        tgb.html("h2", "Hello!")

    tgb.button("Show", on_action=lambda s: s.assign("show_dialog", True))

if __name__ == "__main__":
    Gui(page).run(title="Dialog - Labels")
 """

from taipy.gui import Gui
import taipy.gui.builder as tgb

# Define the root page with navigation
with tgb.Page() as root_page:
    tgb.navbar()  # Default navigation bar
    tgb.text("# Welcome to the Multi-Page Application", mode="md")

# Define Page 1
with tgb.Page() as page_1:
    tgb.text("## This is Page 1", mode="md")

# Define Page 2
with tgb.Page() as page_2:
    tgb.text("## This is Page 2", mode="md")

# Combine all pages
pages = {
    "/": root_page,
    "page1": page_1,
    "page2": page_2
}

# Run the application
Gui(pages=pages).run()