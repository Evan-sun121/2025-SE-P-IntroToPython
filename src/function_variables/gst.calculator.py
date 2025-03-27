def main():
    purchase = int(input("How much was the purchase? "))
    percentage = int(input("What percentage is the GST rate? "))
    price = float(purchase)
    percent = float(percentage)
    gst = price * percent
    print(f"GST will be ${gst:.2f}")

    return gst


main()
