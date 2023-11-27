# Quanto voce ganha por hora?
# Horas trabalhadas no mes
# Em reais quanto de papel vendeu (12%)
# mostrar bruto e Descontos e salario liquido

salary_hour = float(input("How much do you receive per hour?\nR:"))
month_day = int(input("How many hours do you work per day?\nR:"))
extra_hour = int(input("How many overtime hours did you this month?\nR:"))
comission_per = int(input("How is your comission percent?\nR:"))
paper_sell = float(input("How many paper you sell this month $?\nR:"))

salary = salary_hour * month_day * 30 + extra_hour 
comission_value = comission_per / 100 * paper_sell
gross_salary = salary + comission_value


income_tax = gross_salary * 0.11
retirement = gross_salary * 0.08
syndicate = gross_salary * 0.05

discounts_total = income_tax + retirement + syndicate

net_salary = gross_salary - discounts_total

print(f"+ Salary ${salary}")
print(f"+ Value Comission ${comission_value}")
print(f"+ Gross Salary ${gross_salary}\n")

print(f"- Income Tax (11%) ${income_tax}")
print(f"- Retirement (8%) ${retirement}")
print(f"- Syndicate (5%)  ${syndicate}\n")

print(f"- Total DIscount - ${discounts_total}")
print(f"= Net salary = ${net_salary}")



# Ir 11 INSS 8 Sindicato 5








