# CrewAI_Agentic-AI

## Overview

This project uses CrewAI agents to research and generate blog content about how generative AI is transforming the medical industry. It features a Streamlit web interface for interactive exploration.

## Features

- Automated research and content generation using CrewAI agents
- Integration with Serper search tool for up-to-date information
- Streamlit UI for easy topic input and result display

## Requirements

- Python 3.8+
- [OpenAI API access](https://platform.openai.com/)
- [Serper API key](https://serper.dev/)
- The following Python packages:
  - streamlit
  - python-dotenv
  - crewai
  - crewai-tools

> **Note:** If your LLM setup (e.g., OpenAI) requires an API key, add `OPENAI_API_KEY=your_openai_api_key_here` to your `.env` file as well.

## Setup

1. **Clone the repository:**
   ```
   git clone <your-repo-url>
   cd CrewAI_Agentic-AI
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
   Or manually:
   ```
   pip install streamlit python-dotenv crewai crewai-tools
   ```

3. **Set up environment variables:**
   - Create a `.env` file in the project root:
     ```
     SERPER_API_KEY=your_serper_api_key_here
     OPENAI_API_KEY=your_openai_api_key_here  # If required by your LLM.
     ```

## Usage

### Run the Streamlit App

```
streamlit run streamit_app.py
```

- Enter a research topic or use the default.
- Click "Run Research" to generate a blog post.

### Run the Script Directly

You can also run `app.py` for a command-line version:
```
python app.py
```

## Troubleshooting

- **Missing API Key:**  
  Ensure your `.env` file contains valid `SERPER_API_KEY` (and `OPENAI_API_KEY` if needed).
- **Module Not Found:**  
  Double-check that all required packages are installed.
- **Streamlit Not Launching:**  
  Make sure you are running the command in the correct directory.

## File Structure

- `app.py` - Main script for CrewAI workflow
- `streamit_app.py` - Streamlit web interface
- `.env` - Environment variables (not included in repo)
- `README.md` - Project documentation

## License

MIT License

## Acknowledgments

- [CrewAI](https://github.com/joaomdmoura/crewai)
- [Serper](https://serper.dev/)
- [Streamlit](https://streamlit.io/)