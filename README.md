# PySimpleSniffer

PySimpleSniffer is a simple and easy-to-use network sniffer written in Python using the `scapy` library. It allows you to listen on a specified port on a selected network interface and print captured packets to the screen or save them to a file.

## Features

- Capture network packets on a specified port.
- Print captured packets to the console.
- Save captured packets to a file.

## Installation

1. Install the required library:

```bash
pip install scapy
```

2. Clone this repository or download the `main.py` file.

## Usage

Run the sniffer with the following command:

```bash
sudo python main.py <interface> <port> <output_file>
```

- `<interface>`: The name of the network interface (e.g., `eth0`).
- `<port>`: The port you want to listen on (e.g., `80` for HTTP).
- `<output_file>`: The name of the file where captured packets will be saved.

Example:

```bash
sudo python main.py eth0 80 output.txt
```

## Disclaimer and Terms of Use

By using PyPacketSniffer, you agree to the following terms:

1. **Use at Your Own Risk**: PySimpleSniffer is provided "as is" without any warranties or guarantees of any kind. The user assumes full responsibility for any direct or indirect damages arising from the use of this tool.

2. **Legal Compliance**: It is your responsibility to ensure that your use of PySimpleSniffer complies with all applicable laws and regulations. Unauthorized use of this tool to capture network traffic may be illegal in your jurisdiction. Always obtain proper authorization before capturing network traffic.

3. **No Liability**: The developers and contributors of PySimpleSniffer are not liable for any misuse, damage, or legal consequences resulting from the use of this tool. Use this tool responsibly and ethically.

## License

This project is licensed under the GPL-3.0 License. See the LICENSE file for more details.

## Contribution

Contributions are welcome! Please fork this repository and submit pull requests for any improvements or bug fixes.

## Contact

If you have any questions or suggestions, feel free to open an issue in this repository.

---

**Note**: This tool is intended for educational purposes and authorized network monitoring only.
