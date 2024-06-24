from flat import Bill, Flatmate
from reports import PdfReport, FileSharer

amount = float(input("Enter the bill amount: "))
period = input("Enter the bill period: e.g. December 2024")

name1 = input("Enter your name: ")
days_in_house1 = int(input("Enter the days of your stays in the house: "))

name2 = input("Enter another flatmate name: ")
days_in_house2 = int(input(f"Enter the days of {name2} in the house: "))

the_bill = Bill(amount=amount, period=period)
flatmate1 = Flatmate(name=name1, days_in_house=days_in_house1)
flatmate2 = Flatmate(name=name2, days_in_house=days_in_house2)

print(f"{flatmate1.name} pays: ", flatmate1.pays(bill=the_bill, flatmate2=flatmate2))
print(f"{flatmate2.name} pays: ", flatmate2.pays(bill=the_bill, flatmate2=flatmate1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)

file_sharer = FileSharer(filepath=pdf_report.filename)
print(file_sharer.share())