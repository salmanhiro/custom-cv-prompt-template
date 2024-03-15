# Use the official Python image as a parent image
FROM python:3.9-slim

# Update the package lists and install the required packages in one RUN command to keep the image size small
RUN apt-get update && apt-get install -y \
    xclip \
    xvfb

# Set the working directory in the container
WORKDIR /apps

# Copy the current directory contents into the container at /app
COPY . /apps

# Install dependencies
RUN pip install --no-cache-dir streamlit

# Expose the port where Streamlit will run
EXPOSE 8502

# Run the Streamlit app
CMD ["streamlit", "run", "apps/apps.py", "--server.port", "8502"]
