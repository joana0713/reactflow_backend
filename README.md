# 🧩 Pipeline Builder

A drag-and-drop visual pipeline builder built with React and React Flow.

This project demonstrates dynamic node rendering, configurable node types, and a scalable UI architecture using Tailwind CSS.

---

## 🚀 Features

- Drag & Drop node creation
- Dynamic input/output handles
- Config-driven generic nodes
- Specialized nodes (Input, Output, LLM, Text)
- Variable extraction from TextNode (`{{variable}}`)
- Sidebar-based node palette
- Fully styled with Tailwind CSS (no inline design styles)

---

## 🧠 Technical Highlights

- Zustand for state management
- React Flow for graph rendering
- Dynamic handle positioning
- Config-driven UI rendering
- Modular node architecture

---

## 📝 Notes

This project focuses on:
- Clean architecture
- UI consistency
- Extensibility
- Maintainable node configuration structure

---

## 📌 Future Improvements

- Node color themes
- Node duplication & deletion controls
- Save / Load pipeline
- Backend execution engine

---

Built for assignment submission.

## Backend Setup

Start the backend server on port 8000:

```bash
uvicorn main:app --reload --port 8000
```

The frontend sends requests to:

POST /pipelines/parse

Make sure the backend is running before testing the Parse functionality.