# DuplexFlow AI 🚀

Real-Time Full-Duplex Voice Agent & FDB-v3 Benchmark Suite for Samsung PRISM Gen AI

# 📌 Overview
DuplexFlow AI is a cutting-edge, full-stack conversational AI platform built for real-time, bidirectional voice interactions. Powered by LiveKit Agents and the Google Gemini Realtime API, DuplexFlow features ultra-low latency audio processing, multi-domain tool execution (Travel, Banking, Real Estate, E-Commerce), and live telemetry tracking aligned with the FDB-v3 benchmark suite.

#🏗️ Architecture & Tech Stack
Backend & Agent Worker: Python, FastAPI, LiveKit Agents, Google GenAI SDK (gemini-2.5-flash), WebSockets, Subprocess Lifespan Management.

Frontend: Next.js (Turbopack), React, Tailwind CSS, LiveKit WebRTC Client, Recharts, Lucide Icons.

Real-Time Communication: WebRTC via LiveKit Cloud (India South region protocol).

Evaluation Framework: FDB-v3 (Full-Duplex Benchmark) tracking reasoning latency, tool invocation accuracy, and conversational state rollbacks.

#🛠️ Multi-Domain Tool Registry
The AI agent is equipped with robust multi-step tool execution capabilities spanning several domains:

Travel & Flights: search_flights, book_flight

Identity & Security: update_identity_doc

Banking & Finance: get_card_benefits, get_exchange_rate, modify_autopay

Real Estate & Commute: search_apartments, calculate_commute, update_search_filter

E-Commerce & Retail: track_order, search_products, add_to_cart

# 🚀 Quick Start Guide
1. Backend Setup (duplex-flow-backend)
Bash

Clone and navigate to backend
cd duplex-flow-backend

Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows

Install dependencies
pip install -r requirements.txt

Configure environment variables (.env)
LIVEKIT_URL=wss://your-livekit-url
LIVEKIT_API_KEY=your_api_key
LIVEKIT_API_SECRET=your_api_secret
GOOGLE_API_KEY=your_gemini_api_key

Run FastAPI server (automatically launches LiveKit agent worker via lifespan)
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
2. Frontend Setup (duplex-flow-frontend)
Bash

# Navigate to frontend directory
cd duplex-flow-frontend

# Install dependencies
npm install

# Run development server
npm run dev
Open http://localhost:3000 in your browser to launch the Live Studio and Telemetry Dashboard.

# 📡 Core API Endpoints
GET /api/token — Generates secure LiveKit WebRTC access tokens for active voice sessions.

GET /api/live-logs?room=<room_id> — Streams real-time tool execution logs and transcripts for the Live Tool Inspector (IPC).

GET /api/benchmark — Serves aggregate FDB-v3 evaluation pass rates and domain performance breakdowns.
