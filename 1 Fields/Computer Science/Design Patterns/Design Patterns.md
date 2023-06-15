# The Most Important Design Patterns

- **Singleton**: Ensuring that a class has only one instance and providing a global point of access to that instance.
  - **Initialization**: Creating the unique instance of the class during class loading or on first use.
  - **Global access**: Providing a static method to obtain the singleton instance.
  - **Use cases**: Managing resources that should be shared globally, such as configuration data or database connections.

- **Factory Method**: Defining an interface for creating objects in a superclass but allowing subclasses to alter the type of objects that will be created.
  - **Creator**: An abstract class or interface that declares the factory method.
  - **Concrete Creator**: A subclass that implements the factory method, creating concrete objects.
  - **Use cases**: Decoupling the creation of objects from their usage, enabling code reusability and modularity.

- **Strategy**: Defining a family of algorithms, encapsulating each one, and making them interchangeable, allowing the algorithm to vary independently from clients that use it.
  - **Context**: A class that maintains a reference to a strategy object and delegates tasks to it.
  - **Strategy Interface**: An interface that declares a common method for all supported algorithms.
  - **Concrete Strategy**: A class that implements the strategy interface, providing a specific algorithm.
  - **Use cases**: Selecting and changing algorithms at runtime, promoting loose coupling between classes.

- **Observer**: Defining a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
  - **Subject**: A class that maintains a list of observers and provides methods to add, remove, and notify them.
  - **Observer**: An interface that defines the update method for objects that need to be notified of changes in the subject.
  - **Concrete Observer**: A class that implements the observer interface, updating its state in response to changes in the subject.
  - **Use cases**: Implementing event-driven systems, maintaining consistency between related objects.

- **Builder**: Separating the construction of a complex object from its representation, enabling the same construction process to create different representations.
  - **Director**: A class that controls the construction process, using a builder to create a specific representation.
  - **Builder Interface**: An interface that defines methods for constructing parts of a complex object.
  - **Concrete Builder**: A class that implements the builder interface, providing specific implementations for constructing the object.
  - **Use cases**: Creating complex objects with a step-by-step construction process, allowing flexibility in object construction.

- **Adapter**: Allowing classes with incompatible interfaces to work together by wrapping the interface of one class with a new interface expected by another class.
  - **Target**: An interface that defines the domain-specific methods expected by the client.
  - **Adaptee**: A class with a different interface that needs to be adapted to work with the client.
  - **Adapter**: A class that implements the target interface and delegates calls to the adaptee, translating requests and responses as needed.
  - **Use cases**: Integrating legacy or third-party code with existing systems, promoting code reusability and flexibility.

- **State**: Allowing an object to alter its behavior when its internal state changes, making it appear as if the object has changed its class.
  - **Context**: A class that maintains a reference to a state object, delegating state-specific behavior to it.
  - **State Interface**: An interface that defines methods for handling state-specific behavior.
  - **Concrete State**: A class that implements the state interface, providing a specific behavior for a particular state.
  - **Use cases**: Managing objects with complex state transitions, encapsulating state-dependent behavior, and promoting loose coupling.
___
Type: #topic
Topics: [[Computer Science]]

