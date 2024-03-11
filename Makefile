poetry_install:
	poetry install

fix_langchain_hf_bug:
	sed -i 's/llm: Union\[HuggingFaceTextGenInference, HuggingFaceEndpoint, HuggingFaceHub\]/llm: Union[HuggingFaceEndpoint, HuggingFaceTextGenInference, HuggingFaceHub]/g' .venv/Lib/site-packages/langchain_community/chat_models/huggingface.py

.PHONY: setup
setup: poetry_install fix_langchain_hf_bug

.PHONY: api
api:
	poetry run python app.py

.PHONY: ui
ui:
	poetry run streamlit run ui.py