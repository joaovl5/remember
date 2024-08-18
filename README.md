# Remember

This is a work-in-progress project aiming to provide an overhaul to knowledge-base management by implementing several RAG-based techniques. For it's first version, my aim is for these core features:

- **Recurring Snapshot Taking** - periodically takes snapshots of user's activity on computer for storage in knowledge system for later retrieval
- **Multimodal Document Indexing** - allowing the user to attach several files, ranging from images to PDF documents, for storage in knowledge system for later retrieval

## Roadmap

- [ ] Testing and switching function for different RAG back-ends
- [ ] Testing and switching function for different LLM back-ends, both on-device and through APIs
- [ ] Obsidian Integration for connecting graphs

## Development

You could help the development of this project by following these steps.
**These steps are temporary!** Keep in mind this project is still in its early stages and this process will be made better once I have the time.

1. Clone the repository
2. `pip install -r requirements.txt`
3. Go to ./front and run `npm install`
4. On a separate terminal, keep `npm run dev` open, note the port number for editing in step 5.
5. Navigate to `gui/init.py` and change the port number accordingly.

```python
    return "http://localhost:9002/" # Change the port here!
```

6. You can now run `python init.py`
