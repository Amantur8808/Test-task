import azure.storage.queue

def main(mytimer: func.TimerRequest, outqueue: func.Out[str]) -> None:
    queue_service = azure.storage.queue.QueueServiceClient(
        account_url="https://{}.queue.core.windows.net/".format(STORAGE_ACCOUNT_NAME),
        credential=STORAGE_ACCOUNT_KEY
    )
    queue_service.create_queue("myqueue")
    messages = queue_service.get_messages("myqueue")
    for message in messages:
        message_text = message.content
        queue_service.delete_message("myqueue, message.id, message.pop_receipt)
        outqueue.set(message_text)
    #Run container service
    subprocess.call(["kubectl", "run", "hello-world", "--image=alpine", "--restart=Never", "--command", "--", "echo", message_text])                                 
