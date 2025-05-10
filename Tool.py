import os
import random
import time
from abc import ABC, abstractmethod

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')




"""Abstract Tool class"""
class Tool(ABC):
    def __init__(self, name: str, material: str, weight: float):
        self.name = name
        self.material = material
        self.weight = weight
        self.durability = 100

    @abstractmethod
    def use(self) -> None:
        pass

    @abstractmethod
    def repair(self) -> None:
        pass

    def degrade(self, amount: int = 3):
        self.durability -= amount
        if self.durability < 0:
            self.durability = 0

    def check_durability(self) -> bool:
        return self.durability > 0





"""Hammer class"""
class Hammer(Tool):
    def __init__(self, name: str, material: str, weight: float, head_type: str, claw_type: str, handle_length: int):
        super().__init__(name, material, weight)
        self.head_type = head_type
        self.claw_type = claw_type
        self.handle_length = handle_length

    def use(self) -> None:
        if not self.check_durability():
            print("The hammer is too damaged to use. Please repair it.")
            return

        while True:
            clear_screen()
            print(f"Using the {self.name} made of {self.material}, weighing {self.weight}kg, with a {self.handle_length}-inch handle.")
            print("\nHammer Use Menu")
            print("================")
            print("1. Strike a Nail")
            print("2. Remove Nails")
            print("3. Back")

            choice = input("\nEnter your choice (1-3): ")

            if choice == "1":
                self.strike()
            elif choice == "2":
                self.remove_nails()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please select a number from 1 to 3.")
                input("\nPress Enter to return to the menu...")

    def strike(self) -> None:
        if not self.check_durability():
            print("The hammer is too damaged to strike. Please repair it.")
            return

        print(f"Striking with the {self.head_type} hammer...\n")

    
        depth_states = {
            1: "1/4 in",
            2: "1/2 in",
            3: "3/4 in",
            4: "almost in",
            5: "fully driven"
        }

        current_strike = 0
        total_strikes_needed = random.randint(2, 5) 

        while current_strike < total_strikes_needed:
            input(f"Press Enter to strike the nail (Strike #{current_strike + 1})... ")
            current_strike += 1

           
            random_depth = random.randint(1, 5)
            depth = depth_states.get(random_depth, "fully driven")

            if current_strike < total_strikes_needed:
                print(f"The nail is {depth} into the wood. Keep striking.\n")
            else:
                print(f"The nail is {depth} into the wood. Fully driven.\n")

            self.degrade()

    def remove_nails(self) -> None:
        if not self.check_durability():
            print("The hammer is too damaged to remove nails. Please repair it.")
            return

       
        print(f"Removing nails using the {self.claw_type} claw... Done.")
        input("Press Enter to continue...")  
        self.degrade()

    def repair(self) -> None:
        self.durability = 100
        print(f"Repaired the {self.name} hammer. Durability is now full.")






"""Drill class"""
class Drill(Tool):
    def __init__(self, name: str, material: str, weight: float, power_rating: float, is_cordless: bool, drill_speed: int):
        super().__init__(name, material, weight)
        self.power_rating = power_rating
        self.is_cordless = is_cordless
        self.drill_speed = drill_speed  
        self.bit = "Standard"
        self.available_bits = ["Standard", "Masonry", "Wood", "Metal", "Glass"]

    def use(self) -> None:
        if not self.check_durability():
            print("The drill is too damaged to use. Please repair it.")
            return

        while True:
            clear_screen()
            print(f"Using the {self.weight}kg {self.name} that is cordless...")
            print("\nDrill Menu")
            print("==========")
            print("1. Drill Hole")
            print("2. Change Bit")
            print("3. Adjust Speed")
            print("4. Back")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.drill_hole()
            elif choice == "2":
                self.change_bit()
            elif choice == "3":
                self.adjust_speed()
            elif choice == "4":
                break
            else:
                print("Invalid choice.")
                input("Press Enter to continue...")

    def drill_hole(self) -> None:
        if not self.check_durability():
            print("The drill is too damaged to drill. Please repair it.")
            return

        print(f"Drilling a hole with {self.bit} bit at {self.drill_speed} RPM...")

        base_time = 5.0  
        rpm_factor = max(0.5, 3000 / self.drill_speed)  
        drill_time = base_time * rpm_factor / 3

        for i in range(int(drill_time), 0, -1):
            print(f"Drilling... {i} seconds remaining")
            time.sleep(1)

        print(f"Hole drilled using {self.bit} bit!\n")
        input("Press Enter to continue...") 
        self.degrade()

    def change_bit(self) -> None:
        print("Available bits:")
        for idx, bit in enumerate(self.available_bits, start=1):
            print(f"{idx}. {bit}")

        choice = input("Select a bit (number): ")
        if choice.isdigit() and 1 <= int(choice) <= len(self.available_bits):
            self.bit = self.available_bits[int(choice) - 1]
            print(f"Drill bit changed to {self.bit}.")
        else:
            print("Invalid selection.")

        input("Press Enter to continue...")

    def adjust_speed(self) -> None:
        try:
            new_speed = int(input("Enter new RPM (e.g. 500, 1000, 1500, 2000, 3000): "))
            if new_speed > 0:
                self.drill_speed = new_speed
                print(f"Speed adjusted to {self.drill_speed} RPM.")
            else:
                print("RPM must be positive.")
        except ValueError:
            print("Invalid RPM input.")

        input("Press Enter to continue...")

    def repair(self) -> None:
        self.durability = 100
        print(f"Repaired the {self.name} drill. Durability is now full.")





"""Saw class"""
class Saw(Tool):
    def __init__(self, name: str, material: str, weight: float, blade_type: str, length: float, is_corded: bool):
        super().__init__(name, material, weight)
        self.blade_type = blade_type
        self.length = length
        self.is_corded = is_corded
        self.available_blades = ["Wood", "Metal", "Plastic", "Ceramic"] 

    def use(self) -> None:
        if not self.check_durability():
            print("The saw is too damaged to use. Please repair it.")
            return

        while True:
            clear_screen()
            print(f"Using the {self.name} with {self.blade_type} blade...")
            print("\nSaw Use Menu")
            print("=============")
            print("1. Cut Wood")
            print("2. Replace Blade")
            print("3. Back")

            choice = input("\nEnter your choice (1-3): ")

            if choice == "1":
                self.cut_wood()
            elif choice == "2":
                self.replace_blade()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please select a number from 1 to 3.")
                input("\nPress Enter to return to the menu...")

    def cut_wood(self) -> None:
        if not self.check_durability():
            print("The saw is too damaged to cut. Please repair it.")
            return

        
        cut_time = random.randint(3, 6)  
        print(f"Cutting wood with the {self.blade_type} blade...")

        for i in range(cut_time, 0, -1):
            print(f"Cutting... {i} seconds remaining with {self.blade_type} blade.")
            time.sleep(1)

        print(f"Wood cut using the {self.blade_type} blade!\n")
        input("Press Enter to continue...")  
        self.degrade()

    def replace_blade(self) -> None:
        print("Available blades:")
        for idx, blade in enumerate(self.available_blades, start=1):
            print(f"{idx}. {blade} Blade")

        choice = input("Select a blade (number): ")
        if choice.isdigit() and 1 <= int(choice) <= len(self.available_blades):
            self.blade_type = self.available_blades[int(choice) - 1]
            print(f"Blade changed to {self.blade_type} Blade.")
        else:
            print("Invalid selection.")

        input("Press Enter to continue...")

    def repair(self) -> None:
        self.durability = 100
        print(f"Repaired the {self.name} saw. Durability is now full.")







"""Screwdriver Class"""
class Screwdriver(Tool):
    def __init__(self, name: str, material: str, weight: float, tip_type: str, length: float, is_magnetized: bool):
        super().__init__(name, material, weight)
        self.tip_type = tip_type
        self.length = length
        self.is_magnetized = is_magnetized
        self.available_tips = ["Flathead", "Phillips", "Torx", "Hex", "Square"]

    def use(self) -> None:
        if not self.check_durability():
            print("The screwdriver is too damaged to use. Please repair it.")
            return

        while True:
            clear_screen()
            print(f"Using the {self.weight}kg {self.name} with {self.tip_type} tip...")
            print("\nScrewdriver Use Menu")
            print("====================")
            print("1. Tighten/Loosen Screw")
            print("2. Change Tip")
            print("3. Magnetize/Unmagnetize")
            print("4. Back")

            choice = input("\nEnter your choice (1-4): ")

            if choice == "1":
                self.tighten_loosen()
            elif choice == "2":
                self.change_tip()
            elif choice == "3":
                self.toggle_magnetization()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please select a number from 1 to 4.")
                input("\nPress Enter to return to the menu...")

    def tighten_loosen(self) -> None:
        if not self.check_durability():
            print("The screwdriver is too damaged to use. Please repair it.")
            return

        print(f"Tightening/Loosening with the {self.tip_type} tip...")
        for i in range(5, 0, -1):
            print(f"Tightening/Loosening... {i} seconds remaining with {self.tip_type} tip.")
            time.sleep(1)

        print(f"Action completed using the {self.tip_type} tip!\n")
        input("Press Enter to continue...")
        self.degrade()

    def change_tip(self) -> None:
        print("Available tips:")
        for idx, tip in enumerate(self.available_tips, start=1):
            print(f"{idx}. {tip} Tip")

        choice = input("Select a tip (number): ")
        if choice.isdigit() and 1 <= int(choice) <= len(self.available_tips):
            self.tip_type = self.available_tips[int(choice) - 1]
            print(f"Tip changed to {self.tip_type} Tip.")
        else:
            print("Invalid selection.")

        input("Press Enter to continue...")

    def toggle_magnetization(self) -> None:
        self.is_magnetized = not self.is_magnetized
        state = "Magnetized" if self.is_magnetized else "Unmagnetized"
        print(f"The screwdriver is now {state}.")
        input("Press Enter to continue...")

    def repair(self) -> None:
        self.durability = 100
        print(f"Repaired the {self.name} screwdriver. Durability is now full.")







"""Measuring Tape Class"""
class MeasuringTape(Tool):
    def __init__(self, name: str, material: str, weight: float, length: float):
        super().__init__(name, material, weight)
        self.length = length
        self.current_length = 0  

    def use(self) -> None:
        if not self.check_durability():
            print("The measuring tape is too damaged to use. Please repair it.")
            return

        while True:
            clear_screen()
            print(f"Using the {self.name} made of {self.material}, weighing {self.weight}kg, with a {self.length}m length.")
            print("\nMeasuring Tape Use Menu")
            print("========================")
            print("1. Measure Wood Length")
            print("2. Mark Intervals")
            print("3. Back")

            choice = input("\nEnter your choice (1-3): ")

            if choice == "1":
                self.measure_wood_length()
            elif choice == "2":
                self.mark_intervals()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please select a number from 1 to 3.")
                input("\nPress Enter to return to the menu...")

    def measure_wood_length(self) -> None:
        if not self.check_durability():
            print("The measuring tape is too damaged to measure. Please repair it.")
            return

        wood_length = random.uniform(1, self.length)  
        print(f"Measuring wood... The length is {wood_length:.2f} meters.")
        input("Press Enter to continue...")
        self.degrade()

    def mark_intervals(self) -> None:
        if not self.check_durability():
            print("The measuring tape is too damaged to mark intervals. Please repair it.")
            return

        interval = float(input("Enter the interval length to mark (in meters): "))
        if 0 < interval <= self.length:
            print(f"Marking intervals every {interval} meters.")
            for i in range(1, int(self.length // interval) + 1):
                print(f"Mark {i}: {i * interval} meters")
            print("Intervals marked.")
        else:
            print("Invalid interval length. Please enter a value within the tape's length.")

        input("Press Enter to continue...")
        self.degrade()

    def repair(self) -> None:
        self.durability = 100
        print(f"Repaired the {self.name} measuring tape. Durability is now full.")
        
"""Wrench Class"""
class Wrench(Tool):
    def __init__(self, name: str, material: str, weight: float, size: float, is_ratcheting: bool):
        super().__init__(name, material, weight)
        self.size = size  
        self.is_ratcheting = is_ratcheting
        self.available_sizes = [8, 10, 12, 14, 17, 19, 22, 24]

    def use(self) -> None:
        if not self.check_durability():
            print("The wrench is too damaged to use. Please repair it.")
            return

        while True:
            clear_screen()
            print(f"Using the {self.name} ({self.size}mm), Material: {self.material}, Weight: {self.weight}kg")
            print("\nWrench Use Menu")
            print("==================")
            print("1. Tighten Bolt")
            print("2. Loosen Bolt")
            print("3. Change Size")
            print("4. Toggle Ratcheting Mode")
            print("5. Back")

            choice = input("\nEnter your choice (1-5): ")

            if choice == "1":
                self.tighten_bolt()
            elif choice == "2":
                self.loosen_bolt()
            elif choice == "3":
                self.change_size()
            elif choice == "4":
                self.toggle_ratcheting()
            elif choice == "5":
                break
            else:
                print("Invalid choice.")
                input("Press Enter to continue...")

    def tighten_bolt(self) -> None:
        print(f"Tightening a bolt with a {self.size}mm wrench.")
        time.sleep(2)
        print("Bolt tightened.")
        self.degrade()
        input("Press Enter to continue...")

    def loosen_bolt(self) -> None:
        print(f"Loosening a bolt with a {self.size}mm wrench.")
        time.sleep(2)
        print("Bolt loosened.")
        self.degrade()
        input("Press Enter to continue...")

    def change_size(self) -> None:
        print("Available sizes:")
        for idx, s in enumerate(self.available_sizes, start=1):
            print(f"{idx}. {s}mm")

        choice = input("Select a size (number): ")
        if choice.isdigit() and 1 <= int(choice) <= len(self.available_sizes):
            self.size = self.available_sizes[int(choice) - 1]
            print(f"Wrench size changed to {self.size}mm.")
        else:
            print("Invalid selection.")

        input("Press Enter to continue...")

    def toggle_ratcheting(self) -> None:
        self.is_ratcheting = not self.is_ratcheting
        mode = "Ratcheting" if self.is_ratcheting else "Non-Ratcheting"
        print(f"The wrench is now set to {mode} mode.")
        input("Press Enter to continue...")

    def repair(self) -> None:
        self.durability = 100
        print(f"Repaired the {self.name} wrench. Durability is now full.")

 


"""Main menu"""
def tool_menu(tool: Tool):
    while True:
        clear_screen()
        print(f"{tool.name} Menu")
        print("================")
        print("1. Use")
        print("2. Repair")
        print("3. Back")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            tool.use()
        elif choice == "2":
            tool.repair()
            input("Press Enter to continue...")
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    hammer = Hammer("Hammer", "Iron", 2.5, "Flat", "Curved", 16)
    drill = Drill("Drill", "Steel", 1.5, 500.0, True, 1500)
    saw = Saw("Saw", "Steel", 3.0, "Wood", 18, True)  
    screwdriver = Screwdriver("Screwdriver", "Steel", 0.3, "Phillips", 6, False)
    measuring_tape = MeasuringTape("Measuring Tape", "Plastic", 0.5, 25)  
    wrench = Wrench("Wrench", "Chrome-Vanadium", 0.8, 17, True)


    tools = {
        "1": hammer,
        "2": drill,
        "3": saw,
        "4": screwdriver, 
        "5": measuring_tape,
        "6": wrench 
    }

    while True:
        clear_screen()
        print("Toolbox")
        print("=======")
        for key, tool in tools.items():
            print(f"{key}. {tool.name} (Durability: {tool.durability}%)")
        print("0. Exit")

        choice = input("\nSelect a tool to manage: ")

        if choice in tools:
            tool_menu(tools[choice])
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")
            input("Press Enter to try again...")
