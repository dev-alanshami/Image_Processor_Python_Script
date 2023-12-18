# This Program is a wrapper for the image processing program (PHOTO) written in MATLAB, C, Haskell, and Prolog.
# It runs the MATLAB scripts and C, Haskell, and Prolog programs in the correct order.
# It also checks for the requirements of the programs and exits if any of them are not met.
# It also checks for the existence of the image file and exits if it does not exist.
# It prints colored output of the programs to the terminal.
# It has a validation for the input image and also for the requirements of the programs.
    

# Necessary imports
import subprocess
import os
import shutil
import time

# Program Logo
logo = '''
            _           _        
           | |         | |       
        _ __ | |__   ___ | |_ ___  
       | '_ \\| '_ \\ / _ \\| __/ _ \\ 
       | |_) | | | | (_) | || (_) |
       | .__/|_| |_|\\___/ \\__\\___/ 
       | |                         
       |_|                 
'''

# Colors for the terminal
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'

# Function to check if an executable exists
# AI generated code - GPT-3
def check_executable_exists(executable_name, task_description):
    if shutil.which(executable_name) is None:
        print(f"{Colors.RED}{task_description} is not installed or not in the system PATH. Please install it and try again.{Colors.RESET}")
        return False
    return True

# Function to run a MATLAB script
def run_matlab_script(executable, script_name, task_description, action_past_tense, wait_for_completion=True):
    # checks for its own requirements, for resuability
    if not os.path.isfile(executable):
        print(f"{Colors.RED}MATLAB is not correctly installed or the path is incorrect. Please check.{Colors.RESET}")
        return False
    try:
        print(f"{Colors.BLUE}- MATLAB is {task_description}...{Colors.RESET}", end="\n")
        if wait_for_completion:
            subprocess.run([executable, "-batch", f"run('{script_name}');"], check=True)
            print(f"{Colors.GREEN}MATLAB has successfully {action_past_tense}.{Colors.RESET}\n")
            return True
        else:
            process = subprocess.Popen([executable, "-batch", f"run('{script_name}');"])
            print(f"{Colors.GREEN}MATLAB has started {task_description}.{Colors.RESET}\n")
            return process
    except subprocess.CalledProcessError:
        print(f"{Colors.RED}There was a problem while {task_description} in MATLAB.{Colors.RESET}")
        return False

def compile_and_run_c_program(source_file, output_file, input_file, task_description, action_past_tense):

    # checks for its own requirements, for resuability
    if not os.path.isfile(source_file):
        print(f"{Colors.RED}The C program source file is missing. Please check the file.{Colors.RESET}")
        return False
    try:
        print(f"{Colors.BLUE}- The C program is {task_description}...{Colors.RESET}", end="\n")
        subprocess.run(["gcc", source_file, "-o", output_file], check=True)
        if not os.path.isfile(input_file):
            print(f"\n{Colors.RED}Input file for the C program is missing.{Colors.RESET}")
            return False
        with open(input_file, 'r') as file:
            file_content = file.readline().split()
        with open("c_output.txt", "w") as out:
            subprocess.run([f"./{output_file}"] + file_content, check=True, stdout=out)
            out.flush()
        print(f"{Colors.GREEN}C program has successfully {action_past_tense}.{Colors.RESET}\n")
        return True
    except subprocess.CalledProcessError:
        print(f"{Colors.RED}There was an error while {task_description} in the C program.{Colors.RESET}")
        return False

def compile_and_run_haskell_program(source_file, input_file, task_description, action_past_tense):
        
    # checks for its own requirements, for resuability
    if not os.path.isfile(source_file):
        print(f"{Colors.RED}The Haskell source file cannot be found.{Colors.RESET}")
        return False
    try:
        print(f"{Colors.BLUE}- The Haskell program is {task_description}...{Colors.RESET}", end="\n")
        with open(os.devnull, 'w') as devnull:
            subprocess.run(["ghc", source_file, "-o", "haskell_taks"], stdout=devnull, stderr=devnull, check=True)
        if not os.path.isfile(input_file):
            print(f"\n{Colors.RED}Input file for the Haskell program is missing.{Colors.RESET}")
            return False
        with open("haskell_output.txt", "w") as out:
            subprocess.run(["./haskell_taks", input_file], check=True, stdout=out)
            out.flush()
        print(f"{Colors.GREEN}Haskell program has successfully {action_past_tense}.{Colors.RESET}\n")
        return True
    except subprocess.CalledProcessError:
        print(f"{Colors.RED}There was an error while {task_description} in the Haskell program.{Colors.RESET}")
        return False

def run_prolog_program(input_file, task_description, action_past_tense, *args):
    if not os.path.isfile(input_file):
        print(f"{Colors.RED}Input file for the Prolog program is missing.{Colors.RESET}")
        return False
        
    print(f"{Colors.YELLOW}This next step might take a little bit longer, why don't you go grab a coffee? I'll wait..{Colors.RESET}")

    print(f"{Colors.BLUE}- The Prolog program is {task_description}...{Colors.RESET}")

    with open(input_file, 'r') as file:
        input_data = file.read()
    input_array = list(map(int, input_data.split()))
    prolog_input = "[" + ",".join(map(str, input_array)) + "]."
    try:
        result = subprocess.run(['swipl', '-q', '-g', 'main', '-t', 'halt', 'prolog_program.pl'] + list(args),
                                input=prolog_input, capture_output=True, text=True)
        output_result = result.stdout.strip().replace('[', '').replace(']', '').replace(',', ' ')
        with open('prolog_output.txt', 'w') as f:
            f.write(output_result)
        print(f"{Colors.GREEN}Prolog program has successfully {action_past_tense}.{Colors.RESET}\n")
        return True
    except subprocess.CalledProcessError:
        print(f"{Colors.RED}There was an error while {task_description} in the Prolog program.{Colors.RESET}")
        return False

# Main function
if __name__ == "__main__":
    # Logo section
    print("\n\n")
    print(logo.center(120))
    print("\n\n")

    # Welcome message
    print(f"{Colors.CYAN}Welcome to the image processing program (PHOTO).{Colors.RESET}")
    print(f"{Colors.MAGENTA}By student X in CS 420 - Fall 2023{Colors.RESET}\n")

    # Check for program requirements dictionary
    program_requirements = {
        'MATLAB': '/Applications/MATLAB_R2023b.app/bin/matlab',
        'GCC (C Compiler)': 'gcc',
        'GHC (Haskell Compiler)': 'ghc',
        'SWI-Prolog': 'swipl'
    }

    requirements_met = all([check_executable_exists(executable, task_description) for task_description, executable in program_requirements.items()])
    
    # Check if all requirements are met
    if not requirements_met:
        print(f"{Colors.RED}Some program requirements are not met. Please install the required programs and try again.{Colors.RESET}")
        exit(1)

    print(f"{Colors.GREEN}All program requirements are met (matlab, C, Haskell, Prolog). Starting image processing...{Colors.RESET}\n")
    time.sleep(3)

    image_path = input("Enter the exact path to the image, or leave empty for default image (or type 'x' to exit): ").strip().lower()

    # Exit if user types 'x'
    if image_path == 'x':
        print(f"{Colors.YELLOW}Exiting the program.{Colors.RESET}")
        exit(0)

    # Set default image if user leaves empty
    image_path = image_path if os.path.isfile(image_path) else "mickey-1.png"

    # Check if the image file exists
    if not os.path.isfile(image_path):
        print(f"{Colors.RED}No valid image file found. Please ensure the image file exists and try again.{Colors.RESET}")
        exit(1)

    # Write the image path to a file for MATLAB to read
    with open('path.txt', 'w') as file:
        file.write(image_path)

    # Run the MATLAB 1 script
    if not run_matlab_script('/Applications/MATLAB_R2023b.app/bin/matlab', 'matlab1.m', "converting the image to binary", "converted the image to binary", True):
        exit(1)
    time.sleep(5)

    # Run the C program
    if not compile_and_run_c_program("c_program.c", "c_output", "matlab1_output.txt", "reversing the image colors", "reversed the image colors"):
        exit(1)
    time.sleep(5)

    # Run the Haskell program
    if not compile_and_run_haskell_program("haskell_program.hs", "c_output.txt", "flipping the image colors", "flipped the image colors"):
        exit(1)
    time.sleep(5)

    # Run the Prolog program
    if not run_prolog_program('matlab1_output.txt', "rotating the image", "rotated the image"):
        exit(1)
    time.sleep(5)

    # Run the MATLAB 2 script
    matlab_process = run_matlab_script('/Applications/MATLAB_R2023b.app/bin/matlab', "matlab2.m", "displaying all results", "displayed all results", False)
    if matlab_process is None:
        exit(1)

    # Wait for MATLAB to finish
    print(f"{Colors.GREEN}Image processing steps completed. MATLAB is displaying the results.{Colors.RESET}")
