
def create_signs(fio=None, role=None, tel_1=None, tel_2=None, file=None) -> str:
    with open(file=file,
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

        # with open("my_sign_new.html", mode="w", encoding="utf-8") as file:
        #     file.write(sign)
# def create_old_sign(fio=None, role=None, tel_1=None, tel_2=None) -> None:
#     with open("_old_signature_example.html",
#               mode="r",
#               encoding="utf-8") as f:
#
#         data = f.readlines()
#         sign = ""
#         for line in data:
#             if 'fio' in line:
#                 if fio is None:
#                     continue
#                 line = line.replace("fio", f"{fio}")
#             if 'role' in line:
#                 if role is None:
#                     continue
#                 line = line.replace("role", f"{role}")
#             if 'tel_1' in line:
#                 if tel_1 is None:
#                     continue
#                 line = line.replace("tel_1", f"{tel_1}")
#             if 'tel_2' in line:
#                 if tel_2 is None:
#                     continue
#                 line = line.replace("tel_2", f"{tel_2}")
#             sign += line
#
#         with open("my_sign_old.html", mode="w", encoding="utf-8") as file:
#             file.write(sign)
