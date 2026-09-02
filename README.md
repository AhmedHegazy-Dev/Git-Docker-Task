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

## Why Docker Volumes/Mounts Are Useful for Data Engineering Pipelines

In data engineering pipelines, Docker volumes and bind mounts (e.g., `-v "${PWD}/data:/app/data"`) are essential for several key reasons:

1. **Data Persistence Across Ephemeral Containers:**
   Containers are temporary and stateless by design. When a container finishes processing and is removed (`--rm`), any files created inside its writable layer are destroyed. Mounting a volume ensures that processed results (e.g., `processed_sales.txt`, parquet files, database exports) are safely persisted to the host machine or cloud storage.

2. **Decoupling Code from Data:**
   In data engineering, datasets update constantly (daily batch files, streaming intervals), while the processing logic changes less frequently. Volumes allow pipelines to ingest new datasets dynamically without needing to rebuild the Docker image (`docker build`) every time new data arrives.

3. **Bidirectional Input/Output (I/O) Sharing:**
   Mounts allow the container to:
   - **Read** raw incoming data directly from the host or network storage.
   - **Write** transformed, cleaned, or aggregated data back to the host for downstream consumption by BI dashboards, databases, or next-stage pipelines.

4. **Keeping Docker Images Lightweight and Fast:**
   Baking gigabytes or terabytes of data directly into a Docker image bloats image size, slows down image transfer across container registries, and wastes storage. Using volume mounts keeps images lightweight, portable, and fast to deploy.

5. **Security and Data Privacy:**
   Data pipelines often handle sensitive, confidential, or compliance-restricted data (e.g., GDPR, HIPAA). By mounting data at runtime rather than copying it during the build step, sensitive data is never permanently baked into the image layers or pushed to public/private registries.
