def splitter(total_amount,no_of_ppl,tip_percentange):
    
    tip_amount = (total_amount * tip_percentange) / 100
    amount_per_person = (total_amount + tip_amount) / no_of_ppl
    return amount_per_person


if __name__ == "__main__":
    amount, ppl , percent = map(float, input("Enter amount, Number of people, tip percentage:").split())
    print(f"Amount per person: {splitter(amount,ppl,percent)}")  
    