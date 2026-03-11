# nhập chiều cao và cân nặng của người dùng
weight = float(input("Nhập cân nặng (kg): "))
height = float(input("Nhập chiều cao (m): "))            
# tính chỉ số BMI
bmi = weight / (height ** 2)
# in kết quả
print(f"Chỉ số BMI của bạn là: {bmi:.2f}")     
if bmi < 18.5:
    print("Bạn bị thiếu cân.")
elif 18.5 <= bmi < 25:
    print("Bạn có cân nặng bình thường.")
elif 25 <= bmi < 30:
    print("Bạn bị thừa cân.")
else:
    print("Bạn bị béo phì.")    