import mistletoe
import os

with open("output/index.html", "x") as out:
    for file in os.listdir("reports"):
        with open(f"reports/{file}") as f:
            out.write(mistletoe.markdown(f))
        out.write("<br>\n<hr>\n<br>\n")
