patient_name = input("Nhập họ tên bệnh nhân")
patient_age = int(input("Nhập tuổi bệnh nhân"))
spo2_level = int(input("Nhập nồng độ oxy trong máu"))
heart_rate = int(input("Nhập nhịp tim"))
has_insurance = input("Có thẻ bhyt không??") #yes no


if spo2_level < 90 or heart_rate > 120:
    status = "Báo động : ĐỎ"
elif (90 <= spo2_level <= 95) or (100 <= heart_rate <= 120):
    status = "Báo động : VÀNG"
else:
    status = "Khám thường : Xanh"


price = 500_000

if patient_age < 6 or patient_age > 80:
    total_price = 0
elif has_insurance == "yes":
    total_price = price * 0.5
else:
    total_price = price
    


print(f"""
    ------- Phiếu khám điện tử ------------
    Tên : {patient_name}
    Tuổi : {patient_age}
    Nồng độ oxy {spo2_level}
    Nhịp tim {heart_rate}
    Trạng thái : {status}
    Có bảo hiểm y tế : {has_insurance}
    Phí phải trả : {total_price} """
)

