# Simplified Online HelpDesk System 📞💬

A project aimed at implementing a simplified version of an online helpdesk system using **WebSockets** for real-time communication. The system supports multiple client-server interactions and offers private chat functionality based on the concept of availability.

## Introduction
<img width="200" alt="Screenshot 2024-12-25 at 12 54 57 AM" src="https://github.com/user-attachments/assets/e6792e6c-e2e8-43d0-b97f-724063bb7ad3" />
Online HelpDesk Systems are increasingly efficient, often equipped with automated replies. However, many users prefer human interaction over machine responses. This project implements a real-time helpdesk system using WebSockets to enable seamless communication between clients and server-side users without the need for page refreshes.

### Key Features
- **Multiple Clients and Servers**: Supports concurrent client-server interactions with availability-based user assignment.
- **Private Chat**: Enables secure, room-based chat sessions.
- **Real-Time Functionality**: Uses WebSocket technology for instantaneous communication.
- **Ignore Requests**: Server-side users can ignore client requests when necessary.
- **Scalability**: Can be extended to discussion forums capable of supporting up to 250 users.

## Technologies Used
- **Backend**: Flask (lightweight web framework), SQLAlchemy (database ORM for SQL commands), PostgreSQL (database).
- **Frontend**: HTML, CSS, JavaScript.
- **WebSockets**: Powered by SocketIO for real-time communication.

## Advantages
- No data logging ensures privacy.
- Near-instantaneous user pairing.
- Minimal data collection for enhanced user privacy.
- High scalability potential.

## Functionalities
1. **Client-Server Availability**: Assigns server-side users to clients based on availability.
2. **Private Chat Rooms**: Secure chat sessions between clients and servers.
3. **User Notifications**: Displays unavailability messages when no server users are free.
4. **Extensibility**: Potential for use as discussion forums.

## Getting Started

### Prerequisites
- Python 3.x
- Pip
- PostgreSQL

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd HELPDESK

<img width="400" alt="Screenshot 2024-12-25 at 12 54 04 AM" src="https://github.com/user-attachments/assets/a8b82b2b-22d9-458c-9398-fbd9521f3333" />
<img width="400" alt="Screenshot 2024-12-25 at 12 50 57 AM" src="https://github.com/user-attachments/assets/9044ad42-949c-45a7-94ee-fce93d6b725c" />
<img width="400" alt="Screenshot 2024-12-25 at 12 51 11 AM" src="https://github.com/user-attachments/assets/50bb79c3-bf44-4117-866a-5560abc4f97a" />
