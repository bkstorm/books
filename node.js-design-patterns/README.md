# Preface

- The biggest innovation of the decade:
  - Javascript
  - Single-threaded programming model and its asynchronous architecture.
  - Its ecosystem.

# Chapter 1: The Node.js Platform

- The Node.js philosophy:
  - Small core
  - Small modules
    - Easier to understand and use
    - Simpler to test and maintain
    - Small in size and perfect for use in the browser
  - Small sureface area
  - Simplicity and pragmatism
- How Node.js works:
  - I/O is slow
  - blocking I/O
  - nonblocking I/O
  - reactor pattern
  - livuv, the I/O engine
- JavaScript in Node.js
  - Run the latest JavaScript with confidence
  - The module system
  - Full access to operating system services
  - Running native code

# Chapter 2: The Module System

- The need for modules:
  - Having a way to split the codebase into multiple files.
  - Allowing code reuse across different projects.
  - Encapsulation (or information hiding).
  - Managing dependencies.

## CommonJs modules:

## ESM: ECMAScript modules

- static import => static analysis of the dependency tree, which allows optimizations such as dead code elimination (tree shaking) and more.
- read-only live bindings
- circular dependency resolution

- Module identifiers (module specifiers):
  - relative specifiers
  - absolute specifiers
  - bare specifiers
  - deep import specifiers
- Async imports (dynamic imports)
- Module loading in depth
  - Loading phases:
    - parsing
    - instantiation
    - evaluation
  - read-only live bindings

# Chapter 3: Callbacks and Events

- CPS: continuation passing style.
- Pitfalls of callbacks
- sync / async:
  - Always choose a direct style for purely synchronous functions.
  - Use blocking APIs sparingly and only when they don't affect
    the ability of the application to handle concurrent asynchronous
    operations.
  - You can guarantee that a callback is invoked asynchronously by
    deferring its execution using process.nextTick().
- The Observer pattern
  - EventEmitter
- Callback or EventEmitter:
  - Callbacks have some limitations when it comes to supporting different
    types of events. In fact, we can still differentiate between multiple events
    by passing the type as an argument of the callback, or by accepting several
    callbacks, one for each supported event. However, this can't exactly be
    considered an elegant API. In this situation, the EventEmitter can give a
    better interface and leaner code.
  - The EventEmitter should be used when the same event can occur multiple
    times, or may not occur at all. A callback, in fact, is expected to be invoked
    exactly once, whether the operation is successful or not. Having a possibly
    repeating circumstance should make us think again about the semantic
    nature of the occurrence, which is more similar to an event that has to be
    communicated, rather than a result to be returned.
  - An API that uses callbacks can notify only one particular callback, while
    using an EventEmitter allows us to register multiple listeners for the
    same event.

# Chapter 4: Asynchronous Control Flow: Patterns with Callbacks

- sequential execution
- parallel execution
- limited parallel execution

# Chapter 5: Asynchronous Control Flow: Patterns with Promises and Async/Await

# Chapter 6: Coding with Streams

- Importance of streams

  - Readable streams:
    - 2 approachs to receive data: non-flowing and flowing
  - Writable streams:
    - Backpressure
  - Duplex
  - Transform
  - PassThrough:
    - Observability
    - Late piping: Use a PassThrough stream when you need to provide a
      placeholder for data that will be read or written in the future.
    - Lazy streams

- Piping patterns
  - Combining
  - Forking
  - Merging
  - Multiplexing and demultiplexing

Pattern:

- Use a stream, or combination of streams, to easily iterate over a set
  of asynchronous tasks in sequence.(206)

# Chapter 7: Creational

## Factory

> Its main advantage is its ability to decouple the creation of an object from one particular implementation. This allows us, for example, to create an object whose class is determined at runtime. Factory also allows us to expose "a surface area" that is much smaller than that of a class; a class can be extended or manipulated, while a factory, being just a function, offers fewer options to the user, making it more robust and easier to understand. Finally, a factory can also be used to enforce encapsulation by leveraging closures.

## Builder

> Builder is a creational design pattern that simplifies the creation of complex objects by providing a fluent interface, which allows us to build the object step by step. This greatly improves the readability and the general developer experience when creating such complex objects.

## Revealing Constructor

> It solves a very tricky problem, which is: how can we "reveal" some private functionality of an object only at the moment of the object's creation? This is particularly useful when we want to allow an object's internals to be manipulated only during its creation phase. This allows for a few interesting scenarios, such as:

- Creating objects that can be modified only at creation time
- Creating objects whose custom behavior can be defined only at creation time
- Creating objects that can be initialized only once at creation time

## Singleton

> The purpose of the Singleton pattern is to enforce the presence of only one instance of a class and centralize its access. There are a few reasons for using a single instance across all the components of an application:

- For sharing stateful information
- For optimizing resource usage
- To synchronize access to a resource

## Dependency Injection

# Chapter 8: Structural

## Proxy

> A proxy is an object that controls access to another object, called the subject. The proxy and the subject have an identical interface, and this allows us to swap one for the other transparently; in fact, the alternative name for this pattern is surrogate.

## Decorator

## Adapter

> The Adapter pattern allows us to access the functionality of an object using a different interface.

# Chapter 9: Behavioral Design Patterns

## Strategy

> The Strategy pattern enables an object, called the context, to support variations in its logic by extracting the variable parts into separate, interchangeable objects called strategies. The context implements the common logic of a family of algorithms, while a strategy implements the mutable parts, allowing the context to adapt its behavior depending on different factors, such as an input value, a system configuration, or user preferences.

## State

> The State pattern is a specialization of the Strategy pattern where the strategy changes depending on the state of the context.

## Template

> The Template pattern defines an abstract class that implements the skeleton (representing the common parts) of a component, where some of its steps are left undefined. Subclasses can then fill the gaps in the component by implementing the missing parts, called template methods.

## Iterator

## Generator

## Middleware

## Command

# Chapter 11: Advanced Recipes

## Dealing with asynchronously initialized components

- Local initialization check
- Delayed startup
- 🌟 Pre-initialization queues

## Asynchronous request batching and caching

## Canceling asynchronous operations

- Promise
- Generator

## Running CPU-bound tasks

- Interleaving with setImmediate
- Using external processes
- Using worker threads

# Chapter 12: Scalability and Architectural Patterns

> Scalability can be described as the capability of a system to grow and adapt to everchanging conditions.

- Scale cube

## Cloning and load balancing

- Cluster module
- Dealing with stateful communications
  - Sharing the state across multiple instances
  - Sticky load balancing
- Scaling with a reverse proxy
- Dynamic horizontal scaling
- Peer-to-peer load balancing
- Scaling applications using containers

## Decomposing complex applications

# Chapter 13: Messaging and Integration Patterns

## Fundamentals of messaging system

- The direction of the communication, which can be one-way only
  or a request/reply exchange
- The purpose of the message, which also determines its content
- The timing of the message, which can be sent and received in-context
  (synchronously) or out-of-context (asynchronously)
- The delivery of the message, which can happen directly or via a broker

### Message types

- Command: The purpose of this type of message is to trigger the execution of an action or a task on the receiver.
- Event: An Event Message is used to notify another component that something has occurred.
- Document: The Document Message is primarily meant to transfer data between components and machines.
