def eligibility(sal, age, credit_score):
    reason = ""
    if sal >=25000 and age >= 18 and age <=35 and credit_score >=750:
        return "Eligible"
    if sal <25000:
        reason += ("salary is less than 25000 ")
    if age <18 or age >35:
        reason+=("age is not between 18 and 35 ")
    if credit_score < 750:
        reason+=("credit score is less than 750 ")
        
    return reason

if __name__ == "__main__":
    sal, age, credit = map(int,input("Enter the salary, age, credit:").split())
    print(eligibility(sal, age, credit))