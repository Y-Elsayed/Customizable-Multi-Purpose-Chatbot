# Customizable Multi Purpose Chatbot with Analytics tool
RAG based Multi Purpose chatbot, employing LLMs to generate output, and visualize analytics of Chatbot's performance to different user queries.

## Overview

# Chatbot Service with LLM Integration

## Overview

This project implements a chatbot service that uses advanced Natural Language Processing (NLP) models, including Language Models (LLMs) for intelligent interaction. The system is based on the **Retrieval-Augmented Generation (RAG)** approach, allowing the chatbot to retrieve relevant information from an external database before generating contextually appropriate responses. This enhances the chatbot's ability to provide more accurate and business-specific answers.

The system is designed to allow businesses to integrate a customizable chatbot that can be trained on their data, handle various types of queries, and generate responses based on business-specific context. The chatbot is multilingual, supports both cloud and on-premise deployments, and offers analytics to businesses.


## Features

- **Multilingual Support**: The chatbot supports both English and Arabic.
- **LLM Integration**: It can utilize pre-trained language models for generating responses natural responses.
- **Customizable Data**: Businesses can upload their own data, in different formats, and the chatbot adapts to answer queries accordingly.
- **Response Analytics**: Provides analytics about user queries, frequently asked questions, and suggestions for improvement.
- **Service Architecture**: The system is built with a modular architecture, including services for data processing, database management, and chatbot interaction.

## Architecture

The project follows the **MVC (Model-View-Controller)** design pattern:

- **Model**: 
  - Contains the logic for interacting with the chatbot model (using transformers for NLP tasks).
  - Includes the `Chatbot` model, which handles communication with language models.
  
- **View**:
  - The front-end (UI) component which interacts with the user. This could be a mobile app or web app (not included in this repo as it will be a SaaS that clients integrate to their services).
  
- **Service**:
  - The `BackendService`, `ChatbotService` and DataProcessingService are responsible for managing user input, invoking the appropriate services, and processing responses.

- **Controller**:
  - The `BackendService` and `ChatbotService` are responsible for managing user input, invoking the appropriate services, and processing responses.
  
  
### Service Layer:

- **BackendService**: Manages interactions between the chatbot service, data processing service, and database.
- **ChatbotService**: Handles interactions with the chatbot model for generating responses.
- **DataProcessingService**: Processes incoming user queries, including data fetching and searching relevant information.
- **DatabaseService**: Manages the database, creating tables, storing, and fetching data for the chatbot.
