# JARVIS API Documentation

## Module Interfaces

### Core (`src.core`)
- `startup.initialize_system()`: Set up files, check dependencies, and verify configurations.

### AI (`src.ai`)
- `ollama_client.generate_response(prompt)`: Interact with local LLM.
- `planner.plan_action(goal)`: Formulate plan steps.

### Browser (`src.browser`)
- `browser_controller.open_page(url)`: Initialize and navigate.
- `screenshot.take_screenshot()`: Capture UI elements.

### Voice (`src.voice`)
- `speech_to_text.listen()`: Convert mic input to text string.
- `text_to_speech.speak(text)`: Convert string text to audio.
