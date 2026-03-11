import math
def tinh_dien_truong(q, r):
    # Hằng số epsilon_0
    eps_0 = 8.854e-12
    
    # Công thức rút ra từ định luật Gauss cho hình cầu
    e = q / (4 * math.pi * eps_0 * r**2)
    return e

# Nhập dữ liệu
dien_tich = float(input("Nhập điện tích Q (Coulomb): "))
khoang_cach = float(input("Nhập khoảng cách r (m): "))

# Tính và in kết quả
ket_qua = tinh_dien_truong(dien_tich, khoang_cach)
print(f"Cường độ điện trường tại r = {khoang_cach}m là: {ket_qua:.2g} V/m")


