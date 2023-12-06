from django.conf import settings


def create_signs(fio=None, role=None, tel_1=None, tel_2=None, sign=None) -> str:
    file_sign = {
        "new": str(settings.BASE_DIR) + "/static/files/example_1.html",
        "old": str(settings.BASE_DIR) + "/static/files/example_2.html",
    }
    if tel_1 is not None:
        tel_1 = str(tel_1)
        tel_1 = "Тел. +375 " + f"({tel_1[:2]})" + " " + tel_1[2:5] + "-" + tel_1[5:7] + "-" + tel_1[7:9]

    if tel_2 is not None:
        tel_2 = str(tel_2)
        tel_2 = "Тел. +375 " + f"({tel_2[:2]})" + " " + tel_2[2:5] + "-" + tel_2[5:7] + "-" + tel_2[7:9]

    with open(file=file_sign.get(sign),
              mode="r",
              encoding="utf-8") as f:

        data = f.readlines()
        sign = ""
        for line in data:
            if 'fio' in line:
                if fio is None:
                    continue
                line = line.replace("fio", f"{fio}")
            if 'role' in line:
                if role is None:
                    continue
                line = line.replace("role", f"{role}")
            if 'tel_1' in line:
                if tel_1 is None:
                    continue
                line = line.replace("tel_1", f"{tel_1}")
            if 'tel_2' in line:
                if tel_2 is None:
                    continue
                line = line.replace("tel_2", f"{tel_2}")
            sign += line

        return sign
