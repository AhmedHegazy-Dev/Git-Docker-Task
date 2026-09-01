# Git-Docker-Task

## Why Certain Files Should Not Be Committed to Git

- **Generated Files (e.g., cache, build artifacts, processed outputs):** They are redundant, can be easily reproduced by running the code, and cause repository bloat and unnecessary merge conflicts.
- **Virtual Environments (e.g., `.venv/`):** They are platform-specific (tied to local OS/paths), extremely large, and non-portable. Instead, commit dependency files like `requirements.txt`.
- **Secrets (e.g., API keys, passwords, `.env`):** Exposing credentials is a critical security vulnerability. Git history is permanent, making leaked secrets hard to erase.
- **Raw/Private Datasets:** Violates data privacy/compliance rules (e.g., GDPR) and bloats the repository. Large data should be stored in dedicated storage (e.g., S3, DVC) rather than Git.

## Differences Between Dockerfile, Image, and Container

| Concept | What It Is | Analogy | Key Characteristics |
| :--- | :--- | :--- | :--- |
| **Dockerfile** | A text file with build instructions | The **Recipe / Blueprint** | Human-readable configuration script specifying the base image, environment variables, commands to install packages, and startup commands (`docker build`). |
| **Image** | An immutable, standalone package | The **Cake / Class** | A compiled, read-only snapshot containing the OS filesystem, dependencies, and code needed to run the app. Built from a Dockerfile. |
| **Container** | A live, running instance of an image | An **Instance / Object** | An isolated runtime process executing the image with an added thin writable layer on top (`docker run`). Multiple containers can run from a single image. |
