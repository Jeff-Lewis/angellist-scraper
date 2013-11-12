from iron_mq import IronMQ
ironmq = IronMQ(project_id="", token="")
queue = ironmq.queue("requests")

# Warning to all... this is probably the worst possible way to
# enque a bunch of inorder numbers... you have been warned.

# Queue ALL THE THINGS
l = range(500000)
# but do it in small batches
n = 3000
list_of_messages = [l[i:i+n] for i in range(0, len(l), n)]

for ls in list_of_messages:
    # unpack and post the array of #s
    queue.post(*[str(i) for i in ls])
