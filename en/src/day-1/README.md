# Uncomplicating Prometheus - The Training

## DAY-1

### What are we going to see today?

Today, we will focus on what Prometheus is and what problem it solves.
We will understand the different types of monitoring and the differences between them.
Today is the day to learn about the history of Prometheus and its motivation for its creation on SoundCloud.
Let's understand the architecture of Prometheus and how it relates to other applications.
And finally, let's install Prometheus and do our first setup for our newest monitoring service.
We will also have our first contact with the Prometheus web interface and create our first query.


### Why do we need tools like Prometheus?

I know that we haven't talked about what monitoring itself is yet, but I think it's essential to bring this scenario so that you can later understand what Prometheus and this monitoring are for and what it is for.

Well, as you know, every company has an environment where one or more applications are running, consuming some computational resource, whether local, in a data center, or even in a cloud provider, which is more common today.

Let's imagine that we have an online store, the famous e-commerce. Can you imagine how many components we have to monitor to make sure, or almost, that everything is working as expected?

In the case of e-commerce, let's imagine something straightforward and small. You need a web server for an online store, so let's use Nginx.
But to run Nginx, we'll need a VM, container, pod, or an instance in the cloud, so we already have more things to worry about.

Let's imagine that we chose to run Nginx on a VM to simplify things for now. So if we have the VM, we have a hypervisor managing the VM, the host where the VM is running, and Linux installed on the VM where Nginx is running. Not to mention all the network elements involved during the requests to this store of ours.

With this, you can already imagine the size of the problem, and look at that we are talking about a simple store running on a VM, without worrying about complex environments in high availability, resilient and must follow standards to adapt to a particular market niche or local legislation.

If we stop to think only about the items we have to monitor on the host hosting this VM, it would already be a huge list, with much work for the coming days.

There is no shortage of things we need to monitor in our environment.

If you start thinking carefully, you will see that monitoring is crucial for our day-to-day things, where it has no relation to our work. For example, as I write this material, I am following my mother and mother-in-law's flight back to Brazil, thanks to a real-time monitoring system, which brings me this information.

Note that monitoring is not only necessary for when things go wrong. Monitoring is essential to follow the pattern, understand how your systems are operating, and monitor specific activity, as is my case now following the flight.

For us technology professionals, it is essential to understand the importance and how to implement a good monitoring system for our services and systems.
Only through monitoring will we be able to have reliability and efficiency in our services, bringing much value to the business due to the efficiency and availability of our systems.

Through monitoring, we will understand if our service is fully operational or if it is degraded, delivering a terrible experience for our users.

#### What is monitoring?

In my opinion, monitoring means having the current status of the desired item. For example, in the case of a physical machine running Linux, I want to monitor the hardware to ensure that CPU heating problems will not hinder the availability of my system. Still using this example, we have to watch the operating system, as we don't want a full disk or an overloaded network card burdening the entire system.
That's what we haven't even talked about yet about the VM's operating system or the application itself, Nginx.

Monitoring means that you know what is happening in your infrastructure, in your app, in your service in real-time, and the event of a failure or anomaly, that the people involved in the recovery of that component are notified with the maximum amount of information to assist in troubleshooting.

##### Monitoring and Observability
