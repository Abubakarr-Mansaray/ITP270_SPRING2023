#!/bin/python3
import threading
def process_sales(customer_data, customers, sales, threads, dates):

    # process the customer data

    parts = customer_data.split(";")

    if len(parts) >= 4:

        customer = parts[0].strip()

        sale = float(parts[1].strip("$").strip())

        thread_types = parts[2].strip().split("&")

        date = parts[3].strip()

        # add the cleaned up data to the appropriate lists

        customers.append(customer)

        sales.append(sale)

        threads.append(thread_types)

        dates.append(date)
if __name__ == "__main__":

    daily_sales = input("Enter daily sales separated by commas: ")

    customers = []

    sales = []

    threads = []

    dates = []
    # split the daily sales into a list of transactions

    transactions = daily_sales.split(",")
    # create a thread for each transaction

    for transaction in transactions:

        thread = threading.Thread(target=process_sales, args=(transaction, customers, sales, threads, dates))

        threads.append(thread)
    # start all threads
    for thread in threads:
        thread.start()
    # wait for all threads to finish
    for thread in threads:
        thread.join()
    # print the list of customers
    print(customers)
