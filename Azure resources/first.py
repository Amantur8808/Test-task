import azure.storage.queue

def main(mytimer: func.TimerRequest, outqueue: func.Out[str]) -> None:
    queue_service = azure.storage.queue.QueueServiceClient(
        account_url="https://{}.queue.core.windows.net/".format(STORAGE_ACCOUNT_NAME),
        credential=STORAGE_ACCOUNT_KEY
    )
    queue_service.create_queue("myqueue")
    outqueue.set("Hello World")
    queue_service.put_message("myqueue", outqueue.get())
