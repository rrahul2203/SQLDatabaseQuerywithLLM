import boto3
import argparse
import time

def get_crawler_status(crawler_name):
    # Create a Glue client
    glue_client = boto3.client('glue')

    # Get the crawler details
    response = glue_client.get_crawler(Name=crawler_name)

    # Extract the crawler state
    crawler_state = response['Crawler']['State']

    return crawler_state



if __name__ == "__main__":
    argParser = argparse.ArgumentParser()
    args = argParser.parse_args()
    client = boto3.client('glue')
    crawler_name=args.glue_crawler_name
    try:
        response = client.start_crawler(Name=crawler_name )
        print("Successfully started crawler. The crawler may take 2-5 mins to detect the schema.")

        while True:
            # Get the crawler status
            status = get_crawler_status(crawler_name)

            # Print the crawler status
            print(f"Crawler '{crawler_name}' status: {status}")

            if status == 'READY':  # Replace 'READY' with the desired completed state
                break  # Exit the loop if the desired state is reached

            time.sleep(10)  # Sleep for 10 seconds before checking the status again

    except:
        print("error in starting crawler. Check the logs for the error details.")