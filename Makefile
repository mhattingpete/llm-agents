poetry_install:
	poetry install

fix_langchain_hf_bug:
	sed -i 's/llm: Union\[HuggingFaceTextGenInference, HuggingFaceEndpoint, HuggingFaceHub\]/llm: Union[HuggingFaceEndpoint, HuggingFaceTextGenInference, HuggingFaceHub]/g' .venv/Lib/site-packages/langchain_community/chat_models/huggingface.py

.PHONY: setup
setup: poetry_install fix_langchain_hf_bug

.PHONY: install
install: setup

.PHONY: api
api:
	poetry run python app.py

.PHONY: ui
ui:
	poetry run streamlit run ui.py

.PHONY: docs
docs:
	@echo -e "\033[36m Generate documentation to docs...  \e[0m"
	poetry run pdoc --template-directory ./docs_templates --output-dir ./docs ./src

.PHONY: test
test:
	poetry run pytest --html=docs/test_python_functions.html --self-contained-html #--css=pyproject/src/testing/stylesheet.css