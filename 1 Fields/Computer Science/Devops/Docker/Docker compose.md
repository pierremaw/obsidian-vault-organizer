Multi-container application management.

___

With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration.

```
The Compose specification allows one to define a platform-agnostic container based application. Such an application is designed as a set of containers which have to both run together with adequate shared resources and communication channels.
```

Compose works in all environments: production, staging, development, testing, as well as CI workflows. It also has commands for managing the whole lifecycle of your application:

-   Start, stop, and rebuild services
-   View the status of running services
-   Stream the log output of running services
-   Run a one-off command on a service

The key features of Compose that make it effective are:

-   [Have multiple isolated environments on a single host](https://docs.docker.com/compose/features-uses/#have-multiple-isolated-environments-on-a-single-host)
-   [Preserves volume data when containers are created](https://docs.docker.com/compose/features-uses/#preserves-volume-data-when-containers-are-created)
-   [Only recreate containers that have changed](https://docs.docker.com/compose/features-uses/#only-recreate-containers-that-have-changed)

___
Type: #microtopic 
Topics: [[Computer Science]], [[Software development]], [[Devops]], [[Docker]]

