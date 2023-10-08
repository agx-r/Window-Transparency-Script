# Window Transparency Script

This Python script allows you to set the transparency of all top-level windows on your Windows operating system. It uses the `win32gui` library to interact with window properties and applies a specified level of transparency to each visible window.

## Features

- Adjust the transparency of windows with a customizable transparency value.
- Continuously monitor and apply transparency to new windows as they are created.
- Easily configurable with customizable constants.

## Prerequisites

Before running this script, ensure that you have the following prerequisites installed:

- Python 3.x
- Required Python packages:
  - `pywin32` (for `win32gui` interactions)
  - `time` (for timing operations)

You can install the necessary packages using pip:

```bash
pip install pywin32
```

## Usage

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt.

3. Navigate to the directory containing the script.

4. Run the script:

```bash
python window_transparency.py
```

5. The script will continuously monitor and apply transparency to both existing and new top-level windows.

6. To stop the script, press `Ctrl+C` in the terminal.

## Customization

You can customize the script by modifying the following constants in the script:

- `TRANSPARENCY_ALPHA`: Adjust the transparency level by setting a value between 0 and 1. A higher value means less transparency.
- `TRANSPARENCY_INTERVAL`: Set the time interval (in seconds) between transparency updates. Adjust this value based on your preference.

## Troubleshooting

If you encounter any issues while running the script, ensure that you have the required packages installed and that you are running the script with the appropriate permissions.

## License

This script is open-source and available under the [MIT License](LICENSE).

## Author

- [AGX]
- GitHub: [AGX](https://github.com/agx-r)

Feel free to contribute to or modify this script as needed. If you have any questions or encounter any issues, please create an issue in the GitHub repository.
