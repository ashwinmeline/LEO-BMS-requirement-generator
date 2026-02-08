# LEO-BMS-requirement-generator

I chose Python because it allows for rapid iteration and is easily integrated into larger constellation-scale simulation pipelines.

Data Structures (Nested Dictionaries & JSON): * I represent requirements as nested dictionaries to maintain a clear hierarchy (e.g., separating "Operational Limits" from "Sensing Accuracy").

I selected JSON for the output format because it is machine-readable and interoperable. In a modern Model-Based Systems Engineering (MBSE) workflow, these JSON snippets can be automatically ingested by hardware configuration tools or thermal simulators, eliminating the human error associated with manual data entry.

Formalizing Requirements: 
Translated orbital stress factors into specific BMS hardware constraints:

1. State of Charge (SOC) Logic: Drawing from the suggested NASA (MSC-TOPS-40) reading, I implemented a restricted 40-70% SOC window for long-lived missions.
LEO satellites experience ~15 cycles per day. Staying away from the "knees" of the voltage curve is the most effective way a BMS can proactively mitigate the chemical degradation and SEI layer growth I studied in my previous SoH (State of Health) project.

2. Hardware Selection Logic: The generator automatically recommends an Active Balancing strategy if the calculated eclipse C-rate exceeds 0.5C.
Based on Aerospace Corp findings, high-power discharge events create significant thermal gradients across a pack. Active balancing is required to prevent cell divergence without generating the excess waste heat typical of passive resistor-based balancing.

Future Extensions

Radiation-Induced Redundancy: Automatically scaling the BMS architecture (e.g., Triple Modular Redundancy) based on the target altitude's radiation profile.

Communication Protocol Mapping: Linking the current_precision requirements to specific bus types (CAN vs. SpaceWire) based on the sampling frequency needed to track high-power transients(sudden spikes in power). 

"My current threshold in templates.py is set to 0.5C. Even in the low-power case, the narrow SOC window means we have a smaller total capacity, which keeps the C-rate relatively high. For a full thesis, I would refine this threshold by linking it to a thermal model."
