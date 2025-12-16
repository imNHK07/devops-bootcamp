# 1. Start with a base OS that has Python installed.
# We use 'slim' to keep the image small and secure.
FROM python:3.9-slim

# 2. Set the working directory inside the container.
# This is like doing 'cd /app' inside the container.
WORKDIR /app

# 3. Copy our script from the host (your PC) to the container.
# Format: COPY [source] [destination]

COPY log_analyzer.py .

# 4. (Optional) If we had external libraries, we would install them here.
# RUN pip install requests

# 5. Define the command that runs when the container starts.
ENTRYPOINT ["python", "log_analyzer.py"]
