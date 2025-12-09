import streamlit as st
from math import pi

# Initialize session state values
num_assemblies = st.session_state.num_assemblies if 'num_assemblies' in st.session_state else 2

if 'page' not in st.session_state:
    st.session_state.page = "Vertical String Orientation Calculator"  # Default to the first tab
if 'num_assemblies' not in st.session_state:
    st.session_state.num_assemblies = 1  # Default to 1 assembly
if 'assembly_data' not in st.session_state:
    st.session_state.assembly_data = []  # Store data for assemblies
if 'distance' not in st.session_state:
    st.session_state.distance = None
if 'diameter' not in st.session_state:
    st.session_state.diameter = None
if 'rotary_angle' not in st.session_state:
    st.session_state.rotary_angle = None
if 'top_assembly_angle' not in st.session_state:
    st.session_state.top_assembly_angle = None
if 'rotary_result' not in st.session_state:
    st.session_state.rotary_result = None
if 'top_result' not in st.session_state:
    st.session_state.top_result = None
if 'angle_known' not in st.session_state:
    st.session_state.angle_known = "Yes"
if 'top_angle_known' not in st.session_state:
    st.session_state.top_angle_known = "Yes"
if 'total_angle_result' not in st.session_state:
    st.session_state.total_angle_result = None

# Display image above the title
st.logo("https://github.com/NeoJammerZX/String-calculator/blob/main/VallourecLogo.png", size="large", link="https://solutions.vallourec.com/services/orientation-by-vam-field-service/")

# Sidebar navigation with gradient background and enforced white text
st.markdown(
    """
    <style>
    /* Style the sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(to top, #172983, #009ee0); /* Gradient background */
        color: white !important; /* Default text color */
    }
    /* Style the sidebar title */
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
        color: white !important; /* Ensure all sidebar headings are white */
    }
    /* Style the radio buttons in the sidebar */
    [data-testid="stSidebar"] .css-1v3fvcr, [data-testid="stSidebar"] .css-qrbaxs {
        color: white !important; /* Ensure radio button labels are white */
    }
    /* Style the "Go to" label */
    [data-testid="stSidebar"] label {
        color: white !important; /* Ensure the "Go to" text is white */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar navigation
st.sidebar.title("Navigation")
st.session_state.page = st.sidebar.radio(
    "Go to:",
    ["Vertical String Orientation Calculator", "Horizontal Assemblies Configuration", "Documentation"]
)

# Add descriptions in the sidebar
if st.session_state.page == "Vertical String Orientation Calculator":
    st.sidebar.image(
        r"https://github.com/NeoJammerZX/String-calculator/blob/main/RotaryRef1.png",  # Replace with the actual path to your image
        caption="For rig applications and aligning two assemblies like a hanger to a well slot",
        use_container_width=True
    )
elif st.session_state.page == "Horizontal Assemblies Configuration":
    st.sidebar.image(
        r"https://github.com/NeoJammerZX/String-calculator/blob/main/AssemblyRef.png",  # Replace with the actual path to your image
        caption="For assemblies made up in workshop applications like smart completion tools",
        use_container_width=True
    )
elif st.session_state.page == "Documentation":
    st.sidebar.image(
        r"https://github.com/NeoJammerZX/String-calculator/blob/main/AssemblyMakeUpRef.png",  # Replace with the actual path to your image
        caption="Technical reference section for this site and documentation relevant to job execution",
        use_container_width=True
    )
    
# Documentation Section
if st.session_state.page == "Documentation":
    st.title("Documentation")
    st.markdown(
    """<hr style="
        margin: 0px 0;
        border: none;
        border-top: 510px;
        background: linear-gradient(to right, #f9ff00, #008 ee0);
        height: 10px;
    " />""",
    unsafe_allow_html=True)
    
# Procedure Link
    st.subheader("Procedure")
    st.markdown(
        """
        <p style="font-size: 14px;">
        Click the link below to access the procedure documentation:
        </p>
        <a href="https://vallourec.unificence.com" target="_blank" style="font-size: 16px; color: #009ee0; text-decoration: none;">
        ➡️ Open Procedure Documentation
        </a>
        """,
        unsafe_allow_html=True
    )
# Provision for Images or GIFs
    st.subheader("Visual Guides")
    st.markdown(
        """
        <p style="font-size: 14px;">
        Below are visual guides (e.g., images or GIFs) to help you understand the process:
        </p>
        """,
        unsafe_allow_html=True
    )
    # Example GIF/Image Placeholder
    st.image(
        r"https://github.com/NeoJammerZX/String-calculator/blob/main/barrettescheck.gif",
        caption="Ensure the barrettes are properly checked and calibrated before use",
        use_container_width=True
    )
    # Display two images side by side
    col1, col2 = st.columns(2)  # Create two columns
    with col1:
        st.image(
            r"https://github.com/NeoJammerZX/String-calculator/blob/main/barrettepin.gif",
            caption="The barrettes will stop at the pin or box shoulder",
            use_container_width=True
        )
    with col2:
        st.image(
            r"https://github.com/NeoJammerZX/String-calculator/blob/main/barrettebox.gif",  # Replace with the second image path
            caption="Clearly mark this stop point on the connection body",
            use_container_width=True
        )
        
    st.image(
        r"https://github.com/NeoJammerZX/String-calculator/blob/main/DistanceMethod.png",
        caption="Due to its accuracy, the distance method is the primary way of determining the angle between two barrette marks",
        use_container_width=True
    )
    
# Function to calculate rotary angle
def calculate_rotary_angle(x, D):
    if x < 0 or D < 0:
        return "Error: Negative values are not allowed"
    if D == 0:
        return "Error: Diameter cannot be zero"
    rotary_result = round((x / D) * (360 / pi), 2)
    if rotary_result < 0 or rotary_result > 360:
        return "Error: Resulting angle is not possible"
    return rotary_result

# Function to calculate total angle for Vertical String Orientation Calculator
def calculate_total_angle(angle_rotary, angle_assembly):
    if angle_rotary < 0 or angle_assembly < 0:
        return "Error: Negative angles are not allowed"
    total_angle = angle_rotary + angle_assembly
    if total_angle <= 360:
        result = 360 - total_angle
    else:
        result = 720 - total_angle
    if result < 0 or result > 360:
        return "Error: Resulting angle is not possible"
    return f"Angle of Pup Joint needed: **{result:.2f}**°"

# Function to calculate total angle for Horizontal Assemblies Configuration
def calculate_horizontal_total_angle(angle_assembly_n, angle_assembly_n_plus_1):
    if angle_assembly_n < 0 or angle_assembly_n_plus_1 < 0:
        return "Error: Negative angles are not allowed"
    total_angle = angle_assembly_n + angle_assembly_n_plus_1
    if total_angle <= 360:
        result = 360 - total_angle
    else:
        result = 720 - total_angle
    if result < 0 or result > 360:
        return "Error: Resulting angle is not possible"
    return f"**{result:.2f}**°"

# Page 1: Vertical String Orientation Calculator
if st.session_state.page == "Vertical String Orientation Calculator":
    st.title("Vertical String Orientation Calculator")
    st.markdown(
    """<hr style="
        margin: 10px 0;
        border: none;
        border-top: 10px;
        background: linear-gradient(to right, #172983, #009ee0);
        height: 10px;
    " />""",
    unsafe_allow_html=True)

# Inject custom CSS for styling input boxes
    st.markdown(
    """
    <style>
    /* Style for number and text input boxes */
    input[type="number"], input[type="text"] {
        background-color: #172983; /* Light blue background */
        border: 2px solid #009ee0; /* Blue border */
        border-radius: 5px; /* Rounded corners */
        color: #FFFFFF; /* White text */
        padding: 5px; /* Add padding inside the input box */
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Rotary Angle Calculator inside a container
    with st.container(border=True):
        st.markdown(
        """
        <div style="
            background-color: rgba(0, 158, 224, 0.7); /* Blue background with 70% transparency */
            padding: 20px;
            border: 30px solid #009ee0; /* Solid blue border */
            border-radius: 0px;
        ">
        """,
        unsafe_allow_html=True
    )
        st.subheader("Rotary Angle Calculator")
        st.session_state.angle_known = st.radio(
        "Do you know the **angle of the coupling in the rotary?**",
        ("Yes", "No"),
        index=0 if st.session_state.angle_known == "Yes" else 1
    )
        if st.session_state.angle_known == "Yes":
            angle = st.number_input(
            "Angle of the coupling in the rotary:",
            min_value=0.0,
            max_value=360.0,
            step=1.0,
            value=st.session_state.rotary_angle,
            key="rotary_angle_input"
        )
            st.session_state.rotary_angle = angle
        else:
            # Redirect to input distance and diameter
            st.session_state.distance = st.number_input(
                "What is the distance, x?",
                format="%.2f",
                min_value=0.00,
                value=st.session_state.distance,
                key="rotary_distance"
        )
            st.session_state.diameter = st.number_input(
                "What is the diameter, D?",
                format="%.2f",
                min_value=0.00,
                value=st.session_state.diameter,
                key="rotary_diameter"
        )

        col1, col2, col3 = st.columns(3)
    with col1:
        # Disable "Calculate Rotary Angle" button if toggle is "Yes"
        calculate_disabled = st.session_state.angle_known == "Yes"
        if st.button(
            "Calculate Rotary Angle",
            key="calculate_rotary",
            help="Calculate the rotary angle",
            use_container_width=True,
            disabled=calculate_disabled
        ):
            st.session_state.rotary_result = calculate_rotary_angle(st.session_state.distance, st.session_state.diameter)
            if isinstance(st.session_state.rotary_result, (int, float)):
                st.session_state.rotary_angle = st.session_state.rotary_result
                st.success(f"Calculated Rotary Angle: **{st.session_state.rotary_result}**°", icon="✅")
            else:
                st.warning(st.session_state.rotary_result, icon="⚠️")
    with col2:
        if st.button(
            "Refresh Rotary Inputs",
            key="refresh_rotary",
            help="Refresh the input values",
            use_container_width=True
        ):
            st.session_state.distance = None
            st.session_state.diameter = None
            st.session_state.rotary_angle = None
            st.rerun()
    with col3:
        # Disable "Use Calculated Rotary Value" button if toggle is "Yes"
        use_calculated_disabled = st.session_state.angle_known == "Yes"
        if st.button(
            "Use Calculated Rotary Value",
            key="use_calculated_rotary",
            help="Use the calculated value",
            use_container_width=True,
            disabled=use_calculated_disabled
        ):
            if isinstance(st.session_state.rotary_result, (int, float)):
                st.session_state.rotary_angle = st.session_state.rotary_result
                st.session_state.angle_known = "Yes"
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    # Top Assembly Angle Calculator
    st.markdown(
    """<hr style="
        margin: -20px 0;
        border: none;
        border-top: 50px;
        background: linear-gradient(to right, #172983, #009ee0);
        height: 10px;
    " />""",
    unsafe_allow_html=True)

    with st.container(border=True):
        st.subheader("Top Assembly Angle Calculator")
        st.session_state.top_angle_known = st.radio(
        "Do you know the **angle of the top assembly?**",
        ("Yes", "No"),
        index=0 if st.session_state.top_angle_known == "Yes" else 1
    )
        if st.session_state.top_angle_known == "Yes":
            top_angle = st.number_input(
            "Angle of the top assembly:",
            min_value=0.0,
            max_value=360.0,
            step=1.0,
                value=st.session_state.top_assembly_angle,
            key="top_assembly_angle_input"
        )
            st.session_state.top_assembly_angle = top_angle
        else:
        # Redirect to input distance and diameter
            top_distance = st.number_input(
            "What is the distance, x?",
            format="%.2f",
            min_value=0.00,
                value=st.session_state.distance,
            key="top_distance"
        )
            top_diameter = st.number_input(
            "What is the diameter, D?",
            format="%.2f",
            min_value=0.00,
            value=st.session_state.diameter,
            key="top_diameter"
        )

        col1, col2, col3 = st.columns(3)
    with col1:
        # Disable "Calculate Top Assembly Angle" button if toggle is "Yes"
        calculate_disabled = st.session_state.top_angle_known == "Yes"
        if st.button(
            "Calculate Top Assembly Angle",
            key="calculate_top",
            help="Calculate the top assembly angle",
            use_container_width=True,
            disabled=calculate_disabled
        ):
            st.session_state.top_result = calculate_rotary_angle(top_distance, top_diameter)
            if isinstance(st.session_state.top_result, (int, float)):
                st.session_state.top_assembly_angle = st.session_state.top_result
                st.success(f"Calculated Top Assembly Angle: **{st.session_state.top_result}**°", icon="✅")
            else:
                st.warning(st.session_state.top_result, icon="⚠️")
    with col2:
        if st.button(
            "Refresh Top Assembly Inputs",
            key="refresh_top",
            help="Refresh the input values",
            use_container_width=True
        ):
            st.session_state.distance = None
            st.session_state.diameter = None
            st.session_state.top_assembly_angle = None
            st.rerun()
    with col3:
        # Disable "Use Calculated Top Assembly Value" button if toggle is "Yes"
        use_calculated_disabled = st.session_state.top_angle_known == "Yes"
        if st.button(
            "Use Calculated Top Assembly Value",
            key="use_calculated_top",
            help="Use the calculated value",
            use_container_width=True,
            disabled=use_calculated_disabled
        ):
            if isinstance(st.session_state.top_result, (int, float)):
                st.session_state.top_assembly_angle = st.session_state.top_result
                st.session_state.top_angle_known = "Yes"
            st.rerun()

    st.markdown(
    """<hr style="
        margin: 10px 0;
        border: none;
        border-top: 10px;
        background: linear-gradient(to right, #172983, #009ee0);
        height: 10px;
    " />""",
    unsafe_allow_html=True)

    # Total angle calculation
    col1, col2, col3 = st.columns([1, 2, 1])  # Create three columns, with the middle column wider
    with col2:  # Place the button in the center column
        if st.button("Calculate Total Angle", key="calculate_total", help="Calculate the total angle using rotary and top assembly angles", use_container_width=True):
            if isinstance(st.session_state.rotary_angle, (int, float)) and isinstance(st.session_state.top_assembly_angle, (int, float)):
                result = calculate_total_angle(st.session_state.rotary_angle, st.session_state.top_assembly_angle)
                if isinstance(result, str):
                    st.success(result, icon="✅")
            else:
                st.warning("Please ensure both angles are provided before calculating.", icon="⚠️")

    # Refresh all inputs
    col1, col2, col3 = st.columns([1, 2, 1])  # Create three columns, with the middle column wider
    with col2:  # Place the button in the center column
        if st.button("Refresh All", key="refresh_all", help="Clear all input values", use_container_width=True):
            for key in ['distance', 'diameter', 'rotary_angle', 'top_assembly_angle', 'rotary_result', 'top_result', 'total_angle_result']:
                st.session_state[key] = None
            # Default toggles to "Yes"
            st.session_state.angle_known = "Yes"
            st.session_state.top_angle_known = "Yes"
            st.rerun()

# Page 2: Horizontal Assemblies Configuration
elif st.session_state.page == "Horizontal Assemblies Configuration":
    st.title("Horizontal Assemblies Configuration")
    st.markdown(
    """<hr style="
        margin: 10px 0;
        border: none;
        border-top: 10px;
        background: linear-gradient(to right, #172983, #009ee0);
        height: 10px;
    " />""",
    unsafe_allow_html=True)

    # Section 1: Input for number of assemblies
    num_assemblies = st.slider(
        "Specify the number of assemblies (Max: 7):",
        min_value=2,
        max_value=7,
        value=3,  # Default to 3 assemblies for demonstration
        help="Use the slider to indicate how many assemblies are present in the string."
    )

    # Initialize or update assembly data
    if "assembly_data" not in st.session_state or len(st.session_state.assembly_data) != num_assemblies:
        st.session_state.assembly_data = [
            {"assembly_number": num_assemblies-i, "name": f"Assy {num_assemblies-i}", "angle": None, "x": None, "D": None, "angle_known": "Yes"}
            for i in range(num_assemblies)
        ]
    # Section 2: Define Assembly Names
    st.markdown(
    "<h6 style='margin-top: 10x;'>Define Assembly Names</h6>",  # Smaller heading with reduced margin
    unsafe_allow_html=True
)
    st.markdown(
    """<hr style="
        margin: 0 0;
        border: none;
        border-top: 100px;
        background: linear-gradient(to right, #172983, #009ee0);
        height: 10px;
    " />""",
    unsafe_allow_html=True)
    st.markdown(
    """
    <style>
    /* Style for number and text input boxes */
    input[type="number"], input[type="text"] {
        background-color: #172983; /* Light blue background */
        border: 2px solid #009ee0; /* Blue border */
        border-radius: 5px; /* Rounded corners */
        color: #FFFFFF; /* White text */
        padding: 5px; /* Add padding inside the input box */
    }
    </style>
    """,
    unsafe_allow_html=True
)
    for i in range(num_assemblies - 1, -1, -1):
        st.session_state.assembly_data[i]["name"] = st.text_input(
        "",  # No label for the text input
        value=st.session_state.assembly_data[i]["name"],
        key=f"assembly_name_{i + 1}"
    )
        st.markdown(
    """
    <style>
    .stTextInput {
        margin-bottom: -50px;  /* Reduce spacing between text input fields */
    }
    </style>
    """,
    unsafe_allow_html=True
)
    # Section 3: Visualize Assemblies and Pup Joints
    st.markdown(
        """<hr style="
            margin: 50px 0;
            border: none;
            border-top: 10px;
            background: linear-gradient(to right, #172983, #009ee0);
            height: 10px;
        " />""",
        unsafe_allow_html=True
    )
    st.markdown("###### Visualize Assemblies and Pup Joints")  # Smaller heading

    # Add a note about the assembly layout
    st.markdown(
    """
    <p style="font-size: 14px; font-style: italic; background-color: #ffffcc; padding: 10px; border-radius: 5px;">
    *The first assembly is on the right, and this represents the bottom of the assembly.
    </p>
    """,
    unsafe_allow_html=True
)
    assembly_cols = st.columns(2 * num_assemblies - 1)[::-1]  # Create columns for assemblies and pup joints
    for i in range(2 * num_assemblies - 1):
        with assembly_cols[i]:
            if i % 2 == 0:  # Assembly slots
                assembly_index = i // 2  # Calculate the reversed assembly index
                reversed_index = num_assemblies - 1 - assembly_index  # Reverse the index for right-to-left layout
                st.image(
                    r"https://github.com/NeoJammerZX/String-calculator/blob/main/vssymbol.jpg",  # Replace with actual image path
                    caption=f"{st.session_state.assembly_data[reversed_index]['name']}",  # Reverse the assembly names
                    use_container_width=True
                )
            else:  # Pup joint slots
                joint_number = i // 2 + 1  # Calculate the joint number
                reversed_joint_number = joint_number  # Reverse the joint number for right-to-left layout
                if (
                    st.session_state.assembly_data[num_assemblies - 1 - (i // 2)].get("angle") is not None
                    and st.session_state.assembly_data[num_assemblies - 2 - (i // 2)].get("angle") is not None
                ):
                    total_angle = calculate_horizontal_total_angle(
                        st.session_state.assembly_data[num_assemblies - 1 - (i // 2)]["angle"],
                        st.session_state.assembly_data[num_assemblies - 2 - (i // 2)]["angle"]
                    )
                    # Display both the image and the calculated angle text
                    st.image(
                        r"https://github.com/NeoJammerZX/String-calculator/blob/main/pupjoint.jpg",  # Placeholder for pup joint image
                        caption=f"Joint {reversed_joint_number}",
                        use_container_width=True
                    )
                    st.markdown(
                    f"{total_angle}",
                    unsafe_allow_html=True
                )
                else:
                # Display only the image if angles are not available
                    st.image(
                        r"https://github.com/NeoJammerZX/String-calculator/blob/main/pupjoint.jpg",  # Placeholder for pup joint image
                        caption=f"Joint {reversed_joint_number}",
                        use_container_width=True
                )

    # Section 4: Additional Inputs for Assemblies
    cols = st.columns(num_assemblies)  # Create one column per assembly
    # Inject custom CSS for input box styling
    st.markdown(
    """
    <style>
    /* Style for number input boxes */
    input[type="number"] {
        background-color: #172983; /* Light blue background */
        border: 2px solid #009ee0; /* Blue border */
        border-radius: 5px; /* Rounded corners */
        color: #FFFFFF; /* Dark blue text */
        padding: 5px; /* Add padding inside the input box */
    }
    /* Style for radio buttons */
    div[data-baseweb="radio"] {
        background-color: #e6f7ff; /* Light blue background for radio buttons */
        border: 2px solid #009ee0; /* Blue border */
        border-radius: 5px; /* Rounded corners */
        padding: 10px; /* Add padding inside the radio button container */
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Angle known toggle and dynamic inputs
    for i, col in enumerate(cols):
        with col:
        # Angle known toggle
            st.session_state.assembly_data[i]["angle_known"] = st.radio(
                f"Angle known?",
                ("Yes", "No"),
                index=0 if st.session_state.assembly_data[i]["angle_known"] == "Yes" else 1,
                key=f"angle_known_{i + 1}"
        )

            if st.session_state.assembly_data[i]["angle_known"] == "Yes":
            # Input box for angle
                st.session_state.assembly_data[i]["angle"] = st.number_input(
                    f"Angle:",
                    min_value=0.0,
                    max_value=360.0,
                    step=1.0,
                    value=st.session_state.assembly_data[i]["angle"] or None,
                    key=f"angle_{i + 1}"
            )
            else:
                # Redirect to input distance (x) and diameter (D)
                st.session_state.assembly_data[i]["x"] = st.number_input(
                    f"x (Distance):",
                    min_value=0.0,
                    value=st.session_state.assembly_data[i]["x"] or 0.0,
                    key=f"x_{i + 1}"
            )
                st.session_state.assembly_data[i]["D"] = st.number_input(
                    f"D (Diameter):",
                    min_value=0.0,
                    value=st.session_state.assembly_data[i]["D"] or 0.0,
                    key=f"D_{i + 1}"
            )

            # Auto-calculate angle if x and D are provided
                if st.session_state.assembly_data[i]["x"] > 0 and st.session_state.assembly_data[i]["D"] > 0:
                    st.session_state.assembly_data[i]["angle"] = calculate_rotary_angle(
                        st.session_state.assembly_data[i]["x"],
                        st.session_state.assembly_data[i]["D"]
                    )
                    st.success(f"Calculated Angle: {st.session_state.assembly_data[i]['angle']}°", icon="✅")
                    
                    # Add "Use Calculated Value" button
                    if st.button(
                        f"Use Calculated Value",
                        key=f"use_calculated_{i + 1}",
                        help="Use the calculated angle value",
                        use_container_width=True
                    ):
                        st.session_state.assembly_data[i]["angle_known"] = "Yes"
                    st.session_state.assembly_data[i]["angle"] = st.session_state.assembly_data[i]["angle"]

    st.markdown(
        """<hr style="
            margin: -20px 0;
            border: none;
            border-top: -20px;
            background: linear-gradient(to right, #009ee0, #009ee0);
            height: 10px;
        " />""",
        unsafe_allow_html=True
    )
    # Calculate Joint Angles for Horizontal Assemblies Configuration
    col1, col2, col3 = st.columns([1, 2, 1])  # Create three columns, with the middle column wider
    with col2:  # Place the button in the center column
        if st.button("Calculate Joint Angles", key="calculate_joint_angles", help="Recalculate all joint angles", use_container_width=True):
        # Iterate through all pup joints and recalculate angles
            for i in range(num_assemblies - 1):
                if (
                    st.session_state.assembly_data[i].get("angle") is not None
                    and st.session_state.assembly_data[i + 1].get("angle") is not None
            ):
                # Recalculate the total angle for the pup joint
                    total_angle = calculate_horizontal_total_angle(
                        st.session_state.assembly_data[i]["angle"],
                        st.session_state.assembly_data[i + 1]["angle"]
                )
                else:
                    st.warning(f"Missing angles for Assembly {i + 1} or Assembly {i + 2}. Cannot calculate Joint {i + 1}.", icon="⚠️")
                    # Refresh all inputs for Horizontal Assemblies Configuration
    col1, col2, col3 = st.columns([1, 2, 1])  # Create three columns, with the middle column wider
    with col2:  # Place the button in the center column
        if st.button("Refresh All", key="refresh_all_horizontal", help="Clear all input values for assemblies", use_container_width=True):
        # Reset all assembly-related session state variables
            for i, assembly in enumerate(st.session_state.assembly_data):
                assembly["angle"] = None
                assembly["x"] = None
                assembly["D"] = None
                assembly["angle_known"] = "Yes"
                assembly["name"] = f"Assy {i + 1}"  # Reset the name to default (e.g., "Assy 1", "Assy 2", etc.)
            st.session_state.num_assemblies = 2  # Reset to default number of assemblies
            st.rerun()  


