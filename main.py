import re
import json
import datetime


def parse_txt(input_file, output_file):
    pattern = re.compile(
        r"(^(\d{4}/\d{1,2}/\d{1,2}).*?)?((\d{2}:\d{2})\t(.*?)\t(.*?))(?=\n\d{2}:\d{2}|$)",
        re.S | re.M,
    )
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()
    matches = pattern.findall(content)

    result = []
    date = None  # Initialize date
    for match in matches:
        if match[1]:  # 如果日期存在
            date = match[1]
        # Check if message does not contain another date
        if match[3]:
            time_string = match[3]
            time_obj = datetime.datetime.strptime(time_string, "%H:%M")
            naive_datetime = datetime.datetime.strptime(date, "%Y/%m/%d")
            aware_datetime = naive_datetime.replace(
                hour=time_obj.hour,
                minute=time_obj.minute,
                tzinfo=datetime.timezone(
                    datetime.timedelta(hours=8)
                ),  # Convert to GMT+8
            )
            unixtime = int(aware_datetime.timestamp())
            result.append(
                {
                    "date": date if date else "None",  # Add date
                    "time": time_string,  # Add time
                    "from": match[4],
                    "text": match[5],
                    "date_unixtime": str(unixtime) if unixtime else "None",
                }
            )

    with open(output_file, "w", encoding="utf-8") as jsonf:
        json.dump(result, jsonf, ensure_ascii=False)


if __name__ == "__main__":
    # Call the function with your text file
    parse_txt(input_file="", output_file="")
