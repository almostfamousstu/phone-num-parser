class PhoneNumberParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.phone_numbers = {}

    def parse_phone_numbers(self):
        """Parses phone numbers from a given file and stores them in a dictionary."""
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    # Clean inputs/convert keypad equivalents
                    parts = line.strip().replace(" ", "").replace("(", "").replace(")", "-").replace("A", "2").replace("B", "2").replace("C", "2").replace("D", "3").replace("E", "3").replace("F", "3").replace("G", "4").replace("H", "4").replace("I", "4").replace("J", "5").replace("K", "5").replace("L", "5").replace("M", "6").replace("N", "6").replace("O", "6").replace("P", "7").replace("Q", "7").replace("R", "7").replace("S", "7").replace("T", "8").replace("U", "8").replace("V", "8").replace("W", "9").replace("X", "9").replace("Y", "9").replace("Z", "9").split("-")
                    if len(parts) == 3:  
                        # Create nested dictionary
                        temp_dict = dict(zip(['area_code', 'central_office_code', 'exchange'], parts))
                        self.phone_numbers[line.strip()] = temp_dict
        except FileNotFoundError:
            print(f"Error: The file {self.file_path} does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_phone_numbers(self):
        """Returns the parsed phone numbers."""
        return self.phone_numbers
    

def main():
    parser = PhoneNumberParser('C:/Users/fun/phonenumbers.txt')
    parser.parse_phone_numbers()
    parsed_numbers = parser.get_phone_numbers()
    for number, details in parsed_numbers.items():
        print(f"{number}: {details}") 

if __name__ == '__main__':
    main()