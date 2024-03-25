import datetime

def increment_epoch(epoch_date):
    # Convert epoch timestamp to datetime
    dt = datetime.datetime.fromtimestamp(epoch_date / 1000)  # Divide by 1000 to convert milliseconds to seconds

    # Increment by one day
    dt += datetime.timedelta(days=1)

    # Convert back to epoch timestamp
    updated_epoch = int(dt.timestamp() * 1000)  # Multiply by 1000 to convert seconds back to milliseconds

    return updated_epoch

# Example usage
epoch_input = 1535162451650  # Your initial epoch timestamp
updated_epoch_output = increment_epoch(epoch_input)
print(f"Original epoch: {epoch_input}")
print(f"Updated epoch: {updated_epoch_output}")
