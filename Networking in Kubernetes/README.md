The question was "How can you restrict networking between pods in Kubernetes? Give an example. Should this
mechanism be enabled separately?"

So in Kubernetes, networking between pods can be restricted using Network Policies. For example.
I can create a Network Policy to only allow traffic from a specific set of pods to a specific set of pods in the same namespace.

If you look at my .yaml file, you can see that policy will only allow traffic from pods with the "role=frontend" label to pods with the "role=db" label in the "default" namespace.

And also Network Policies should be enabled separately by installing and configuring a network plugin that supports them on the cluster.
