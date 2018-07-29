import os
import sys
from google.cloud import pubsub_v1
from google.cloud.pubsub import types

data = sys.argv[1]
nn = "000"
if data == "channel":
    nn=sys.argv[2]

os.environ['GOOGLE_APPLICATION_CREDENTIALS']='/home/<INSERT USERNAME>/<INSERT JSON>.json'
#batch_settings = pubsub_v1.types.BatchSettings( max_bytes=0,)
#publisher = pubsub_v1.PublisherClient(batch_settings)
publisher = pubsub_v1.PublisherClient()
topic='projects/rpiir-208011/topics/tatasky'
publisher.publish(topic, data.encode('utf-8'),num=nn)
