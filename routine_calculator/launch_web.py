import sys
import os
from streamlit.web import cli as stcli

def main():
    # Get the path to the web.py file within the package
    package_dir = os.path.dirname(os.path.abspath(__file__))
    web_app_path = os.path.join(package_dir, 'web.py')
    
    # Construct the arguments for streamlit
    sys.argv = ["streamlit", "run", web_app_path]
    
    # Run streamlit
    sys.exit(stcli.main())

if __name__ == "__main__":
    main()
