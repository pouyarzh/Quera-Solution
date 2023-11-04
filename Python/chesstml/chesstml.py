from bs4 import BeautifulSoup as bs
import os

def process(path):
    # Open the HTML file
    html = open(path, "r")

    # Parse HTML file in Beautiful Soup
    soup = bs(html, 'html.parser')

    # Print a certain line
    print("Number of paragraph tags:")

    # Calculating and printing the
    # number of paragraph tags
    return len(soup.find_all("a"))



# Change the directory and read all of the files from path
def change_directory(path):
    os.chdir(path)

    # Read text File
    def read_text_file(path):
        with open(path, 'r') as f:
            print(f.read())

    # iterate through all file
    for file in os.listdir():
        # Check whether file is in text format or not
        if file.endswith(".html"):
            file_path = f"{path}\{file}"

            # call read text file function
            read_text_file(file_path)


if __name__ == "__main__":
    process('/MainPythonProject/QueraProblemSet/QueraStartDate/chesstml/test/.pytest_cache/htmlsampletest2.html')