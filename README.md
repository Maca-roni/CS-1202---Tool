# Laboratory Activity 3 & 4 - CS-1202 - Tool
This program simulates a virtual toolbox where the user can manage various tool. Each tool has specific features, such as durability, and the ability to be used, repaired, or modified. 

🛠️ Toolmaster: Workshop Simulator

Toolmaster: Workshop Simulator is a console-based application designed to demonstrate key Object-Oriented Programming (OOP) principles using a collection of virtual tools. This interactive program allows users to manage and utilize various tools, each with unique functionalities and realistic durability mechanics in a simulated workshop environment.

👥 Development Team:

    Dereck Dimaano (Dereck-1123)

    Franz Villanueva (FrnzV)

    Rocklyn Mary Lopez (rocks294)

    Ron Emmanuel Guial (Maca_roni)

                                                                   

❓ What is Toolmaster?

Toolmaster serves as a comprehensive workshop simulator where users can explore the use and maintenance of different tools. The program emphasizes OOP concepts, offering functionalities such as using tools, replacing components, and repairing worn-out equipment.

🔧 Core Features:

    - Interactive Workshop Menu: Navigate through various tools and select actions like using, repairing, or inspecting tools.
    - Realistic Durability Mechanics: Tools degrade with each use, requiring repairs to restore them to peak condition.
    - Customizable Components: Swap out saw blades or drill bits to adapt tools for specific tasks.

🛠️ Available Tools and Their Functions:

    - Hammer: Strike and remove nails, with each strike randomly affecting nail depth.
    - Drill: Drill holes at variable speeds, change drill bits for different materials.
    - Saw: Cut through wood using different blade types, each suited for specific materials.
    - Measuring Tape: Measure wood lengths and mark intervals at user-defined distances.
    - Wrench: Tighten or loosen bolts with adjustable sizes; includes torque control.
    - Screwdriver: Tighten or loosen screws, change tip types (Flathead, Phillips, Torx), and toggle magnetization.


📦 Key OOP Concepts Implemented:

    - Inheritance: The Tool superclass defines core attributes and methods, extended by each tool type.
    - Polymorphism: Each tool type implements its own use() method, showcasing different behaviors.
    - Encapsulation: Tool attributes are managed internally, with controlled access through methods.
    - Abstraction: Essential tool behaviors are defined as abstract methods, ensuring consistency across tools.

Class Diagram:

![UML](https://github.com/Maca-roni/CS-1202---Tool/blob/68fbff446cc0608be836707d0a485e1129007449/UML.png)

▶️ How to Get Started:

Clone or download the repository.

Open the project folder in your preferred Python environment.

Run the main program file:

    Tool.py

Follow the on-screen instructions to navigate through the tool menu, use tools, and manage their durability.

🌟 Acknowledgements:

We extend our deepest gratitude to our instructor and mentors for their guidance and support throughout this project. Special thanks to everyone who contributed to the development and testing of Toolmaster: Workshop Simulator.
