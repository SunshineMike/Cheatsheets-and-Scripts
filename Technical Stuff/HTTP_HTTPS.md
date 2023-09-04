# HTTP/HTTPS Protocol Cheatsheet

A quick guide to understanding key aspects, methods, status codes, and headers in HTTP/HTTPS.

## Table of Contents
1. [Introduction](#introduction)
2. [HTTP Methods](#http-methods)
3. [Status Codes](#status-codes)
4. [Request Headers](#request-headers)
5. [Response Headers](#response-headers)
6. [Cookies](#cookies)
7. [HTTPS](#https)

---

## Introduction

HTTP (HyperText Transfer Protocol) and HTTPS (HTTP Secure) are application-layer protocols for transmitting hypermedia documents. HTTPS is the secure version of HTTP.

---

## HTTP Methods

### GET
Retrieve data from the server.
```http
GET /page.html HTTP/1.1
```

### POST
Send data to the server.
```http
POST /form HTTP/1.1
```

### PUT
Update a resource on the server.
```http
PUT /resource/1 HTTP/1.1
```

### DELETE
Remove a resource from the server.
```http
DELETE /resource/1 HTTP/1.1
```

### HEAD
Retrieve headers for a resource.
```http
HEAD /page.html HTTP/1.1
```

### OPTIONS
List available methods for a resource.
```http
OPTIONS /resource HTTP/1.1
```

### PATCH
Apply a partial update to a resource.
```http
PATCH /resource/1 HTTP/1.1
```

---

## Status Codes

### 1xx - Informational
- `100 Continue`

### 2xx - Success
- `200 OK`
- `201 Created`
- `204 No Content`

### 3xx - Redirection
- `301 Moved Permanently`
- `302 Found`
- `304 Not Modified`

### 4xx - Client Errors
- `400 Bad Request`
- `401 Unauthorized`
- `404 Not Found`
- `405 Method Not Allowed`

### 5xx - Server Errors
- `500 Internal Server Error`
- `502 Bad Gateway`
- `503 Service Unavailable`

---

## Request Headers

### Host
Specifies the domain name of the server.
```http
Host: www.example.com
```

### User-Agent
Specifies client information.
```http
User-Agent: Mozilla/5.0
```

### Accept
Specifies media types accepted by the client.
```http
Accept: text/html
```

---

## Response Headers

### Content-Type
Indicates the media type of the resource.
```http
Content-Type: text/html
```

### Content-Length
Indicates the size of the response body.
```http
Content-Length: 348
```

### Set-Cookie
Send cookies from server to client.
```http
Set-Cookie: key=value
```

---

## Cookies

### Cookie Header
Cookies sent from client to server.
```http
Cookie: key=value; key2=value2
```

---

## HTTPS

HTTPS is HTTP with encryption. It uses SSL/TLS to secure the data.

### SSL/TLS
- SSL (Secure Sockets Layer)
- TLS (Transport Layer Security)

---
