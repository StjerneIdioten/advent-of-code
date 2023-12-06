from pathlib import Path

with open(Path(__file__).parent / "test") as file:
    # Seeds
    seeds = list(map(int, file.readline().rstrip('\n').split()[1:]))
    file.readline()

    print(f"Seeds: {seeds}")

    # Seed to soil
    file.readline()
    seed_to_soil = []
    while (line := file.readline()) != '\n':
        seed_to_soil.append(tuple(map(int, line.rstrip('\n').split())))

    print(f"Seed to soil: {seed_to_soil}")

    # Soil to fertilizer
    file.readline()
    soil_to_fertilizer = []
    while (line := file.readline()) != '\n':
        soil_to_fertilizer.append(tuple(map(int, line.rstrip('\n').split())))

    print(f"Soil to fertilizer: {soil_to_fertilizer}")
        
    # Fertilizer to water
    file.readline()
    fertilizer_to_water = []
    while (line := file.readline()) != '\n':
        fertilizer_to_water.append(tuple(map(int, line.rstrip('\n').split())))

    print(f"Fertilizer to water: {fertilizer_to_water}")

    # Water to light
    file.readline()
    water_to_light = []
    while (line := file.readline()) != '\n':
        water_to_light.append(tuple(map(int, line.rstrip('\n').split())))

    print(f"Water to light: {water_to_light}")

    # Light to temperature
    file.readline()
    light_to_temperature = []
    while (line := file.readline()) != '\n':
        light_to_temperature.append(tuple(map(int, line.rstrip('\n').split())))

    print(f"Light to temperature: {light_to_temperature}")

    # Temperature to humidity
    file.readline()
    temperature_to_humidity = []
    while (line := file.readline()) != '\n':
        temperature_to_humidity.append(tuple(map(int, line.rstrip('\n').split())))

    print(f"Temperature to humidity: {temperature_to_humidity}")

    # Humidity to location
    file.readline()
    humidity_to_location = []
    while (line := file.readline()) != '' :
        humidity_to_location.append(tuple(map(int, line.rstrip('\n').split())))

    print(f"Humidity to location: {humidity_to_location}")

    
        
