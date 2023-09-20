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
