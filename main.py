import sys
from calculator import get_emission_factor_for_fuel, compute_carbon_emission
def run_carbon_app():
    
    print("\n                                                  ========================================                                                                   ")
    print("                                                   CALCULATING CARBON EMISSION FROM CAR                                                                      ")
    print("                                                  ========================================                                                                   ")

    try:
        user_fuel_choice_num = input("Enter which type of fuel your car uses (1 for Petrol / 2 for Diesel): ")
        display_fuel_type_name = "Unknown"

        if user_fuel_choice_num == "1":
            display_fuel_type_name = "Petrol"
        elif user_fuel_choice_num == "2":
            display_fuel_type_name = "Diesel"
        
        current_emission_factor = get_emission_factor_for_fuel(user_fuel_choice_num)

        if current_emission_factor is None:
            print("WRONG FUEL TYPE ENTERED")
            sys.exit()
           

        journey_distance_input = float(input("Input the total distance you would cover in car (in kilometers): "))
        vehicle_efficiency_input = float(input("Enter your car's fuel efficiency(Km/L): "))

        calculated_emission_output = compute_carbon_emission(journey_distance_input, vehicle_efficiency_input, current_emission_factor)

        print("\n--- Detailed Carbon Emission Report ---")
        print(f"Fuel Source:    {display_fuel_type_name}")
        print(f"Distance Traveled: {journey_distance_input} km")
        print(f"Fuel Economy:   {vehicle_efficiency_input} km/L")
        print("-" * 30)
        print(f"                                             ESTIMATED Carbon OUTPUT IS: < {calculated_emission_output} > kg")
    
        if calculated_emission_output > 130.0:
            print("========================================================================================================================================================")
            print("==================================PLEASE USE PUBLIC TRANSPORT SUCH AS TRAIN OR BUSES OR FLIGHTS FOR LONG DISTANCE TRAVEL==================================")
            print("========================================================================================================================================================")
        elif 80 < calculated_emission_output < 130:
            print("========================================================================================================================================================")
            print("=================================YOUR CAR IS POLLUTING THE ENVIRONMENT PLEASE PLANT SOME TREES!!!!!!!!!!!!!!!!!!!!======================================")
            print("========================================================================================================================================================")
        else:
            print("========================================================================================================================================================")
            print("=================================YOUR VEHICLE IS GOOD FOR USE AND ENVIRONMENT FRIENDLY , KEEP DRIVING  ^_^  ============================================")
            print("========================================================================================================================================================")
   
    except ValueError:
        print("\n[INPUT ERROR] Please ensure you enter valid numerical values (digits only) for distance and fuel efficiency.")

if __name__ == "__main__":
    run_carbon_app()
    print()
    print()
    print("                                                       ^_^  HAVE A GOOD RIDE  ^_^                                                                              ")
