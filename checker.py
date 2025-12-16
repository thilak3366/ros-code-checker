import zipfile, os, subprocess, json, re

def check(zip_path):
    os.makedirs("tmp", exist_ok=True)
    zipfile.ZipFile(zip_path).extractall("tmp")

    report = {
        "syntax": "pass",
        "structure": "pass",
        "ros": {},
        "warnings": []
    }

    if "package.xml" not in os.listdir("tmp"):
        report["structure"] = "fail"

    for root,_,files in os.walk("tmp"):
        for f in files:
            if f.endswith(".py"):
                path = os.path.join(root,f)

                if subprocess.run(
                    ["python3","-m","py_compile",path],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                ).returncode != 0:
                    report["syntax"] = "fail"

                code = open(path).read()
                report["ros"]["init"] = "rclpy.init" in code
                report["ros"]["publisher"] = "create_publisher" in code
                report["ros"]["subscriber"] = "create_subscription" in code

                if "while True" in code and "sleep" not in code:
                    report["warnings"].append(
                        "Infinite loop without sleep detected"
                    )

    json.dump(report, open("report.json","w"), indent=2)
    open("report.txt","w").write(str(report))
    return report

if __name__=="__main__":
    check("uploaded.zip")
