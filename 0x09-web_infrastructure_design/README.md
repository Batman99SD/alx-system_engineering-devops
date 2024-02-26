#Web infrastructure design
#task_0

Web Infrastructure Design:

    User Request:
        A user wants to access www.foobar.com.

    Domain Name:
        The domain name "foobar.com" is registered and configured with a DNS record that points the www subdomain to the server's IP address (let's say 8.8.8.8).

    Server (8.8.8.8):
        A single server hosts the entire web infrastructure.

    Web Server (Nginx):
        Nginx is installed on the server and configured as the web server.
        Handles HTTP requests and acts as a reverse proxy, passing requests to the application server.

    Application Server:
        An application server (e.g., running a LAMP stack) is installed on the server.
        Hosts the application codebase and processes dynamic content.

    Application Files (Code Base):
        The application codebase is stored on the server.
        Nginx forwards dynamic requests to the application server for processing.

    Database (MySQL):
        MySQL is installed on the server.
        Stores and manages the website's database, handling data storage and retrieval.

    Communication:
        The server communicates with the user's computer over the Internet using the HTTP/HTTPS protocol.
        The user's browser sends an HTTP request to the server, and the server responds with the requested web page.

Specifics about the Infrastructure:

    What is a server?
        A server is a computer system that hosts and provides services or resources to other computers (clients) in a network. In this context, it hosts the web infrastructure for www.foobar.com.

    Role of the Domain Name:
        The domain name acts as a human-readable address for the website (www.foobar.com) and is translated into an IP address by the DNS system.

    Type of DNS Record for www.foobar.com:
        The DNS record for www.foobar.com is an A (Address) record, mapping the domain to the server's IP address.

    Role of the Web Server:
        Nginx serves as the web server, handling static content, acting as a reverse proxy for dynamic requests, and managing connections between the user and the application server.

    Role of the Application Server:
        The application server runs the application codebase, processes dynamic content, and interacts with the database to generate responses to user requests.

    Role of the Database:
        MySQL serves as the database, storing and managing the website's data, including user information, content, etc.

    Communication with User's Computer:
        Communication between the server and the user's computer occurs over the HTTP/HTTPS protocol. The server responds to user requests by sending HTML, CSS, and other resources required to render the web page in the user's browser.

Issues with the Infrastructure:

    Single Point of Failure (SPOF):
        The entire infrastructure relies on a single server. If this server fails, the entire website becomes inaccessible.

    Downtime during Maintenance:
        Any maintenance activities, such as deploying new code or restarting the web server, result in downtime. During this period, the website is not available to users.

    Limited Scalability:
        The infrastructure may struggle to handle a significant increase in traffic. As traffic grows, a single server may become a bottleneck, leading to performance issues and potential downtime.

#task_1

Web Infrastructure Design:

    User Request:
        A user wants to access www.foobar.com.

    Domain Name:
        The domain name "foobar.com" is registered and configured with DNS records pointing to the load balancer's IP address.

    Load Balancer (HAproxy):
        HAproxy is introduced to distribute incoming traffic among multiple servers, improving performance, and ensuring high availability.
        It uses a Round Robin distribution algorithm to distribute requests evenly among the available servers.

    Server 1 and Server 2:
        Two servers are added to provide redundancy, fault tolerance, and scalability.
        Both servers have Nginx installed as the web server to handle incoming requests.

    Application Server:
        The application server runs the code base for www.foobar.com, handling dynamic content and business logic.

    Database (MySQL Primary-Replica Cluster):
        A MySQL Primary-Replica (Master-Slave) cluster is introduced to ensure data redundancy, fault tolerance, and read scalability.
        The Primary node manages write operations, and the Replica node(s) replicate data to maintain a synchronized copy.

    Application Files (Code Base):
        The application codebase is stored on the servers and is synchronized to ensure consistency.

Specifics about the Infrastructure:

    Why Load Balancer (HAproxy):
        Added for distributing incoming traffic evenly among multiple servers to improve performance, scalability, and ensure high availability.

    Load Balancer Distribution Algorithm:
        Round Robin: Requests are distributed in a circular sequence to each server in turn.

    Active-Active or Active-Passive Setup:
        Active-Active: Both servers actively handle incoming requests, providing load distribution and redundancy.

    Database Primary-Replica Cluster:
        The Primary node handles write operations, and Replica node(s) replicate data for fault tolerance and read scalability.

    Difference Between Primary and Replica Nodes:
        Primary Node: Handles write operations, manages data consistency, and is the authoritative source.
        Replica Node: Holds a synchronized copy of the data, primarily used for read operations, provides fault tolerance, and improves scalability.

Issues with the Infrastructure:

    Single Point of Failure (SPOF):
        The load balancer is a potential single point of failure. If it fails, users won't be able to access the web application.

    Security Issues:
        No firewall is mentioned in the design, leaving the infrastructure vulnerable to unauthorized access. Additionally, there is no mention of HTTPS, exposing the communication between users and the web servers to potential security threats.

    No Monitoring:
        There is no provision for monitoring the health and performance of the servers, load balancer, or database cluster. Lack of monitoring can lead to delays in identifying and resolving issues, impacting the availability and performance of the web application.

#task_2

Web Infrastructure Design:

    User Request:
        A user wants to access www.foobar.com securely.

    Domain Name:
        The domain name "foobar.com" is registered and configured with DNS records pointing to the load balancer's IP address.

    Load Balancer (Nginx with SSL Termination):
        Nginx is used as the load balancer, and SSL termination is performed at this level to ensure secure communication.
        SSL certificates for www.foobar.com are installed on the load balancer.

    Server 1, Server 2, Server 3:
        Three servers are added to provide redundancy, fault tolerance, and scalability.
        Each server has the same components: Nginx as the web server, the application server, and MySQL as the database.

    Firewalls:
        Firewalls are added to control and monitor incoming and outgoing network traffic to enhance security.
        They are configured to allow only necessary traffic and block unauthorized access.

    Monitoring Clients (Sumo Logic or Other Monitoring Services):
        Monitoring clients are installed on each server to collect data for analysis and monitoring.
        Sumo Logic or another monitoring service is used to aggregate and analyze the data from all servers.

Specifics about the Infrastructure:

    Why Firewalls:
        Added for network security. Firewalls control traffic based on predefined security rules, preventing unauthorized access and enhancing overall system security.

    Why HTTPS:
        To encrypt the traffic between the user's browser and the web server, ensuring the confidentiality and integrity of the data during transit.

    Why Monitoring:
        Monitoring helps track the performance, health, and security of the infrastructure. It allows for proactive issue detection, troubleshooting, and optimization.

    How Monitoring Tool Collects Data:
        The monitoring tool (Sumo Logic or other) collects data through agents installed on each server. These agents gather information on system metrics, application performance, and security events.

    Monitoring Web Server QPS:
        To monitor web server QPS (Queries Per Second), the monitoring tool analyzes the request logs generated by Nginx. Metrics related to the number of incoming requests per second can be monitored to understand server load and performance.

Issues with the Infrastructure:

    Terminating SSL at the Load Balancer Level:
        This might be considered an issue because it exposes decrypted traffic between the load balancer and the servers within the internal network. For increased security, SSL termination could be done directly on the web servers.

    Single MySQL Server Accepting Writes:
        This is a potential issue because it creates a single point of failure for write operations. If the MySQL server fails, write operations cannot be performed. Consider implementing a MySQL Primary-Replica (Master-Slave) cluster for fault tolerance.

    Identical Servers with Same Components:
        Having identical servers with the same components might be a problem if all servers are affected by a common issue, leading to a widespread failure. Introducing diversity in the infrastructure components or distributing components across different server types can enhance overall system resilience.

#task_3

Updated Web Infrastructure Design:

    User Request:
        A user wants to access www.foobar.com securely.

    Domain Name:
        The domain name "foobar.com" is registered and configured with DNS records pointing to the load balancer's IP address.

    Load Balancer Cluster (HAProxy):
        HAProxy is configured in a cluster setup with two instances for high availability.
        It distributes incoming traffic evenly among multiple servers and ensures redundancy.

    Server 1 (Web Server):
        Server dedicated to hosting the web server (Nginx).
        Nginx handles static content, SSL termination, and forwards dynamic requests to the application server.

    Server 2 (Application Server):
        Dedicated server for running the application server (e.g., Node.js, Django, etc.).
        Handles dynamic content, executes business logic, and communicates with the database.

    Server 3 (Database - MySQL):
        Dedicated server hosting the MySQL database.
        Manages data storage, retrieval, and ensures data consistency.

    Firewalls:
        Firewalls are in place to control and monitor network traffic for security purposes.
        They are configured to allow only necessary traffic and block unauthorized access.
