A customizable QR code generator developed based on Python that supports both command line and graphical interface modes. This project is the final project of the software engineering program COMP2116 Macao Polytechnic University.

Group name :Dream team

members : P2321041 Jorven 
          
          P2322403 Vito 	
          
          P2320462 Brian 	

Software image input and output display
<img width="864" alt="8160e468db1f7bdac22230a6b183210" src="https://github.com/user-attachments/assets/3f64f9a8-da21-4197-9d2e-79385be0e3bd" />
<img width="1023" alt="149ec74c5fd84ce0aa58ad5a9ffd8df" src="https://github.com/user-attachments/assets/740fd8cd-006e-4d1e-9cb8-564a0ef96513" />

Software development process adopted: Agile development

Choosing agile development over a waterfall model:
    
    More flexible to adapt to changes in requirements, and requirements may be adjusted (such as adding new GUI functions).
    
    Iteratively deliver available versions, with limited course time, so you can produce demonstrable versions more quickly.
    
    For the testing phase, continuous integration and testing, and unit tests to ensure code quality.
    
    In terms of team collaboration, the daily progress is synchronized, which is suitable for teams of 3-4 people to work efficiently.

Agile practices are concrete
    
    Sprint cycle: 2 weekly iterations
    
    Task Kanban: Manage with GitHub Projects (To Do/In Progress/Done)
    
    Daily stand-up meeting: 15 minutes to synchronize progress (offline or Discord)

Software Uses and Target Markets
  
  Core application scenarios
    
    Individual users: Quickly generate QR codes such as contact information, Wi-Fi passwords, etc
    
    Enterprise Scenario: Marketing Campaign (Customized QR Code with Logo)
    
    Developers: Provide CLI tools to integrate into automated processes

Software Development Program

Development Process:

Week 1 Basic function implementation: Complete the underlying code implementation of the QR code generation function.
  
  Key Tasks:
    
    Research and integrate with mainstream QR code generation libraries (e.g., QR code, pyQRCODE).
    
    Implement the core function: support input text/URL to generate a standard QR code image (PNG/SVG format).
    
    Basic parameter configuration: size, error correction level, color, etc.
    
    Output Validation: Ensure that the generated QR code is recognizable by a universal barcode scanning tool.

Week 2 Function Expansion and Systematization: Improve basic functions, add decoding and analysis modules, and improve code maintainability.
  
  Key Tasks:
    
    Function expansion: Integrate QR code decoding functions (such as OpenCV, Pyzbar) to support data analysis from images.
                        
                        Add an analysis module: Collect metadata such as QR code pixel distribution, version information, and fault tolerance.
    
    Code optimization: Modular refactoring: Separate the generation, decoding, and analysis logic to reduce the coupling degree.
                       
                       Exception handling: Robust designs such as input validation and file read/write error capture are added.
    
    Preliminary GUI framework: Design a prototype of a Tkinter/PyQt interface and define the interaction logic.

Week 3 Testing & Delivery: Ensure functional stability through systematic testing and close the project loop.
  
  Key Tasks:
    
    Test coverage:  Unit Tests: Verify the functionality of each module (e.g., generate/decode boundary condition tests).
                    
                    Integration testing: Simulate user flows (generation→ saving→ decoding → analysis).
                    
                    Compatibility testing: cross-platform (Windows/macOS/Linux) and different resolution verification.
    
    GUI Improvement:
                    Implement a complete user interface and integrate all functional modules.
                    
                    Optimize the interactive experience (such as progress prompts, error pop-ups).
    
    Documentation & Delivery:
                    
                    Write user manuals (API instructions, GUI how-to guides).
                    
                    Output a test report to confirm that the acceptance criteria are met.

Existing software features: 1. Generate QR codes
                            
                            2. Decode the QR code
                            
                            3. Analyze the QR code
                            
                            4. Launch the GUI interface
                            
                            5. Exit

Future Plans   Functions to be developed: Batch generation (CSV import) , Dynamic QR code (URL tracking) , Optimize the GUI user experience.

Division of labor: P2321041 Jorven   1.Generate QR code 2.Decode QR code 5.Exit
                   
                   P2322403 Vito     3. Analyze the QR code and readme writing
                   
                   P2320462 Brian    4.Launch the GUI interface and Video Debriefing

Domo (Youtube url）

Core algorithms
python

1. Data encoding → 2. Reed-Solomon → 3. Module Arrangement → 4. Render the image

Operating environment requirements

Programming language         Python 3.8+

Operating                    system Windows/macOS/Linux

Hardware requirements        1GB RAM, 100MB disk space

Dependency libraries         qrcode, pillow, pyzbar

Open Source Statement: Third-party libraries used
                       
                       qrcode (MIT License)
                       Pillow (HPND License)
                       pyzbar (MIT License)
