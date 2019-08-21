def publish_messages(project_id, topic_name):
    """Publishes multiple messages to a Pub/Sub topic."""
    # [START pubsub_quickstart_publisher]
    # [START pubsub_publish]
    from google.cloud import pubsub_v1

    publisher = pubsub_v1.PublisherClient()
    # The `topic_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/topics/{topic_name}`
    topic_path = publisher.topic_path(project_id, topic_name)
    print(topic_path)
    for n in range(1, 10):
	data = u'Message number {}'.format(n)
        # Data must be a bytestring
        print("data :" + data)
	data = data.encode('utf-8')
        # When you publish a message, the client returns a future.
        future = publisher.publish(topic_path, data=data)
        print(future.result())

    print('Published messages.')
