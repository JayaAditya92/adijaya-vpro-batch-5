# MASTER PROMPT: Build a Complete Adaptive RAG Application from Scratch

## 1. Role and objective

Act as a Senior AI Engineer, Python Backend Architect, React/TypeScript Engineer, and QA Engineer.

Build a complete, modular, professional Adaptive Retrieval-Augmented Generation (Adaptive RAG) application from scratch.

The application must be functional, maintainable, secure by default, responsive, and validated before you declare completion.

Do not merely provide instructions, pseudo-code, sample snippets, or a partial implementation. Create the actual project files, implement the application, run the available checks, identify failures, and fix them.

Do not claim that the application works unless you have actually verified the relevant checks.

## 2. Exact project location

Create the project inside this existing repository:

`C:\Users\desktop\batch-5\adijaya-vpro-batch-5\RAGS\adaptive`

Rules:

1. Inspect the current repository and development environment first.
2. Confirm that the target path is correct before writing files.
3. Preserve all unrelated existing files.
4. Never overwrite existing user work without inspection and an explicit reason.
5. Create all application files inside the `adaptive` directory.
6. Use Windows-compatible commands and paths.
7. Detect installed Python, Node.js, npm, and Git versions before selecting compatible dependencies.
8. If the target directory already contains files, inspect them and reuse appropriate components instead of blindly replacing them.

## 3. Required technology stack

### Backend
- Python 3.11 or another compatible, installed Python version.
- FastAPI.
- Uvicorn.
- Pydantic and Pydantic Settings.
- Official OpenAI Python SDK.
- ChromaDB with persistent local storage.
- Sentence Transformers for local text embeddings.
- Pytest and HTTPX for testing.

### Frontend
- React.
- TypeScript.
- Vite.
- React Router only if multiple routes require it.
- A consistent component and styling system using CSS or a suitable UI library.
- Responsive layouts for desktop, tablet, and mobile.
- Lucide React icons or another maintained icon library.

Use compatible, maintained dependency versions. Avoid unnecessary dependencies and do not mix incompatible major versions.

Use npm for the frontend unless the existing repository has a justified package-manager convention.

## 4. Adaptive RAG functionality

Implement a genuine adaptive RAG pipeline with clearly separated, testable modules.

Required processing flow:

1. Receive a user query.
2. Validate and normalize the query.
3. Analyze the query and decide whether document retrieval is necessary.
4. Route appropriate queries to direct generation or retrieval.
5. When retrieval is needed, search the ChromaDB collection.
6. Evaluate the relevance and adequacy of retrieved chunks.
7. Rewrite the query and retry retrieval when justified.
8. Apply a configurable maximum retrieval-attempt limit.
9. Generate an answer grounded in the retrieved evidence.
10. Return source citations, processing metadata, and an explicit retrieval outcome.
11. Abstain or request clarification when the available evidence is insufficient.
12. Return useful error messages without exposing secrets or internal stack traces.

The adaptive decisions must be implemented in application code, not merely described in comments.

### Required modules

- Query analyzer and router.
- Document ingestion pipeline.
- Text normalization and chunking.
- Embedding provider.
- ChromaDB vector-store adapter.
- Retriever.
- Retrieval relevance evaluator.
- Query rewriting service.
- Answer-generation service.
- Source citation formatter.
- Adaptive RAG orchestrator.
- Configuration and dependency management.
- API schemas and exception handling.

Keep these modules independently testable.

### Retrieval rules

- Use Sentence Transformers for local embeddings.
- Make the embedding model configurable through environment variables.
- Ensure document and query embeddings use the same model and compatible dimensions.
- Persist the ChromaDB collection across application restarts.
- Use stable document and chunk identifiers.
- Avoid inserting duplicate chunks when a document is reprocessed.
- Preserve document names, chunk identifiers, and useful metadata.
- Use configurable chunk size, overlap, retrieval top-k, and relevance thresholds.
- Limit query rewriting and retrieval retries.
- Never fabricate source citations.
- Clearly distinguish retrieved evidence from model-generated interpretation.
- Handle empty collections and missing documents gracefully.

Do not make external search or web retrieval mandatory for the first version.

## 5. OpenAI integration

Use the official OpenAI Python SDK.

Configuration must come from environment variables:

- OPENAI_API_KEY
- OPENAI_MODEL
- EMBEDDING_MODEL
- CHROMA_PERSIST_DIRECTORY
- CHROMA_COLLECTION_NAME
- API_HOST
- API_PORT
- FRONTEND_ORIGIN
- LOG_LEVEL

Add suitable settings for chunk size, chunk overlap, retrieval top-k, similarity threshold, and maximum retrieval attempts.

Use a current, supported OpenAI model configured by OPENAI_MODEL. Do not hardcode a model name throughout the codebase.

Important rules:

1. Never hardcode API keys or credentials.
2. Never commit `.env` files containing secrets.
3. Provide `.env.example` with placeholder values only.
4. Validate required configuration during application startup.
5. Never print API keys in logs or API responses.
6. Handle API authentication errors, rate limits, timeouts, and service failures.
7. Use bounded retries where appropriate.
8. Do not retry indefinitely.
9. Keep API calls and business logic in service modules.
10. Make error messages actionable without exposing sensitive information.

Do not call OpenAI for embedding generation if the selected embedding configuration is explicitly using local Sentence Transformers.

## 6. Sample documents

Create useful, original sample documents inside:

`backend/data/sample_documents/`

Include at least these documents:

- `adaptive_rag_overview.md`
- `openai_integration_guide.md`
- `chromadb_operations.md`
- `api_reference.md`
- `deployment_guide.md`

Write meaningful content, not empty placeholders.

The sample documents should describe the application's actual architecture, configuration, API endpoints, ingestion procedure, retrieval workflow, and troubleshooting steps.

Create an ingestion command that indexes these documents into ChromaDB.

Provide a safe way to re-ingest changed files without duplicating existing chunks.

The application must explain how to load sample documents on first startup. Avoid silently making expensive embedding or API calls during module imports.

## 7. Required directory structure

Create a clean modular structure similar to the following. Adjust only where necessary to preserve a simpler, well-justified architecture.

adaptive/
├── README.md
├── .gitignore
├── .env.example
├── pyproject.toml
├── package.json
├── run.ps1
├── stop.ps1
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── logging.py
│   │   │   └── exceptions.py
│   │   ├── api/
│   │   │   ├── router.py
│   │   │   └── routes/
│   │   │       ├── health.py
│   │   │       ├── chat.py
│   │   │       ├── documents.py
│   │   │       └── diagnostics.py
│   │   ├── schemas/
│   │   │   ├── chat.py
│   │   │   ├── documents.py
│   │   │   └── common.py
│   │   ├── rag/
│   │   │   ├── orchestrator.py
│   │   │   ├── query_analyzer.py
│   │   │   ├── router.py
│   │   │   ├── chunker.py
│   │   │   ├── evaluator.py
│   │   │   ├── query_rewriter.py
│   │   │   └── citations.py
│   │   ├── services/
│   │   │   ├── chat_service.py
│   │   │   ├── document_service.py
│   │   │   └── answer_service.py
│   │   ├── providers/
│   │   │   ├── openai_provider.py
│   │   │   └── embedding_provider.py
│   │   ├── vectorstores/
│   │   │   └── chroma_store.py
│   │   └── dependencies.py
│   ├── data/
│   │   └── sample_documents/
│   ├── scripts/
│   │   └── ingest_samples.py
│   └── tests/
│       ├── conftest.py
│       ├── test_health.py
│       ├── test_chat.py
│       ├── test_chunker.py
│       ├── test_router.py
│       ├── test_retrieval.py
│       ├── test_citations.py
│       └── test_orchestrator.py
└── frontend/
    ├── package.json
    ├── index.html
    ├── public/
    │   └── brand/
    │       └── pro-skills-logo.png
    └── src/
        ├── main.tsx
        ├── App.tsx
        ├── api/
        │   ├── client.ts
        │   └── types.ts
        ├── components/
        │   ├── layout/
        │   ├── chat/
        │   ├── documents/
        │   └── common/
        ├── pages/
        │   ├── DashboardPage.tsx
        │   ├── ChatPage.tsx
        │   ├── DocumentsPage.tsx
        │   └── SettingsPage.tsx
        ├── hooks/
        ├── styles/
        └── utils/

Do not create empty modules or unused files just to match this tree. Every file must serve a real purpose. Add only essential configuration files and test utilities.

Keep the root package.json focused on orchestrating the frontend and backend commands, not duplicating dependencies.

## 8. Pro Skills branding and logo

Use the Pro Skills logo supplied by the user.

The supplied image is a logo featuring an orange symbol and orange "Pro" text with black "SKILLS" lettering.

Locate the actual uploaded image file if it is available in the working environment. Copy the original image to:

`frontend/public/brand/pro-skills-logo.png`

If the source file is unavailable, ask the user for its local path. Do not fabricate the original logo, substitute an unrelated logo, or claim that the logo was copied if it was not.

Display the logo prominently in the application sidebar/header and on the login or welcome area if one exists.

Requirements:

- Preserve the original aspect ratio.
- Use an accessible alt attribute.
- Avoid stretching or cropping the logo.
- Ensure it remains visible on desktop and mobile.
- Use the Pro Skills orange and charcoal colors as the primary branding inspiration.

## 9. Frontend requirements

Create a polished AI document-assistant dashboard.

### Main layout

- Responsive sidebar with Pro Skills logo.
- Application title: Adaptive RAG Studio.
- Navigation for Dashboard, Chat, Documents, and Settings.
- Main workspace with a clear page hierarchy.
- Responsive sidebar behavior on smaller screens.
- Consistent spacing, typography, colors, borders, and shadows.
- Accessible focus states and keyboard navigation.

### Dashboard

Show actual backend-derived information where available:

- Backend health.
- Vector-store status.
- Number of indexed documents.
- Number of indexed chunks, if reliably available.
- Configured retrieval settings.
- Recent query activity, if persisted.
- Helpful first-run instructions when the vector store is empty.

Do not invent metrics or display fake production statistics.

### Chat interface

Implement:

- A clean conversation layout.
- User and assistant message styling.
- A multiline question input.
- Enter to submit and Shift+Enter for a new line.
- Loading and disabled states.
- Error and retry states.
- Answer formatting.
- Clickable source references that display document name and relevant chunk information.
- Retrieval diagnostics showing the selected route, retrieval attempts, and relevant scores when available.
- An explanation when retrieval is skipped or evidence is insufficient.
- A clear conversation reset action.

Do not expose private prompts, API keys, raw stack traces, or sensitive backend configuration.

### Documents page

Implement:

- Upload supported text and Markdown documents.
- List indexed documents.
- Display ingestion status.
- Show ingestion errors.
- Provide an explicit re-index action when supported.
- Confirm before destructive deletion.
- Handle empty states and large filenames gracefully.

Support `.txt` and `.md` initially. Add PDF or DOCX only if their dependencies and parsing behavior are implemented and tested properly.

### Settings page

Display safe configuration information, including:

- Selected model name.
- Embedding model.
- Retrieval top-k.
- Chunk size and overlap.
- Relevance threshold.
- Maximum retry attempts.
- API connectivity and vector-store health.

Do not display secrets. Clearly distinguish read-only settings from settings that can actually be changed and persisted.

### Styling

- Use a professional light theme by default.
- Use orange accents inspired by the supplied logo.
- Use readable typography and consistent design tokens.
- Use responsive CSS layouts, not fixed desktop-only widths.
- Support common desktop, tablet, and mobile viewport sizes.
- Include accessible labels, semantic HTML, visible focus indicators, and sufficient contrast.
- Avoid excessive gradients, unnecessary animations, clutter, and decorative elements that interfere with usability.

Do not use fake buttons, placeholder navigation, or nonfunctional UI controls.

## 10. API requirements

Implement and document the following endpoints:

- `GET /api/health`
- `GET /api/health/ready`
- `POST /api/chat`
- `GET /api/documents`
- `POST /api/documents/upload`
- `POST /api/documents/ingest-samples`
- `POST /api/documents/{document_id}/reindex`
- `DELETE /api/documents/{document_id}`
- `GET /api/diagnostics`

Use appropriate HTTP status codes, request validation, response schemas, and error handling.

Avoid adding redundant endpoints. If a proposed endpoint is not needed, document the reason for omitting it.

Use FastAPI's generated OpenAPI documentation.

Configure CORS for the intended local frontend origin only. Do not use unrestricted CORS in the default configuration.

Validate uploaded file types and sizes. Use safe filenames, avoid path traversal, and prevent arbitrary filesystem access.

Do not expose local filesystem paths or secrets through public API responses.

## 11. Security and reliability

- Load configuration using typed settings.
- Provide safe `.gitignore` rules for `.env`, Python caches, virtual environments, `node_modules`, build output, and local vector-store data.
- Never remove existing Git history or rewrite unrelated branches.
- Never commit real secrets.
- Use dependency injection where it improves testability.
- Avoid circular imports.
- Avoid global mutable application state.
- Use application lifespan management for shared resources.
- Close resources correctly on shutdown.
- Use explicit timeouts for external API calls.
- Validate incoming request sizes and document uploads.
- Limit query length and retrieval attempts.
- Handle empty input and malformed requests.
- Add structured, useful logging without leaking sensitive data.
- Avoid suppressing exceptions without handling them.
- Avoid broad `except Exception` blocks unless they are used at a proper application boundary with safe logging and error translation.
- Never fabricate successful API responses when a service is unavailable.

Use deterministic unit tests with mocks wherever possible so the test suite does not require a real OpenAI API key.

## 12. Testing requirements

Create meaningful tests for:

- Application startup and health endpoints.
- Configuration validation.
- Query routing.
- Direct-answer versus retrieval decisions.
- Document chunking and overlap.
- Empty and malformed documents.
- ChromaDB persistence and retrieval behavior.
- Duplicate-ingestion prevention.
- Relevance evaluation.
- Query rewrite retry limits.
- Insufficient-evidence behavior.
- Citation correctness.
- API validation and error responses.
- File-upload validation.
- Chat orchestration.
- Frontend TypeScript compilation.
- Frontend production build.

Mock external OpenAI calls for unit tests.

Add integration tests for local ChromaDB behavior where practical.

If a test requires unavailable external credentials, distinguish it clearly from the offline test suite. Never mark an unexecuted test as passed.

## 13. One-command Windows startup

Create a PowerShell script named `run.ps1` in the project root.

The intended user experience is:

1. Open PowerShell.
2. Navigate to the `adaptive` directory.
3. Run `.\run.ps1`.
4. Follow clear first-run setup instructions if configuration or dependencies are missing.
5. Start the backend and frontend.
6. Open the local React application in the browser.

The script should:

- Check required tools before starting.
- Validate the working directory.
- Create a Python virtual environment if necessary.
- Install dependencies using the project's pinned or constrained dependency definitions.
- Install frontend dependencies only when necessary.
- Check `.env` existence and explain how to configure it.
- Never invent or insert a real API key.
- Start the backend and frontend as separate managed processes.
- Print the actual local URLs.
- Detect startup failures and provide useful diagnostics.
- Avoid starting duplicate processes unnecessarily.
- Handle Ctrl+C and child-process cleanup where feasible.
- Avoid silently overwriting environment files.
- Avoid running destructive cleanup commands.

If the OpenAI API key is missing, explain exactly how to configure it and stop before starting API-dependent functionality. Offline tests and setup validation should remain possible without a key.

Create `stop.ps1` only if it can safely identify and stop the processes started by this project without terminating unrelated processes.

Provide a reliable alternative for developers who prefer to run the backend and frontend in separate terminals.

A single startup command is the goal, but do not promise a one-click setup if prerequisites or network access are unavailable.

## 14. Root README.md

Write a complete, beginner-friendly README that covers:

1. Application overview.
2. Architecture and Adaptive RAG workflow.
3. Full directory structure.
4. Prerequisites and compatible versions.
5. Initial setup.
6. Environment configuration.
7. OpenAI API key setup.
8. Local Sentence Transformers model setup.
9. ChromaDB persistence.
10. Sample document ingestion.
11. One-command startup.
12. Separate-terminal startup.
13. API endpoints.
14. Swagger/OpenAPI documentation.
15. How to run tests.
16. How to troubleshoot common errors.
17. How to change the LLM or embedding model.
18. How to add new document formats safely.
19. How to stop the application.
20. Known limitations and next steps.

Provide exact Windows PowerShell commands. Do not include commands that assume the user is in a different directory.

## 15. Implementation process

Follow this sequence.

### Phase 1: Inspect

- Inspect the repository and target directory.
- Check available runtimes and package managers.
- Check whether the supplied logo is accessible.
- Identify existing files that must be preserved.
- Report blockers before proceeding when they require user input.

### Phase 2: Design

- Finalize the architecture.
- Define request and response schemas.
- Define module responsibilities.
- Define the adaptive routing and retry policy.
- Define configuration defaults and validation.
- Define source-citation format.
- Keep the implementation minimal but complete.

### Phase 3: Implement

- Create the backend and frontend.
- Create all required source files.
- Create sample documents.
- Implement ingestion and persistent vector storage.
- Implement the adaptive pipeline.
- Build the React UI.
- Integrate the supplied logo.
- Add the root startup and shutdown scripts.
- Write setup and troubleshooting documentation.

### Phase 4: Validate

Run the available checks, including:

- Python syntax and import checks.
- Backend unit tests.
- API tests.
- Dependency consistency checks where available.
- Frontend TypeScript checks.
- Frontend production build.
- Startup-script validation.
- A local backend health check.
- A basic frontend accessibility and responsive-layout review.

Run actual end-to-end API tests with a real OpenAI key only when one is safely configured and network access is available.

### Phase 5: Fix

For each failure:

1. Identify the root cause.
2. Fix the actual source.
3. Re-run the failed check.
4. Re-run relevant regression tests.
5. Verify that the fix did not break other modules.

Do not add duplicate implementations to work around a problem. Do not suppress errors simply to achieve a green test result.

### Phase 6: Final report

Report:

- Final project path.
- Implemented architecture.
- Actual directory structure.
- Files created.
- Logo integration status.
- Commands executed.
- Tests that passed.
- Tests that failed or could not be executed.
- Whether an OpenAI API key is still required.
- Exact commands to start and stop the application.
- Actual local URLs if the services were successfully started.
- Remaining limitations.

## 16. Strict engineering rules

- No unnecessary code.
- No duplicate services or overlapping abstractions.
- No speculative dependencies.
- No dead code.
- No empty placeholder modules.
- No hardcoded credentials.
- No fabricated test results.
- No fake UI metrics.
- No unbounded retries.
- No unnecessary background services.
- No Docker requirement for the first local version.
- No unnecessary microservices.
- No premature abstraction.
- No unsupported claims about production readiness.
- No destructive Git operations.
- No replacing working files without inspection.
- No incomplete snippets presented as a completed application.

Prefer clear, typed, readable code over clever implementations.

Make reasonable engineering decisions independently when requirements are sufficiently clear. Ask a concise question only when an essential input is genuinely unavailable or a decision could risk existing user data.

## Definition of done

The application is complete only when:

1. The files exist in the requested directory.
2. The backend and frontend dependencies are defined.
3. The application starts using the documented workflow, subject to required external configuration.
4. The React application displays the actual supplied Pro Skills logo.
5. The chat API implements adaptive routing and retrieval.
6. ChromaDB stores and retrieves indexed sample documents.
7. Answers include valid source references when retrieved evidence supports them.
8. Insufficient evidence is handled honestly.
9. The frontend builds successfully.
10. The automated tests have been executed and their real results reported.
11. The README explains setup and troubleshooting.
12. All unresolved issues are explicitly disclosed.

Begin with Phase 1. Inspect the actual environment before writing code. Then continue through implementation, validation, and repair without stopping after merely generating a plan.