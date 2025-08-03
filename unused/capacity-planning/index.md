---
draft: true
---

-   Problem: how many servers do we need?
-   More specific question is how many we need to:
    -   Give reasonable guarantees of uptime
        -   99.99% availability means 4.5 minutes of downtime every 30 days
        -   Which is probably not good enough for 911
    -   Process some number of transactions per second
    -   Ensure no transaction takes longer than a certain time
    -   Ensure predictable services times
        -   Most people would rather wait 10 seconds every time than 1 second 9 times and 20 seconds the tenth
-   Some questions can be answered with basic statistics
-   Others require <span g="queueing_theory">queueing theory</span>

## How does a simple server behave?

-   Assume:
    -   Requests arrive randomly at a rate of $$\lambda$$ per second
        -   So inter-arrival time is $$1/\lambda$$
    -   Requests stay in queue once they arrive (no drop-outs)
    -   Served in arrival order (first-come, first-served)
    -   Requests completed at a rate of $$\mu$$ per second
    -   Require $$\lambda \lt \mu$$ or the queue will grow infinitely long
-   <span g="littles_law">Little's Law</span>
    -   Let $$N$$ be the average number of requests in the system (queue length + 1)
    -   Let $$T$$ be the average total time a request stays in the system (queueing plus service)
    -   $$N = \lambda T$$
    -   I.e., average number of requests in the system = arrival rate times the average time each request is in the system
    -   Example: arrival = 5 requests/second, time in the system is 2 seconds, so 10 requests in the system at a time
-   Another form: average number of requests being processed at any time = throughput $$\times$$ average time each request is in the system
    -   So 0.5 requests/second and a 10-second response time implies 5 servers
    -   If a site handles 100 million requests/day with a 5-second response time, they must have at least 55,000 servers
-   Let $$q(t)$$ be the probability that nothing happens in time interval $$t$$
-   If $$x$$ is the waiting time for the first event, then $$P(x \gt t) = q(t)$$
-   If the system has no memory, then $$q(t_1 + t_2)$$ = $$q(t_1)q(t_2)$$
-   Only solution is $$q(t) = e^{-\lambda t}$$
    -   $$P(x \gt t_2 + t_1 | x \gt t_1)$$
        = $$P(x \gt t_2 + t_1)/P(x \gt t_1)$$
        = $$e^{- \lambda (t_2 + t_1)} / e^{- \lambda t_1}$$
        = $$e^{- \lambda t_2}$$
-   So $$P(x \leq t) = 1 - e^{-\lambda t}$$ (FIXME: figure)
-   Mean and standard deviation both equal the rate $$\lambda$$
-   Probably of $$k$$ events in time $$t$$ is a <span g="poisson_distribution">Poisson distribution</span>
    $$P(k, t) = \lambda t e^{- \lambda t}/k!$$ (FIXME: figure)

## How can we model queues?

-   For small $$\delta t$$:
    -   Probability of no request in that time is $$P_0(\delta t) = 1 - \lambda \delta t$$
    -   Probability of one request in that time is $$P_1(\delta t) = \lambda \delta t$$
    -   Probability of more than one request is $$P_k(\delta t) = 0$$ for $$k \gt 1$$
-   Queue is an infinite <span g="state_machine">state machine</span> where each state is the number of requests in the queue (FIXME: figure)
    -   Transition probability going upward is $$\lambda$$
    -   If service time also follows exponential distribution, transition probability going downward is $$\mu$$

$$
\begin{align*}
\mu P_1 & = & \lambda P_0 \\
\lambda P_0 + \mu P_2 & = & \lambda P_1 + \mu P_1 \\
\ldots & = & \ldots \\
P_0 + P_1 + \ldots & = & 1 \\
\end{align*}
$$

-   Solution is $$P_0 = 1 - \frac{\lambda}{\mu}$$ and $$P_i = (\frac{\lambda}{\mu})^i (1 - \frac{\lambda}{\mu})$$
-   <span g="utilization">Utilization</span> $$U = 1 - P_0 = \frac{\lambda}{\mu}$$
-   Number of requests in the system is $$\sum_{i=0}^{\infty} i P_i$$
    = $$\sum_{i=0}^{\infty} i (\frac{\lambda}{\mu})^i (1 - \frac{\lambda}{\mu})$$
    = $$(1 - \frac{\lambda}{\mu}) \sum_{i=0}^{\infty} i (\frac{\lambda}{\mu})^i$$
    = $$(1 - \frac{\lambda}{\mu}) \sum_{i=0}^{\infty} \frac{\lambda / \mu}{(1 - \lambda / \mu)^2}$$
    = $$\frac{\lambda / \mu}{1 - \lambda / \mu}$$
-   Use Little's Law to get mean response time
    -   $$N = \lambda T$$
    -   So $$T = N / \lambda$$
        = $$\frac{(\lambda / \mu)}{1 - \lambda / \mu} \frac{1}{\lambda}$$
        = $$\frac{1}{\mu - \lambda}$$
    -   Remember: we require $$\lambda \lt \mu$$ or the queue will grow infinitely long
-   Using the alternative formulation of Little's Law to get mean number of requests in queue
    -   $$N = (\frac{\lambda}{\mu})^2 / (1 - \lambda / \mu)$$
-   Example: file server gets 40 requests/second, needs 10 msec/request (so $$\mu$$ is 100)
    -   Assume requests are independent (probably not true)
    -   Average response time is 16.6 msec
-   But look how behavior changes:

| $$\lambda$$ (req/sec) | $$\mu$$ (req/sec) | Response time (msec) | Queue length (req) |
| ------------------: | --------------: | -------------------: | -----------------: |
|                  40 |             100 |                 16.6 |               0.26 |
|                  80 |             100 |                 50.0 |               3.20 |
|                  90 |             100 |                100.0 |               8.10 |

-   I.e., doubling request rate triples response time
-   Increase request rate slightly to 90 requests/second, response time doubles again to 100 msec
-   If we have $$s$$ servers and write $$\rho = \lambda / \mu$$ then the probability that a request goes into queue is:

$$
\begin{align*}
C(s, \rho) & = & \frac{1}{1 + (1 - \rho)(\frac{s!}{(s \rho)^s})\sum_{k=0}^{s-1}\frac{(s \rho)^k}{k!}}
\end{align*}
$$

-   Average number of requests in the system (in queue and being served) is $$\frac{1 - \rho}{\rho} C(s, \rho) + s \rho$$

-   Response time is $$\frac{C(s, \rho)}{s \mu - \lambda} + \frac{1}{\mu}$$

-   Calculate requests in the system and waiting times for various combinations of $$\lambda$$, $$\mu$$, and $$s$$
    -   Two servers of the same speed does better than halving the response time
    -   One server that's twice as fast is slightly better

| $$\lambda$$ (req/sec) | $$\mu$$ (req/sec) | servers | response (msec) |
| ----------: | ----------: | ------: | --------------: |
| 20 | 40 | 1 |   75.0 |
| 20 | 40 | 2 |   33.3 |
| 20 | 80 | 1 |   29.2 |

## What are the limits on scalability?

-   Analysis above assumes that there is no cost to handing requests to servers
-   In reality, there usually is
-   <span g="amdahls_law">Amdahl's Law</span>
    -   Let $$\theta$$ be the fraction of work that can be parallelized
    -   Total time on $$s$$ servers is $$T_s = \theta T_1 / s + (1 - \theta)T_1$$
    -   Speedup as $$s \rightarrow \infty$$ is $$1 / \theta$$
    -   I.e., if 5% of the work is inherently serial, the maximum possible speedup is 20X
