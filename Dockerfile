# Use the official Python image as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /apps

# Copy the current directory contents into the container at /app
COPY . /apps

# Install dependencies
RUN pip install --no-cache-dir streamlit pyperclip

# Expose the port where Streamlit will run
EXPOSE 8502

# Run the Streamlit app
CMD ["streamlit", "run", "apps/apps.py", "--server.port", "8502"]
