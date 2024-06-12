def exit_pressure(initial_pressure, exit_area_ratio, specific_heat_ratio):
    """
    Calculates the exit pressure of a nozzle.

    Args:
        initial_pressure (float): Initial pressure (e.g., chamber pressure).
        exit_area_ratio (float): Area ratio at the nozzle exit (A_exit / A_throat).
        specific_heat_ratio (float): Specific heat ratio (γ) of the gas.

    Returns:
        float: Exit pressure...
    """
    exit_pressure = initial_pressure / exit_area_ratio ** (specific_heat_ratio)
    return exit_pressure

# Example usage
initial_pressure = 100000  # Pa (chamber pressure)
exit_area_ratio = 2.5  # A_exit / A_throat
specific_heat_ratio = 1.4  # γ (for air)

exit_p = exit_pressure(initial_pressure, exit_area_ratio, specific_heat_ratio)
print(f"Exit pressure: {exit_p:.2f} Pa")
