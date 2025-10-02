# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import asyncio
from arduino_iot_cloud import ArduinoCloudClient
import traceback

# Arduino IoT Cloud credentials
DEVICE_ID = "26cdd025-7251-41aa-9448-826b73d8254c"
SECRET_KEY = "l1moJFDO?@NDXb8NdSw#EJvU@"

# Callback when temperature changes in the cloud
def on_temperature_changed(client, value):
    print(f"[IoT Cloud] New temperature: {value}")

# Main async function
async def run_cloud_client():
    try:
        print("Connecting to Arduino IoT Cloud...")

        # Create cloud client
        client = ArduinoCloudClient(
            device_id=DEVICE_ID,
            username=DEVICE_ID,
            password=SECRET_KEY
        )

        # Register cloud variable 'temperature'
        client.register(
            "temperature",
            value=None,
            on_write=on_temperature_changed
        )

        print("Listening for cloud variable updates...")

        # Begin listening (poll every 5 seconds, retry every 1 second on failure)
        await client.run(interval=5, backoff=1)

    except Exception as e:
        print("An error occurred:")
        traceback.print_exc()

# Script entry point
if __name__ == "__main__":
    asyncio.run(run_cloud_client())





# %%
