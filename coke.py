def main():
    amount_due=50
    total_insert=0

    while amount_due>0:
        print(f"Amount Due: {amount_due}")

        insert=int(input("Insert Coin: "))

        if insert not in [25,10,5]:
            continue
        else:
            amount_due -= insert
            total_insert += insert
            owe = total_insert-50

    if amount_due == 0:
        print ("Change Owed: 0")
    elif amount_due<0 and total_insert>50:
        print("Change Owed: {}".format(owe))


main()
