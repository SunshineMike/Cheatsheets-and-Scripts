# SOLID Principles Cheatsheet

A quick reference guide to the SOLID principles, which are essential for maintainable and scalable software design.

## Table of Contents
1. [Introduction](#introduction)
2. [Single Responsibility Principle (SRP)](#single-responsibility-principle-srp)
3. [Open-Closed Principle (OCP)](#open-closed-principle-ocp)
4. [Liskov Substitution Principle (LSP)](#liskov-substitution-principle-lsp)
5. [Interface Segregation Principle (ISP)](#interface-segregation-principle-isp)
6. [Dependency Inversion Principle (DIP)](#dependency-inversion-principle-dip)

---

## Introduction

The SOLID principles are a set of five design principles intended to make software designs more understandable, flexible, and maintainable.

---

## Single Responsibility Principle (SRP)

### Concept
- A class should have only one reason to change.
  
### Example
```java
// Bad
public class Report {
    public void generate() {
        // generate report
    }
    public void saveToFile() {
        // save report to file
    }
}

// Good
public class Report {
    public void generate() {
        // generate report
    }
}

public class ReportSaver {
    public void saveToFile() {
        // save report to file
    }
}
```

---

## Open-Closed Principle (OCP)

### Concept
- Software entities should be open for extension but closed for modification.

### Example
```java
// Bad
public class Circle {
    public double radius;
}

public class AreaCalculator {
    public double calculate(Circle circle) {
        return Math.PI * Math.pow(circle.radius, 2);
    }
}

// Good
public interface Shape {
    double area();
}

public class Circle implements Shape {
    public double radius;
    public double area() {
        return Math.PI * Math.pow(radius, 2);
    }
}
```

---

## Liskov Substitution Principle (LSP)

### Concept
- Objects of a superclass should be replaceable with objects of a subclass without affecting program correctness.

### Example
```java
// Good
public class Bird {
    public void fly() {
        // implementation
    }
}

public class Penguin extends Bird {
    @Override
    public void fly() {
        throw new UnsupportedOperationException();
    }
}
```

---

## Interface Segregation Principle (ISP)

### Concept
- Clients should not be forced to depend on interfaces they do not use.

### Example
```java
// Bad
public interface Worker {
    void work();
    void eat();
}

// Good
public interface Workable {
    void work();
}

public interface Eatable {
    void eat();
}
```

---

## Dependency Inversion Principle (DIP)

### Concept
- High-level modules should not depend on low-level modules; both should depend on abstractions.

### Example
```java
// Bad
public class MySQLDatabase {
    public void connect() {
        // implementation
    }
}

public class UserManager {
    private MySQLDatabase database;
}

// Good
public interface Database {
    void connect();
}

public class UserManager {
    private Database database;
}
```

---
