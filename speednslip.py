import time
import matplotlib.pyplot as plt
import streamlit as st
import random

# Throttle values should be integers
def generate_throttle_values():
    return random.randint(45, 85)

# Engine speed values should be integers
def generate_engine_speed_values():
    return random.randint(1400, 1500)

# Implement depth values remain with two decimal precision
def generate_implement_depth_values():
    return round(random.uniform(5, 45), 2)

# Forward speed values remain with two decimal precision
def generate_forward_speed_values():
    return round(random.uniform(0.8, 4.5), 2)

# Slip percentage as a float with two decimal precision
def calculate_slip():
    return round(random.uniform(12.10, 17.85), 2)

# Gear ratios as per the provided list
gear_ratios = [160, 120, 80, 40, 30]

# Rest of your code remains the same but ensure the formulas for ent and fcp are correct.

# Main function to display tractor parameters
def display_parameters():
    st.markdown("<h1>Real-time Tractor Performance Prediction</h1>", unsafe_allow_html=True)

    # Initialize placeholders for output and graph
    output_placeholder = st.empty()
    graph_placeholder = st.empty()

    # Initialize lists to store data for plotting
    throttle_values = []
    engine_speed_values = []
    forward_speed_values = []
    implement_depth_values = []
    slip_values = []
    engine_torque_values = []
    fuel_consumption_values = []
    engine_power_values = []
    specific_fuel_consumption_values = []
    fuel_consumption_area_values = []
    implement_draft_values = []
    drawbar_power_values = []
    tractive_efficiency_values = []
    time_stamps = []

    # Infinite loop for continuous data generation
    while True:
        time_stamp = len(time_stamps)  # Using the list length as a time index

        # Calculate new parameters
        params = calculate_parameters()

        # Append new values to lists
        throttle_values.append(params['throttle'])
        engine_speed_values.append(params['engine_speed'])
        forward_speed_values.append(params['forward_speed'])
        implement_depth_values.append(params['implement_depth'])
        slip_values.append(params['slip'])
        engine_torque_values.append(params['engine_torque'])
        fuel_consumption_values.append(params['fuel_consumption'])
        engine_power_values.append(params['engine_power'])
        specific_fuel_consumption_values.append(params['specific_fuel_consumption'])
        fuel_consumption_area_values.append(params['fuel_consumption_area'])
        implement_draft_values.append(params['implement_draft'])
        drawbar_power_values.append(params['drawbar_power'])
        tractive_efficiency_values.append(params['tractive_efficiency'])
        time_stamps.append(time_stamp)

        # Generate the table with icons and larger font
        table_html = generate_table_html(params)
        output_placeholder.markdown(table_html, unsafe_allow_html=True)

        # Plot the real-time data on the right with dots and shaded areas
        fig, ax = plt.subplots(8, 1, figsize=(10, 15), sharex=True)

        ax[0].plot(time_stamps, engine_torque_values, label="Engine Torque (Nm)", color='green', marker='o')
        ax[0].fill_between(time_stamps, engine_torque_values, color='green', alpha=0.2)

        ax[1].plot(time_stamps, fuel_consumption_values, label="Fuel consumption (L/h)", color='blue', marker='o')
        ax[1].fill_between(time_stamps, fuel_consumption_values, color='blue', alpha=0.2)

        ax[2].plot(time_stamps, engine_power_values, label="Engine power (hp)", color='orange', marker='o')
        ax[2].fill_between(time_stamps, engine_power_values, color='orange', alpha=0.2)

        ax[3].plot(time_stamps, specific_fuel_consumption_values, label="Specific fuel consumption (kg/hp-hr)", color='purple', marker='o')
        ax[3].fill_between(time_stamps, specific_fuel_consumption_values, color='purple', alpha=0.2)

        ax[4].plot(time_stamps, fuel_consumption_area_values, label="Fuel consumption per tilled area (L/ha)", color='red', marker='o')
        ax[4].fill_between(time_stamps, fuel_consumption_area_values, color='red', alpha=0.2)

        ax[5].plot(time_stamps, implement_draft_values, label="Implement draft (kN)", color='pink', marker='o')
        ax[5].fill_between(time_stamps, implement_draft_values, color='pink', alpha=0.2)

        ax[6].plot(time_stamps, drawbar_power_values, label="Drawbar power (hp)", color='orange', marker='o')
        ax[6].fill_between(time_stamps, drawbar_power_values, color='orange', alpha=0.2)

        ax[7].plot(time_stamps, tractive_efficiency_values, label="Tractive efficiency (%)", color='blue', marker='o')
        ax[7].fill_between(time_stamps, tractive_efficiency_values, color='blue', alpha=0.2)

        for axis in ax:
            axis.legend(loc="upper right")
            axis.grid(True)

        ax[-1].set_xlabel("Time")

        # Display plot
        graph_placeholder.pyplot(fig)

        # Pause for a short time to simulate real-time behavior
        time.sleep(1)

# Run the real-time display function
if __name__ == "__main__":
    display_parameters()
