def get_emission_factor_for_fuel(fuel_type_str):
   
    fuel_type_input = fuel_type_str.lower().strip()

    if fuel_type_input == "1":
        return 2.31 
    elif fuel_type_input == "2":
        return 2.68 
    else:
               return None

def compute_carbon_emission(travel_distance_km, vehicle_mileage_kml, emission_factor_value):
   
    if vehicle_mileage_kml <= 0:
       
        return 0.0

    fuel_used_liters = travel_distance_km / vehicle_mileage_kml

    total_carbon_emission = fuel_used_liters * emission_factor_value

    return round(total_carbon_emission, 2)
