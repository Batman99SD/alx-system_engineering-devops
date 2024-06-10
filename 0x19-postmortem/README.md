# API Service Degradation

## Summary

On May 15th, 2024, API services were slow, affecting 60% of users. Users experienced significant delays in response times, with some requests timing out. A memory leak in the caching layer caused the servers to exhaust available memory and swap, severely degrading performance.

## Timeline

10:30 - Issue detected via monitoring alert indicating high API response times and increased error rates.
10:35 - Initial investigation focused on application logs and database performance.
10:50 - Backend team observed normal database performance, ruled out database as the cause.
11:00 - Misleading path: Investigated recent application updates for possible regressions.
11:20 - Escalated to infrastructure team to check server health and resource utilization.
11:35 - Identified high memory usage and swap activity on caching servers.
12:00 - Detailed memory profiling revealed a memory leak in the caching layer software.
12:15 - Deployed a temporary fix by restarting caching servers to release memory.
12:45 - Applied a patch to the caching layer to address the memory leak.
13:00 - Monitoring confirmed improved response times and error rates returned to normal levels.

## Root Cause and Resolution

The root cause of the outage was a memory leak in the caching layer software, introduced in a recent update. The memory leak caused the servers to exhaust available memory, leading to increased swapping and degraded performance.

### Resolution Steps:

    Identification: Memory profiling tools identified the memory leak in the caching layer.
    Temporary Fix: Restarted caching servers to temporarily alleviate the memory pressure.
    Permanent Fix: Applied a patch to the caching layer software to fix the memory leak.
    Verification: Monitored system performance to ensure the issue was resolved and service returned to normal.

## Corrective and Preventative Measures

- Enhance memory usage monitoring for caching servers.
- Improve testing procedures to catch memory leaks before deploying updates.
- Strengthen the rollback plan for caching layer updates to allow quick reversion in case of issues.

