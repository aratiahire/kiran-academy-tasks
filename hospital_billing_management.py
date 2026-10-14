
def calculateConsultationFee(fee):
    return fee


def calculateMedicineCost(medicines):
    return medicines


def calculateRoomCharges(days, charge):
    return days * charge


def totalBill(consultation, medicines, days, roomCharge):
    consultationFee = calculateConsultationFee(consultation)
    medicineCost = calculateMedicineCost(medicines)
    roomCharges = calculateRoomCharges(days, roomCharge)

    return consultationFee + medicineCost + roomCharges


def calculateDiscountedBill(consultation, medicines, days, roomCharge):
    total = totalBill(consultation, medicines, days, roomCharge)
    discount = total * 10 / 100

    return total - discount


consultation = 500
medicines = 1500
days = 3
roomCharge = 1000

total = totalBill(consultation, medicines, days, roomCharge)
discount = total * 10 / 100
finalBill = calculateDiscountedBill(consultation, medicines, days, roomCharge)

print("Consultation Fee =", format(consultation, ".2f"))
print("Medicine Cost =", format(medicines, ".2f"))
print("Room Charges =", format(days * roomCharge, ".2f"))
print("Total Bill =", format(total, ".2f"))
print("Discount =", format(discount, ".2f"))
print("Final Payable Amount =", format(finalBill, ".2f"))

