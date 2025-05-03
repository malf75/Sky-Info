def moon_phase(value: float):
    if 0 <= value <= 2.33:
        return "New Moon (Invisible)"
    elif 2.34 <= value <= 4.66:
        return "Waxing Crescent (Early)"
    elif 4.67 <= value <= 6.99:
        return "Waxing Crescent (Late)"
    elif 7 <= value <= 9.33:
        return "First Quarter (Early)"
    elif 9.34 <= value <= 11.66:
        return "Waxing Gibbous (Early)"
    elif 11.67 <= value <= 13.99:
        return "Waxing Gibbous (Late)"
    elif 14 <= value <= 16.33:
        return "Waxing Gibbous (Very Late)"
    elif 16.34 <= value <= 18.66:
        return "Full Moon (Peak)"
    elif 18.67 <= value <= 20.99:
        return "Waning Gibbous (Early)"
    elif 21 <= value <= 23.33:
        return "Waning Gibbous (Late)"
    elif 23.34 <= value <= 25.66:
        return "Last Quarter (Early)"
    elif 25.67 <= value <= 27.99:
        return "Waning Crescent"
    else:
        return "Unknown"