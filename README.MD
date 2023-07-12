# LINE2JSON

LINE2JSON is a Python utility that helps in converting LINE chat logs from a text format into a more convenient and structured JSON format. Moreover, it also facilitates conversion of timestamps into Unix format for easier computation and comparison in different programming languages.

## Features

1. Converts LINE chat logs from .txt format to structured JSON format.
2. Handles chat dates and times, and converts them into Unix timestamps.

## How to Use

The utility is contained in a single Python script which can be used by calling the `parse_txt` function and passing the path to your LINE chat log text file. 

```python
from line2json import parse_txt

# Call the function with your text file
parse_txt("/path/to/your/LINEchatlog.txt")
```
This will generate a JSON file named "result.json" in the same directory as your script. The JSON file contains your chat logs in a structured format.

## JSON Format
Each message in the chat log is represented as a JSON object with the following properties:

"date": The date the message was sent.
"time": The time the message was sent.
"from": The sender of the message.
"text": The message text.
"date_unixtime": The date and time the message was sent, represented as a Unix timestamp.

For example:

```json
{
  "date": "2020/7/28",
  "time": "14:18",
  "from": "John Doe",
  "text": "Hello, World!",
  "date_unixtime": "1595927880"
}
```

## Notes
This utility assumes that the chat logs are in a specific format as provided by LINE's chat log export feature as of 2023. If LINE changes their export format or if you have chat logs in a different format, you may need to adjust the regular expression pattern used by this utility.

Please replace /path/to/your/LINEchatlog.txt in the "How to Use" section with an actual path according to your preference or leave it as is if you want to provide a generic example. The same applies to other placeholder values used in the README.