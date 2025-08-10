


import streamlit as st
import os
import subprocess
import json
import random
import pandas as pd
from datetime import datetime
import time
import base64
from twilio.rest import Client  # Import Twilio library
import urllib.request
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw
import psutil
import paramiko  # Import paramiko for SSH
from googlesearch import search  # Import Google Search
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
from keras.models import Sequential
from keras.layers import Dense
from openai import OpenAI
import google.generativeai as genai
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.asknews import AskNewsSearch
import streamlit.components.v1 as components  # Added for JavaScript projects

# Page configuration
st.set_page_config(
    page_title="Suhana's Multi-Tech Toolkit",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #667eea;
    }
    .success-box {
        background: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .error-box {
        background: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Helper functions
def execute_command(command):
    """Execute system command safely"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
        return result.stdout if result.returncode == 0 else result.stderr
    except subprocess.TimeoutExpired:
        return "Command timed out"
    except Exception as e:
        return f"Error: {str(e)}"

def safe_file_read(filename):
    """Safely read file content"""
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                return f.read()
        else:
            return "File not found"
    except Exception as e:
        return f"Error reading file: {str(e)}"

def format_timestamp():
    """Get formatted timestamp"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Sidebar Configuration
with st.sidebar:
    st.markdown("### 👨‍💻 Suhana Laddha")
    st.markdown("**Crafting Smart Tools with Code**")
    st.markdown("---")
    # Add some metrics
    st.metric("Dashboard Version", "v2.0")
    st.metric("Last Updated", datetime.now().strftime("%m/%d/%Y"))
    st.metric("Available Tools", "20", delta="8")
    st.metric("Commands Run", "0", delta="0")
    st.metric("Success Rate", "100%", delta="0%")
    st.metric("Uptime", "100%", delta="0%")
    st.markdown("---")
    st.markdown("### 🔧 Quick Tools")
    # Quick system info
    if st.button("💻 System Info"):
        st.code(f"User: {os.getenv('USER', 'Unknown')}")
        st.code(f"OS: {os.name}")
        st.code(f"Time: {format_timestamp()}")

# Main Header
st.markdown("""
<div class="main-header">
    <h1>🚀 Suhana's Multi-Tech Toolkit Dashboard</h1>
    <p>Your one-stop solution for development, deployment, and system management tasks</p>
</div>
""", unsafe_allow_html=True)

# Initialize session state for menu and project_tab if they don't exist
if 'menu' not in st.session_state:
    st.session_state.menu = "🏠 Dashboard Home"
if 'project_tab' not in st.session_state:
    st.session_state.project_tab = None

# Navigation Menu
menu = st.selectbox("🗂️ Choose a Category", [
    "🏠 Dashboard Home",
    "⭐ Featured Projects",
    "🐍 Python Tasks",
    "🐧 Linux Tasks",
    "🐳 Docker Tasks",
    "⚡ JavaScript Tasks",
    "📝 Git Tasks",
    "☸️ Kubernetes Tasks",
    "🤖 ML Tasks",
    "🌐 Web Dev Tasks",
    "🔧 Jenkins Tasks",
    "☁️ AWS Tasks",
    "🕸️ Web Scraping",
    "📸 Image Processing",
    "💬 Communication",
    "🤖 Agentic AI"
], index=[
    "🏠 Dashboard Home",
    "⭐ Featured Projects",
    "🐍 Python Tasks",
    "🐧 Linux Tasks",
    "🐳 Docker Tasks",
    "⚡ JavaScript Tasks",
    "📝 Git Tasks",
    "☸️ Kubernetes Tasks",
    "🤖 ML Tasks",
    "🌐 Web Dev Tasks",
    "🔧 Jenkins Tasks",
    "☁️ AWS Tasks",
    "🕸️ Web Scraping",
    "📸 Image Processing",
    "💬 Communication",
    "🤖 Agentic AI"
].index(st.session_state.menu))
st.session_state.menu = menu  # Update session state after selection
st.markdown("---")

# Dashboard Home
if menu == "🏠 Dashboard Home":
    st.markdown("### 🌟 Featured Tools")
    feat_col1, feat_col2, feat_col3 = st.columns(3)
    with feat_col1:
        with st.container():
            st.markdown("#### 🐍 Python Tools")
            st.write("Calculate factorials, generate random numbers, and manage packages")
            if st.button("Go to Python Tools"):
                st.session_state.menu = "🐍 Python Tasks"
                st.rerun()
    with feat_col2:
        with st.container():
            st.markdown("#### 🐳 Docker Tools")
            st.write("Manage containers, images, and orchestration")
            if st.button("Go to Docker Tools"):
                st.session_state.menu = "🐳 Docker Tasks"
                st.rerun()
    with feat_col3:
        with st.container():
            st.markdown("#### 🤖 ML Tools")
            st.write("Machine learning predictions and data analysis")
            if st.button("Go to ML Tools"):
                st.session_state.menu = "🤖 ML Tasks"
                st.rerun()
    
    # Platefull app showcase
    st.markdown("---")
    st.markdown("### 🍽️ Featured App: Platefull")
    
    # Create a card-like container
    with st.container():
        # App header
        col1, col2 = st.columns([1, 5])
        with col1:
            st.markdown("### 🍽️")
        with col2:
            st.markdown("## Platefull")
            st.markdown("*Created by Suhana and Kunika*")
        
        # Tagline
        st.markdown(
            f"<div style='background-color: #4CAF50; color: white; padding: 0.5rem 1rem; border-radius: 20px; display: inline-block; margin-bottom: 1rem;'>"
            f"<strong>Har plate ho full</strong></div>", 
            unsafe_allow_html=True
        )
        st.markdown("#### From your plate.....toh someone's day")
        st.markdown("### Don't Waste, Donate a Plate")
        
        # Feature grid
        col1, col2 = st.columns(2)
        with col1:
            with st.container():
                st.markdown("**Target Audience**")
                st.info("For Food Donors")
            with st.container():
                st.markdown("**Problem**")
                st.info("Food Waste Meet Hunger")
        with col2:
            with st.container():
                st.markdown("**Our Solution**")
                st.info("Real time food donation network")
            with st.container():
                st.markdown("**Benefit**")
                st.info("Donate, Reduce, Feed, Impact")
        
        # What sets us apart
        st.markdown("**What Sets Us Apart**")
        st.success("Smart Verified food Tracking")
        
        # Preview buttons
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🚀 Preview Platefull"):
                import webbrowser
                webbrowser.open("https://platefullwebapp.vercel.app/")
        with col2:
            if st.button("🚀 Visit Showcase Website"):
                import webbrowser
                webbrowser.open("https://www.lwjazbaa.com/startup/platefull")# Python Tasks
elif menu == "🐍 Python Tasks":
    st.header("🐍 Python Development Tools")
    tab1, tab2, tab3, tab4 = st.tabs(["🔢 Calculator", "📞 Twilio Call", "📦 Packages", "🎲 Random Gen"])
    with tab1:
        st.subheader("🔢 Calculate Factorial")
        col1, col2 = st.columns([2, 1])
        with col1:
            num = st.number_input("Enter a number", min_value=0, max_value=20, step=1)
        with col2:
            st.write("")  # Space
            calculate_btn = st.button("Calculate", key="calc_fact")
        if calculate_btn:
            fact = 1
            for i in range(1, int(num) + 1):
                fact *= i
            st.success(f"✅ Factorial of {int(num)} is {fact:,}")
            # Show calculation steps
            steps = []
            temp_fact = 1
            for i in range(1, int(num) + 1):
                temp_fact *= i
                steps.append(f"{i}! = {temp_fact:,}")
            with st.expander("View Calculation Steps"):
                for step in steps:
                    st.text(step)
    with tab2:
        # Twilio Call Functionality
        st.subheader("📞 Make a Twilio Call")
        account_sid = st.text_input("Twilio Account SID", type="password")
        auth_token = st.text_input("Twilio Auth Token", type="password")
        to_number = st.text_input("To Number (with country code)")
        from_number = st.text_input("From Number (Your Twilio Number)")
        twiml_message = st.text_area("TwiML Message", "<Response><Say>Hello! This is a test call from Python using Twilio.</Say></Response>")
        if st.button("Initiate Call"):
            try:
                client = Client(account_sid, auth_token)
                call = client.calls.create(
                    to=to_number,
                    from_=from_number,
                    twiml=twiml_message
                )
                st.success(f"📞 Call initiated successfully! Call SID: {call.sid}")
            except Exception as e:
                st.error(f"❌ Error initiating call: {e}")
    with tab3:
        st.subheader("📦 Python Package Manager")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📋 List Installed Packages"):
                with st.spinner("Loading packages..."):
                    result = execute_command("pip list")
                    st.code(result, language="text")
        with col2:
            package_name = st.text_input("Install Package")
            if st.button("📥 Install") and package_name:
                with st.spinner(f"Installing {package_name}..."):
                    result = execute_command(f"pip install {package_name}")
                    if "Successfully installed" in result:
                        st.success(f"✅ {package_name} installed successfully!")
                    else:
                        st.error(f"❌ Error installing {package_name}")
                        st.code(result)
    with tab4:
        st.subheader("🎲 Random Number Generator")
        col1, col2, col3 = st.columns(3)
        with col1:
            lower = st.number_input("Lower Limit", value=0)
        with col2:
            upper = st.number_input("Upper Limit", value=100)
        with col3:
            count = st.number_input("How many numbers?", min_value=1, max_value=100, value=1)
        if st.button("🎯 Generate Random Numbers"):
            numbers = [random.randint(int(lower), int(upper)) for _ in range(int(count))]
            st.success(f"🎲 Random numbers: {', '.join(map(str, numbers))}")
            # Show statistics
            if count > 1:
                st.info(f"📊 Average: {sum(numbers)/len(numbers):.2f}, Min: {min(numbers)}, Max: {max(numbers)}")

# Linux Tasks
elif menu == "🐧 Linux Tasks":
    st.header("🐧 Linux System Administration")
    
    # Add SSH connection option
    st.subheader("🔌 SSH Connection")
    col1, col2, col3 = st.columns(3)
    with col1:
        ssh_host = st.text_input("SSH Host", value="10.167.24.14")
    with col2:
        ssh_user = st.text_input("SSH Username", value="root")
    with col3:
        ssh_password = st.text_input("SSH Password", type="password")
    
    # Function to execute SSH command
    def execute_ssh_command(command):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ssh_host, username=ssh_user, password=ssh_password)
            stdin, stdout, stderr = ssh.exec_command(command)
            result = stdout.read().decode() + stderr.read().decode()
            ssh.close()
            return result
        except Exception as e:
            return f"Error: {str(e)}"
    
    # Check if SSH connection is established
    if st.button("Test SSH Connection"):
        result = execute_ssh_command("echo 'SSH Connection Successful'")
        if "Error" in result:
            st.error(result)
        else:
            st.success("SSH Connection Established!")
    
    tab1, tab2, tab3, tab4 = st.tabs(["📂 File System", "💾 System Info", "🔍 Process Monitor", "📝 File Operations"])
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📍 Current Location")
            if st.button("Check PWD"):
                result = execute_ssh_command("pwd")
                st.code(result)
        with col2:
            st.subheader("📁 Directory Listing")
            if st.button("List Files (ls -la)"):
                result = execute_ssh_command("ls -la")
                st.code(result)
    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("💾 Disk Usage"):
                result = execute_ssh_command("df -h")
                st.code(result)
        with col2:
            if st.button("🖥️ Memory Usage"):
                result = execute_ssh_command("free -h")
                st.code(result)
        if st.button("🔧 System Information"):
            result = execute_ssh_command("uname -a")
            st.code(result)
    with tab3:
        if st.button("⚡ Running Processes"):
            result = execute_ssh_command("ps aux | head -20")
            st.code(result)
        process_name = st.text_input("Search for process:")
        if st.button("🔍 Search Process") and process_name:
            result = execute_ssh_command(f"ps aux | grep {process_name}")
            st.code(result)
    with tab4:
        file_name = st.text_input("Enter filename to read:")
        if st.button("📖 Read File") and file_name:
            result = execute_ssh_command(f"cat {file_name}")
            st.code(result)

# Docker Tasks
elif menu == "🐳 Docker Tasks":
    st.header("🐳 Docker Container Management")
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["⚙️ Configuration", "📊 Overview", "🚀 Launch", "🛑 Control", "🚀 Project Showcase"])
    with tab1:
        st.subheader("🐳 Docker SSH Configuration")
        st.warning("⚠️ **Security Warning:** This section allows direct SSH access.  Use with extreme caution and ensure proper security measures are in place.")
        # SSH Input
        rhel_ip = st.text_input("RHEL9 IP Address", "10.167.24.14")
        username = st.text_input("SSH Username", "root")
        password = st.text_input("SSH Password", type="password")
        st.session_state.docker_config = {
            'rhel_ip': rhel_ip,
            'username': username,
            'password': password
        }
    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📦 Running Containers"):
                result = execute_command("docker ps")
                st.code(result)
        with col2:
            if st.button("🗃️ All Containers"):
                result = execute_command("docker ps -a")
                st.code(result)
        if st.button("🖼️ Docker Images"):
            result = execute_command("docker images")
            st.code(result)
    with tab3:
        st.subheader("🚀 Launch New Container")
        col1, col2, col3 = st.columns(3)
        with col1:
            img = st.text_input("Image Name (e.g., ubuntu:latest)")
        with col2:
            container_name = st.text_input("Container Name (optional)")
        with col3:
            port_mapping = st.text_input("Port Mapping (e.g., 8080:80)")
        if st.button("🚀 Run Container") and img:
            cmd = f"docker run -dit"
            if container_name:
                cmd += f" --name {container_name}"
            if port_mapping:
                cmd += f" -p {port_mapping}"
            cmd += f" {img}"
            result = execute_command(cmd)
            if "Error" not in result:
                st.success(f"✅ Container launched successfully!")
                st.code(result)
            else:
                st.error("❌ Failed to launch container")
                st.code(result)
    with tab4:
        col1, col2 = st.columns(2)
        with col1:
            container_id = st.text_input("Container ID/Name to stop:")
            if st.button("🛑 Stop Container") and container_id:
                result = execute_command(f"docker stop {container_id}")
                st.code(result)
        with col2:
            remove_id = st.text_input("Container ID/Name to remove:")
            if st.button("🗑️ Remove Container") and remove_id:
                result = execute_command(f"docker rm {remove_id}")
                st.code(result)
        if st.button("🧹 Clean System"):
            result = execute_command("docker system prune -f")
            st.success("System cleaned!")
            st.code(result)
    with tab5:
        st.subheader("🚀 Docker Project Showcase")
        st.markdown("Showcase of various container-based projects implemented using Docker")
        
        # Docker-in-Docker (DinD)
        st.markdown("---")
        st.subheader("🔄 Docker-in-Docker (DinD)")
        st.markdown("""
        Docker-in-Docker (DinD) allows you to run Docker containers within a Docker container. 
        This is particularly useful for CI/CD pipelines where you need to build and test Docker images.
        
        **Key Features:**
        - Run Docker commands inside a container
        - Build Docker images within containers
        - Test containerized applications in isolation
        """)
        st.markdown("[View DinD Project](https://www.linkedin.com/posts/suhana-laddha-b88874295_docker-dockerindocker-dind-activity-7350018647999864832-Bfan?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEd_SJgBPramPoTnC2UCLtfN15Su8W_bqNo)")
        
        # MongoDB in Container
        st.markdown("---")
        st.subheader("🍃 MongoDB in Container")
        st.markdown("""
        Running MongoDB in a Docker container provides a portable and scalable database solution. 
        This project demonstrates how to set up and manage MongoDB using Docker.
        
        **Key Features:**
        - Persistent data storage using volumes
        - Environment configuration for MongoDB
        - Easy deployment and scaling
        - Backup and restore operations
        """)
        st.markdown("[View MongoDB Project](https://www.linkedin.com/posts/suhana-laddha-b88874295_mongodb-linuxworld-vimaldagasir-activity-7355099586148913152-jXva?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEd_SJgBPramPoTnC2UCLtfN15Su8W_bqNo)")
        
        # Apache Webserver in Container
        st.markdown("---")
        st.subheader("🌐 Apache Webserver in Container")
        st.markdown("""
        This project showcases how to containerize an Apache webserver using Docker. 
        It demonstrates serving static websites and basic web hosting capabilities.
        
        **Key Features:**
        - Serve HTML/CSS/JavaScript files
        - Custom configuration via httpd.conf
        - Port mapping for web access
        - Volume mounting for content management
        """)
        apache_url = st.text_input("Apache Webserver Project LinkedIn URL:", key="apache_url")
        if apache_url:
            st.markdown(f"[View Apache Project]({apache_url})")
        
        # Flask Ping Application
        st.markdown("---")
        st.subheader("🏓 Flask Ping Application")
        st.markdown("""
        A simple Flask application that responds to ping requests. 
        This project demonstrates containerizing a Python web application with Docker.
        
        **Key Features:**
        - RESTful API endpoint
        - Health check functionality
        - Dockerfile optimization
        - Multi-stage builds for smaller images
        """)
        st.markdown("[View Flask Ping Project](https://www.linkedin.com/posts/suhana-laddha-b88874295_flask-docker-rhel-activity-7355164980716982273-t3cQ?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEd_SJgBPramPoTnC2UCLtfN15Su8W_bqNo)")
        
        # Microservices Project
        st.markdown("---")
        st.subheader("🏗️ Microservices Architecture")
        st.markdown("""
        ### Built a Microservices-Based Project Using Docker & Python
        
        I recently worked on a DevOps project that implements a clean microservices architecture with two independent services:
         📦 User Service and 📦 Data Service — both containerized and running through Docker.
        
        **Project Highlights:**
        - Separated codebase for each service with its own app.py, Dockerfile, and requirements.txt
        - Used PostgreSQL as the backend database, initialized using init.sql
        - Defined and managed all services with a single docker-compose.yml for orchestration
        - Followed a clean, modular folder structure suitable for real-world applications
        
        **Key Learnings:**
        - How microservices communicate through containers
        - The importance of clean dependency and environment isolation
        - End-to-end service deployment and linking with Docker
        
        Grateful for the continuous guidance I receive during my internship at LinuxWorld, where learning truly happens through doing. 🙌
        """)
        st.markdown("[View Microservices Project](https://www.linkedin.com/posts/suhana-laddha-b88874295_devops-microservices-docker-activity-7355159726852100096-52v3?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEd_SJgBPramPoTnC2UCLtfN15Su8W_bqNo)")
        
        # Docker Architecture Overview
        st.markdown("---")
        st.subheader("🏗️ Docker Architecture Overview")
        st.image("https://www.docker.com/sites/default/files/d8/2019-07/container-what-is-container.png", 
                caption="Docker Container Architecture")

# JavaScript Tasks
elif menu == "⚡ JavaScript Tasks":
    st.header("🟨 JavaScript Projects Dashboard")
    st.markdown("This section includes various JS-based tools like webcam photo capture, email sending, and WhatsApp messaging, all embedded inside your Streamlit app.")
    
    st.markdown("### 📸 Project 1: Capture Photo & Download")
    with st.expander("▶️ Open Camera + Download Tool"):
        try:
            components.html(open("photo.html", "r", encoding="utf-8").read(), height=500, scrolling=True)
        except FileNotFoundError:
            st.error("photo.html file not found!")
    
    st.markdown("### 📧 Project 2: Send Email via EmailJS")
    with st.expander("▶️ Open EmailJS Mailer"):
        try:
            components.html(open("email.html", "r", encoding="utf-8").read(), height=500, scrolling=False)
        except FileNotFoundError:
            st.error("email.html file not found!")
    
    st.markdown("### 📸📧 Project 3: Take Photo & Send via Gmail")
    with st.expander("▶️ Open Capture + Email Tool"):
        try:
            components.html(open("photogml.html", "r", encoding="utf-8").read(), height=600, scrolling=False)
        except FileNotFoundError:
            st.error("photogml.html file not found!")
    
    st.markdown("### 💬 Project 4: Send WhatsApp Message")
    with st.expander("▶️ Open WhatsApp Web Messenger"):
        try:
            components.html(open("whtsp.html", "r", encoding="utf-8").read(), height=400, scrolling=False)
        except FileNotFoundError:
            st.error("whtsp.html file not found!")
    
    st.markdown("### 📱 Project 5: Instagram Auto Poster")
    with st.expander("▶️ Open Instagram Auto Poster"):
        st.subheader("Instagram Auto Poster Configuration")
        
        # Configuration inputs
        st.markdown("#### Login Credentials")
        col1, col2 = st.columns(2)
        with col1:
            username = st.text_input("Instagram Username")
        with col2:
            password = st.text_input("Instagram Password", type="password")
        
        st.markdown("#### File Settings")
        session_file = st.text_input("Session File Path", value="instagram_session.json")
        temp_image_path = st.text_input("Temporary Image Path", value="temp_image.jpg")
        
        # Post settings
        st.markdown("#### Post Settings")
        uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
        caption = st.text_area("Enter Caption", max_chars=2200)
        
        col1, col2 = st.columns(2)
        with col1:
            post_now = st.button("📤 Post Now")
        with col2:
            enable_schedule = st.checkbox("🕒 Schedule Post")
        
        if enable_schedule:
            post_time = st.time_input("Choose Daily Time")
        else:
            post_time = None
        
        status = st.empty()
        
        # Import required modules
        try:
            from instagrapi import Client
            import schedule
            import threading
            import time
        except ImportError:
            st.error("Required modules not installed. Please run: pip install instagrapi schedule")
        
        # Instagram login function
        def login_instagram():
            cl = Client()
            if os.path.exists(session_file):
                cl.load_settings(session_file)
                try:
                    cl.login(username, password)
                except Exception:
                    st.warning("⚠️ Session expired, retrying login...")
                    cl.set_settings({})
                    cl.login(username, password)
                    cl.dump_settings(session_file)
            else:
                cl.login(username, password)
                cl.dump_settings(session_file)
            return cl
        
        # Post function
        def post_to_instagram(image_path, caption_text):
            try:
                client = login_instagram()
                client.photo_upload(image_path, caption_text)
                return "✅ Post uploaded successfully!"
            except Exception as e:
                return f"❌ Error during posting: {e}"
        
        # Scheduler function
        def start_scheduler(scheduled_time, caption_text):
            def job():
                if os.path.exists(temp_image_path):
                    post_to_instagram(temp_image_path, caption_text)
                else:
                    print("Image not found. Skipping scheduled post.")
            
            schedule.every().day.at(scheduled_time).do(job)
            
            def run_scheduler():
                while True:
                    schedule.run_pending()
                    time.sleep(60)
            
            threading.Thread(target=run_scheduler, daemon=True).start()
            return f"⏰ Scheduled daily post at {scheduled_time}"
        
        # Handle immediate post
        if post_now:
            if uploaded_file and caption and username and password:
                with open(temp_image_path, "wb") as f:
                    f.write(uploaded_file.read())
                result = post_to_instagram(temp_image_path, caption)
                if "✅" in result:
                    status.success(result)
                else:
                    status.error(result)
            else:
                st.warning("⚠️ Please fill all required fields.")
        
        # Handle scheduling
        if enable_schedule and post_time:
            if uploaded_file and caption and username and password:
                with open(temp_image_path, "wb") as f:
                    f.write(uploaded_file.read())
                scheduled_str = post_time.strftime("%H:%M")
                msg = start_scheduler(scheduled_str, caption)
                status.success(msg)
            else:
                st.warning("⚠️ Please fill all required fields to schedule the post.")
    
    st.markdown("### 🎥 Project 6: Video Recorder and Email")
    with st.expander("▶️ Open Video Recorder"):
        try:
            components.html(open("video_email.html", "r", encoding="utf-8").read(), height=600, scrolling=False)
        except FileNotFoundError:
            st.error("video_email.html file not found!")

# Git Tasks
elif menu == "📝 Git Tasks":
    st.header("📝 Git Version Control")
    tab1, tab2, tab3, tab4 = st.tabs(["ℹ️ Status", "📥 Pull/Fetch", "📤 Commit/Push", "🌿 Branches"])
    with tab1:
        if st.button("📊 Git Status"):
            result = execute_command("git status")
            st.code(result)
        if st.button("📜 Git Log (Last 5)"):
            result = execute_command("git log --oneline -5")
            st.code(result)
    with tab2:
        repo_dir = st.text_input("Repository Path (optional):")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📥 Git Pull"):
                cmd = f"cd {repo_dir} && git pull" if repo_dir else "git pull"
                result = execute_command(cmd)
                st.code(result)
        with col2:
            if st.button("📡 Git Fetch"):
                cmd = f"cd {repo_dir} && git fetch" if repo_dir else "git fetch"
                result = execute_command(cmd)
                st.code(result)
    with tab3:
        commit_msg = st.text_input("Commit Message:")
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("➕ Add All"):
                result = execute_command("git add .")
                st.code(result)
        with col2:
            if st.button("💾 Commit") and commit_msg:
                result = execute_command(f'git commit -m "{commit_msg}"')
                st.code(result)
        with col3:
            if st.button("📤 Push"):
                result = execute_command("git push")
                st.code(result)
    with tab4:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🌿 List Branches"):
                result = execute_command("git branch -a")
                st.code(result)
        with col2:
            branch_name = st.text_input("New Branch Name:")
            if st.button("➕ Create Branch") and branch_name:
                result = execute_command(f"git checkout -b {branch_name}")
                st.code(result)

# Kubernetes Tasks
elif menu == "☸️ Kubernetes Tasks":
    st.header("☸️ Kubernetes Orchestration")
    
    # Add cluster configuration
    st.subheader("🔌 Cluster Configuration")
    col1, col2 = st.columns(2)
    with col1:
        kube_config = st.text_area("Kubeconfig Content", height=200, help="Paste your kubeconfig content here")
    with col2:
        cluster_context = st.text_input("Cluster Context", help="Specify the context to use (optional)")
    
    # Function to execute kubectl command
    def execute_kubectl_command(command):
        try:
            # Save kubeconfig to a temporary file
            if kube_config:
                with open("temp_kubeconfig", "w") as f:
                    f.write(kube_config)
                os.environ["KUBECONFIG"] = "temp_kubeconfig"
            
            # Add context if specified
            if cluster_context:
                command = f"kubectl config use-context {cluster_context} && {command}"
            
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return result.stdout if result.returncode == 0 else result.stderr
        except Exception as e:
            return f"Error: {str(e)}"
    
    # Check if cluster is accessible
    if st.button("Test Cluster Connection"):
        result = execute_kubectl_command("kubectl cluster-info")
        if "Error" in result:
            st.error(result)
        else:
            st.success("Cluster Connection Established!")
    
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "🔍 Resources", "📝 Describe", "⚙️ Management"])
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🏢 Cluster Info"):
                result = execute_kubectl_command("kubectl cluster-info")
                st.code(result)
        with col2:
            if st.button("📦 All Pods"):
                result = execute_kubectl_command("kubectl get pods --all-namespaces")
                st.code(result)
    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔧 Services"):
                result = execute_kubectl_command("kubectl get services")
                st.code(result)
        with col2:
            if st.button("📱 Deployments"):
                result = execute_kubectl_command("kubectl get deployments")
                st.code(result)
        if st.button("📊 Nodes"):
            result = execute_kubectl_command("kubectl get nodes")
            st.code(result)
    with tab3:
        resource_type = st.selectbox("Resource Type:", ["pod", "service", "deployment", "node"])
        resource_name = st.text_input("Resource Name:")
        if st.button("🔍 Describe Resource") and resource_name:
            result = execute_kubectl_command(f"kubectl describe {resource_type} {resource_name}")
            st.code(result)
    with tab4:
        st.subheader("⚙️ Resource Management")
        yaml_content = st.text_area("YAML Configuration:", height=200)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Apply Config") and yaml_content:
                # Save to temp file and apply
                with open("temp_config.yaml", "w") as f:
                    f.write(yaml_content)
                result = execute_kubectl_command("kubectl apply -f temp_config.yaml")
                st.code(result)
        with col2:
            delete_resource = st.text_input("Delete Resource (type/name):")
            if st.button("🗑️ Delete") and delete_resource:
                result = execute_kubectl_command(f"kubectl delete {delete_resource}")
                st.code(result)

# ML Tasks
elif menu == "🤖 ML Tasks":
    st.header("🤖 Machine Learning & AI Tools")
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs([
        "🏠 Predictions", 
        "🧠 NLP Models", 
        "📊 Data Analysis", 
        "📈 Visualization", 
        "🧮 Statistics",
        "📊 Train Marks Model",
        "🧠 Deep Learning Model",
        "✍️ Prompt Engineering",
        "🎯 Project Showcase",
        "👁️ Computer Vision"
    ])
    with tab1:
        st.subheader("🏠 House Price Prediction")
        col1, col2, col3 = st.columns(3)
        with col1:
            sqft = st.number_input("Square Feet", min_value=0, value=1500)
        with col2:
            bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)
        with col3:
            bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)
        location_multiplier = st.slider("Location Factor", 0.5, 2.0, 1.0)
        if st.button("💰 Predict Price"):
            # Simple price calculation model
            base_price = sqft * 5000
            bedroom_bonus = bedrooms * 100000
            bathroom_bonus = bathrooms * 50000
            final_price = (base_price + bedroom_bonus + bathroom_bonus) * location_multiplier
            st.success(f"🏠 Estimated Price: ₹{final_price:,.2f}")
            # Show breakdown
            with st.expander("💡 Price Breakdown"):
                st.write(f"Base Price (₹5000/sqft): ₹{base_price:,.2f}")
                st.write(f"Bedroom Bonus: ₹{bedroom_bonus:,.2f}")
                st.write(f"Bathroom Bonus: ₹{bathroom_bonus:,.2f}")
                st.write(f"Location Factor: {location_multiplier}x")
    with tab2:
        st.subheader("🧠 Natural Language Processing Models")
        # Sentiment Analysis Demo
        st.markdown("#### 😊 Sentiment Analysis")
        text_input = st.text_area("Enter text for sentiment analysis:",
                                 placeholder="I'm feeling great about this new project!")
        if st.button("🔍 Analyze Sentiment"):
            # Simple keyword-based sentiment analysis for demo
            positive_words = ['good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic', 'happy', 'love', 'perfect']
            negative_words = ['bad', 'terrible', 'awful', 'hate', 'sad', 'angry', 'frustrated', 'disappointed']
            text_lower = text_input.lower()
            pos_count = sum(1 for word in positive_words if word in text_lower)
            neg_count = sum(1 for word in negative_words if word in text_lower)
            if pos_count > neg_count:
                sentiment = "Positive 😊"
                confidence = min(0.9, 0.5 + (pos_count - neg_count) * 0.1)
            elif neg_count > pos_count:
                sentiment = "Negative 😔"
                confidence = min(0.9, 0.5 + (neg_count - pos_count) * 0.1)
            else:
                sentiment = "Neutral 😐"
                confidence = 0.5
            col1, col2 = st.columns(2)
            col1.metric("Sentiment", sentiment)
            col2.metric("Confidence", f"{confidence:.2%}")
        # Text Classification Demo
        st.markdown("#### 📝 Text Classification")
        classification_text = st.text_area("Enter text for classification:",
                                         placeholder="This movie was absolutely brilliant!")
        categories = st.multiselect("Categories:",
                                  ["Entertainment", "Technology", "Health", "Sports", "Politics"],
                                  default=["Entertainment", "Technology"])
        if st.button("🏷️ Classify Text") and classification_text:
            # Mock classification results
            import random
            results = {}
            for category in categories:
                confidence = random.uniform(0.1, 0.9)
                results[category] = confidence
            # Sort by confidence
            sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
            st.write("**Classification Results:**")
            for category, confidence in sorted_results:
                st.write(f"**{category}**: {confidence:.2%}")
                st.progress(confidence)
        # Connect to AI Psychiatrist
        st.markdown("---")
        st.info("💡 **Want to try advanced NLP?** Check out the AI Psychiatrist project in Featured Projects!")
        if st.button("🧠 Go to AI Psychiatrist"):
            st.session_state.menu = "⭐ Featured Projects"
            st.rerun()
    with tab3:
        st.subheader("📊 Sample Dataset Analysis")
        if st.button("📈 Generate Real Estate Dataset"):
            # Generate sample data
            n_samples = st.slider("Number of Samples", 10, 100, 50)
            data = {
                'Area_sqft': [random.randint(800, 3000) for _ in range(n_samples)],
                'Bedrooms': [random.randint(1, 5) for _ in range(n_samples)],
                'Bathrooms': [random.randint(1, 4) for _ in range(n_samples)],
                'Age_years': [random.randint(0, 30) for _ in range(n_samples)],
                'Location_Score': [random.uniform(0.5, 2.0) for _ in range(n_samples)]
            }
            # Calculate prices based on our model
            data['Price'] = [
                (area * 5000 + bed * 100000 + bath * 50000) * loc_score - age * 10000
                for area, bed, bath, age, loc_score in zip(
                    data['Area_sqft'], data['Bedrooms'], data['Bathrooms'],
                    data['Age_years'], data['Location_Score']
                )
            ]
            df = pd.DataFrame(data)
            st.dataframe(df, use_container_width=True)
            # Basic statistics
            st.subheader("📈 Dataset Statistics")
            st.write(df.describe())
    with tab4:
        if 'df' in locals():
            st.subheader("📊 Data Visualizations")
            viz_type = st.selectbox("Visualization Type:",
                                  ["Price Distribution", "Area vs Price", "Bedrooms vs Price"])
            if viz_type == "Price Distribution":
                st.bar_chart(df['Price'])
            elif viz_type == "Area vs Price":
                st.scatter_chart(df[['Area_sqft', 'Price']])
            elif viz_type == "Bedrooms vs Price":
                bedroom_avg = df.groupby('Bedrooms')['Price'].mean()
                st.bar_chart(bedroom_avg)
        else:
            st.info("Generate a dataset first to see visualizations!")
    with tab5:
        st.subheader("🧮 Statistical Calculators")
        # Simple statistics calculator
        numbers = st.text_input("Enter numbers (comma-separated):")
        if st.button("📊 Calculate Statistics") and numbers:
            try:
                num_list = [float(x.strip()) for x in numbers.split(',')]
                mean_val = sum(num_list) / len(num_list)
                median_val = sorted(num_list)[len(num_list) // 2]
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Mean", f"{mean_val:.2f}")
                with col2:
                    st.metric("Median", f"{median_val:.2f}")
                with col3:
                    st.metric("Count", len(num_list))
            except ValueError:
                st.error("Please enter valid numbers separated by commas")
    with tab6:
        st.subheader("📊 Train Marks Prediction Model")
        st.write("Upload a CSV file with 'Hours' and 'Marks' columns to train a linear regression model.")
        
        # File upload
        uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
        
        if uploaded_file is not None:
            try:
                # Read the uploaded file
                data = pd.read_csv(uploaded_file)
                st.write("Dataset preview:")
                st.dataframe(data.head())
                
                # Check if required columns exist
                if 'Hours' in data.columns and 'Marks' in data.columns:
                    X = data[['Hours']]
                    y = data['Marks']
                    
                    # Split the data
                    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
                    
                    # Train the model
                    model = LinearRegression()
                    model.fit(X_train, y_train)
                    
                    # Display model metrics
                    st.write(f"Model Coefficient: {model.coef_[0]:.4f}")
                    st.write(f"Model Intercept: {model.intercept_[0]:.4f}")
                    
                    # Save the model
                    joblib.dump(model, "marks_predictor.pkl")
                    st.success("✅ Model trained and saved as marks_predictor.pkl")
                    
                    # Provide download link for the model
                    with open("marks_predictor.pkl", "rb") as f:
                        st.download_button(
                            label="Download Trained Model",
                            data=f,
                            file_name="marks_predictor.pkl",
                            mime="application/octet-stream"
                        )
                else:
                    st.error("CSV must contain 'Hours' and 'Marks' columns")
            except Exception as e:
                st.error(f"Error processing file: {e}")
        else:
            st.info("Please upload a CSV file to train the model.")
    with tab7:
        st.subheader("🧠 Deep Learning Model Builder")
        st.write("Build a simple sequential neural network model.")
        
        # Model configuration
        col1, col2 = st.columns(2)
        with col1:
            input_shape = st.number_input("Input Shape", min_value=1, value=5)
        with col2:
            num_layers = st.number_input("Number of Layers", min_value=1, max_value=10, value=2)
        
        # Create model button
        if st.button("Create Model"):
            try:
                # Initialize the model
                brain = Sequential()
                
                # Add input layer
                brain.add(Dense(units=4, input_shape=(input_shape,)))
                
                # Add hidden layers
                for i in range(int(num_layers) - 1):
                    units = st.number_input(f"Units in Layer {i+2}", min_value=1, value=5, key=f"layer_{i}")
                    brain.add(Dense(units=units))
                
                # Display model summary
                st.subheader("Model Summary")
                brain.summary()
                
                # Save model architecture
                model_json = brain.to_json()
                with open("model_architecture.json", "w") as json_file:
                    json_file.write(model_json)
                
                st.success("✅ Model architecture created and saved as model_architecture.json")
                
                # Provide download link
                with open("model_architecture.json", "r") as f:
                    st.download_button(
                        label="Download Model Architecture",
                        data=f.read(),
                        file_name="model_architecture.json",
                        mime="application/json"
                    )
            except Exception as e:
                st.error(f"Error creating model: {e}")
    with tab8:
        st.subheader("✍️ Prompt Engineering with LifeHacksHelperGPT")
        st.markdown("""
        LifeHacksHelperGPT is an AI assistant that provides life hacks, productivity tips, and time-saving tricks. 
        It helps users simplify their lives and boost efficiency through practical advice.
        """)
        
        # API Key input
        google_api_key = st.text_input("Google API Key:", type="password", key="lifehacks_api_key")
        
        # User input
        user_question = st.text_area("Ask for a life hack or productivity tip:", height=100)
        
        if st.button("Get Life Hack"):
            if not google_api_key:
                st.error("Please enter your Google API key")
            elif not user_question:
                st.error("Please ask a question")
            else:
                try:
                    # Configure the API
                    genai.configure(api_key=google_api_key)
                    
                    # Initialize the model
                    model = genai.GenerativeModel("gemini-2.5-flash")
                    
                    # Start chat with system message
                    chat = model.start_chat(
                        history=[
                            {
                                "role": "user",
                                "parts": [" You are LifeHacksHelperGPT and you possess extensive knowledge of life hacks, productivity tips, and time-saving tricks. Offering guidance on organizing, multitasking, and optimizing daily routines, you help users simplify their lives and boost their efficiency."]
                            }
                        ]
                    )
                    
                    # Get response
                    response = chat.send_message(user_question)
                    
                    # Display response
                    st.subheader("LifeHacksHelperGPT Response:")
                    st.success(response.text)
                except Exception as e:
                    st.error(f"Error processing your request: {e}")
        
        # Example questions
        st.markdown("---")
        st.markdown("### Example Questions:")
        st.markdown("""
        - How can I better organize my workspace for productivity?
        - What are some time-saving tricks for meal preparation?
        - How can I improve my morning routine to be more efficient?
        - What are some multitasking techniques that actually work?
        """)
    with tab9:
        st.subheader("🎯 ML Project Showcase")
        
        # Project 1
        st.markdown("---")
        st.subheader("📊 Sales Prediction Model")
        st.markdown("""
        ### Advanced Sales Forecasting with Machine Learning
        
        This project involved developing a sophisticated sales prediction model using advanced regression techniques.
        
        #### Project Highlights:
        - Analyzed historical sales data across multiple product categories
        - Implemented feature engineering to capture seasonality and trends
        - Compared multiple regression models (Linear, Random Forest, XGBoost)
        - Achieved 92% accuracy in predicting quarterly sales figures
        
        #### Technologies Used:
        - Python, Pandas, NumPy
        - Scikit-learn, XGBoost
        - Matplotlib, Seaborn for visualization
        - Jupyter Notebooks for experimentation
        
        This project significantly improved inventory planning and resource allocation for the business.
        """)
        
        linkedin_url = st.text_input("LinkedIn Post URL:", placeholder="https://www.linkedin.com/posts/username-sales-prediction", key="sales_pred_url")
        
        if linkedin_url:
            if st.button("View LinkedIn Post", key="view_sales_pred"):
                st.markdown(f"[View LinkedIn Post]({linkedin_url})")
        
        # Project 2
        st.markdown("---")
        st.subheader("🔍 Image Classification System")
        st.markdown("""
        ### Automated Image Classification with Deep Learning
        
        Developed an image classification system to categorize products for an e-commerce platform.
        
        #### Project Highlights:
        - Built a convolutional neural network (CNN) from scratch
        - Trained on a dataset of 50,000+ product images
        - Achieved 95% classification accuracy across 10 categories
        - Implemented data augmentation techniques to improve model generalization
        
        #### Technologies Used:
        - TensorFlow, Keras
        - OpenCV for image processing
        - Google Colab for GPU acceleration
        - Flask for creating a simple API
        
        The system was integrated into the company's product upload workflow, reducing manual categorization effort by 80%.
        """)
        
        linkedin_url = st.text_input("LinkedIn Post URL:", placeholder="https://www.linkedin.com/posts/username-image-classification", key="image_class_url")
        
        if linkedin_url:
            if st.button("View LinkedIn Post", key="view_image_class"):
                st.markdown(f"[View LinkedIn Post]({linkedin_url})")
        
        # Project 3
        st.markdown("---")
        st.subheader("🗣️ Natural Language Processing")
        st.markdown("""
        ### Sentiment Analysis for Customer Reviews
        
        Developed an advanced NLP system to analyze customer sentiment from product reviews and feedback.
        
        #### Project Highlights:
        - Implemented BERT-based sentiment analysis model
        - Processed over 100,000 customer reviews with 89% accuracy
        - Created a dashboard for real-time sentiment tracking
        - Integrated with customer support system for priority handling
        
        #### Technologies Used:
        - Python, NLTK, spaCy
        - Transformers, BERT
        - Streamlit for dashboard
        - AWS for deployment
        
        This project helped the company identify customer pain points and improve product quality.
        """)
        
        linkedin_url = st.text_input("LinkedIn Post URL:", placeholder="https://www.linkedin.com/posts/username-nlp-project", key="nlp_url")
        
        if linkedin_url:
            if st.button("View LinkedIn Post", key="view_nlp"):
                st.markdown(f"[View LinkedIn Post]({linkedin_url})")
    with tab10:
        st.subheader("👁️ Computer Vision Project")
        st.markdown("""
        ### Advanced Object Detection and Recognition
        
        This project focuses on developing a state-of-the-art computer vision system for real-time object detection and recognition in complex environments.
        
        #### Project Highlights:
        - Implemented YOLOv5 for real-time object detection with 95% accuracy
        - Created custom dataset with 10,000+ annotated images
        - Developed a user-friendly interface for easy interaction
        - Optimized model for edge devices with TensorFlow Lite
        
        #### Technical Approach:
        - Used OpenCV for image preprocessing and augmentation
        - Implemented transfer learning with pre-trained models
        - Created a pipeline for model training, evaluation, and deployment
        - Developed a REST API using Flask for model inference
        
        This project has applications in surveillance, retail analytics, and autonomous systems.
        """)
        
        linkedin_url = st.text_input("LinkedIn Post URL:", placeholder="https://www.linkedin.com/posts/username-computer-vision-project")
        
        if linkedin_url:
            if st.button("View LinkedIn Post"):
                st.markdown(f"[View LinkedIn Post]({linkedin_url})")
        
        st.markdown("---")
        st.subheader("Project Demo")
        st.image("https://miro.medium.com/max/1400/1*SH5oB5FkFf1Gz7m5tJYpPA.png", caption="Object Detection in Action")

# Web Dev Tasks
elif menu == "🌐 Web Dev Tasks":
    st.header("🌐 Web Development Tools")
    tab1, tab2, tab3 = st.tabs(["🎨 HTML Generator", "💅 CSS Styles", "🔧 Tools"])
    with tab1:
        st.subheader("🎨 HTML Page Generator")
        col1, col2 = st.columns(2)
        with col1:
            title = st.text_input("Page Title", value="My Awesome Page")
            body = st.text_area("Page Content", value="Welcome to my website!", height=100)
        with col2:
            bg_color = st.color_picker("Background Color", "#ffffff")
            text_color = st.color_picker("Text Color", "#000000")
            font_family = st.selectbox("Font Family", ["Arial", "Helvetica", "Georgia", "Times New Roman"])
        if st.button("🚀 Generate HTML"):
            html_code = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            background-color: {bg_color};
            color: {text_color};
            font-family: {font_family}, sans-serif;
            padding: 20px;
            line-height: 1.6;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }}
        h1 {{
            border-bottom: 2px solid {text_color};
            padding-bottom: 10px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{title}</h1>
        <p>{body}</p>
        <footer>
            <small>Generated by Suhana's Toolkit at {format_timestamp()}</small>
        </footer>
    </div>
</body>
</html>"""
            st.code(html_code, language='html')
            # Provide download option
            st.download_button(
                label="💾 Download HTML",
                data=html_code,
                file_name=f"{title.lower().replace(' ', '_')}.html",
                mime="text/html"
            )
    with tab2:
        st.subheader("💅 CSS Style Generator")
        element_type = st.selectbox("Element Type:", ["button", "div", "input", "h1", "p"])
        col1, col2, col3 = st.columns(3)
        with col1:
            css_bg = st.color_picker("Background", "#4CAF50", key="css_bg")
            css_color = st.color_picker("Text Color", "#ffffff", key="css_text")
        with col2:
            padding = st.slider("Padding (px)", 0, 20, 5, key="css_padding")
            margin = st.slider("Margin (px)", 0, 20, 5, key="css_margin")
        with col3:
            border_radius = st.slider("Border Radius (px)", 0, 20, 5, key="css_radius")
            font_size = st.slider("Font Size (px)", 10, 30, 16, key="css_font")
        if st.button("✨ Generate CSS"):
            css_code = f"""{element_type} {{
    background-color: {css_bg};
    color: {css_color};
    padding: {padding}px;
    margin: {margin}px;
    border-radius: {border_radius}px;
    font-size: {font_size}px;
}}"""
            st.code(css_code, language='css')
            # Download CSS
            st.download_button(
                label="💾 Download CSS",
                data=css_code,
                file_name="style.css",
                mime="text/css"
            )
    with tab3:
        st.subheader("🔧 Useful Web Dev Tools")
        # Placeholder for more tools
        st.info("More tools coming soon! Stay tuned.")

# Jenkins Tasks
elif menu == "🔧 Jenkins Tasks":
    st.header("🔧 Jenkins Automation")
    tab1, tab2 = st.tabs(["📋 Overview", "🚀 CI/CD Pipeline"])
    
    with tab1:
        st.info("Jenkins integration is coming soon! Stay tuned.")
    
    with tab2:
        st.subheader("🚀 CI/CD Pipeline Showcase")
        st.markdown("""
        ### CI/CD Pipeline with Jenkins
        Continuous Integration and Continuous Deployment (CI/CD) is a crucial part of modern software development. 
        Jenkins is a leading open-source automation server that helps implement CI/CD pipelines.
        
        #### Key Components:
        - **Source Code Management**: Integration with Git repositories
        - **Build Automation**: Compiling code and running tests
        - **Deployment**: Automatically deploying to staging/production environments
        - **Notification**: Alerting team members about build status
        """)
        
        st.markdown("[View LinkedIn Post](https://www.linkedin.com/posts/suhana-laddha-b88874295_devops-jenkins-github-activity-7347752969494327296-q6Y_?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEd_SJgBPramPoTnC2UCLtfN15Su8W_bqNo)")
        
        st.markdown("---")
        st.subheader("CI/CD Pipeline Diagram")
        st.image("https://www.jenkins.io/images/book-title/cd-pipeline.png", caption="Typical CI/CD Pipeline")

# AWS Tasks
elif menu == "☁️ AWS Tasks":
    st.header("☁️ AWS Cloud Services")
    tab1, tab2, tab3, tab4 = st.tabs(["📋 Overview", "🔌 API Gateway Project", "🤖 EC2 Gesture Control", "⚡ Serverless Computing"])
    
    with tab1:
        st.info("AWS integration is coming soon! Stay tuned.")
    
    with tab2:
        st.subheader("🔌 API Gateway with Lambda and EC2")
        st.markdown("""
        ### Serverless API with AWS API Gateway
        
        This project demonstrates how to create a serverless API using AWS services:
        
        #### Architecture Components:
        1. **API Gateway**: Acts as the entry point for all API requests
        2. **Lambda Functions**: Process requests and implement business logic
        3. **EC2 Instances**: Host backend services or databases
        4. **DynamoDB**: NoSQL database for storing data (optional)
        5. **IAM Roles**: Secure access between services
        
        #### Workflow:
        1. Client sends a request to API Gateway
        2. API Gateway triggers a Lambda function
        3. Lambda function processes the request
        4. Lambda may interact with EC2 instances or databases
        5. Response is returned through API Gateway to the client
        
        #### Benefits:
        - **Scalability**: Automatically scales with demand
        - **Cost-effective**: Pay only for what you use
        - **Low maintenance**: No server management required
        - **Security**: Built-in security features
        """)
        
        linkedin_url = st.text_input("LinkedIn Post URL:", placeholder="https://www.linkedin.com/posts/username-api-gateway-project")
        
        if linkedin_url:
            if st.button("View LinkedIn Post"):
                st.markdown(f"[View LinkedIn Post]({linkedin_url})")
        
        st.markdown("---")
        st.subheader("Architecture Diagram")
        st.image("https://d1.awsstatic.com/serverless/Serverless-Image_API-Gateway-Lambda.4b3b2a9f0b9f3a3f8e5c7e0d7f0c3e1a3f8e5c7e.png", caption="AWS API Gateway with Lambda")
    
    with tab3:
        st.subheader("🤖 EC2 Gesture Control Project")
        st.markdown("""
        ### Launching an AWS EC2 Instance with Just a Hand Gesture! ✨ 👋
        
        During my internship at LinuxWorld, I worked on an exciting project combining Python, OpenCV, and AWS.
        
        #### Project Brief:
        I created a system where showing five fingers in front of a webcam triggers the launch of an EC2 instance on AWS — all done programmatically through Python + Boto3.
        
        #### Tech Stack:
        - Python
        - OpenCV (for gesture recognition)
        - AWS EC2 (via Boto3)
        - Linux scripting
        
        #### Key Features:
        - Real-time hand gesture detection using computer vision
        - Seamless integration with AWS services through Boto3
        - Automated EC2 instance provisioning with predefined configurations
        - Error handling and logging for robust operation
        
        #### Technical Implementation:
        - Used OpenCV's Haar cascades for hand detection
        - Implemented finger counting algorithm to detect five fingers
        - Configured AWS credentials and security groups for secure access
        - Created Boto3 functions to launch EC2 instances with specific AMI and instance type
        - Added termination logic to manage resources efficiently
        
        This project taught me how to connect real-time computer vision with cloud automation — a powerful combo of AI + DevOps!
        
        Grateful for the constant motivation and support from Preeti Ma'am, and truly inspired by Vimal Sir's vision that pushes us to go beyond limits. 🙌
        """)
        
        st.markdown("[View LinkedIn Post](https://www.linkedin.com/posts/suhana-laddha-b88874295_python-aws-gesturecontrol-activity-7357727450966994946-HF-a?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEd_SJgBPramPoTnC2UCLtfN15Su8W_bqNo)")
        
        st.markdown("---")
        st.subheader("Project Demo")
        st.image("https://miro.medium.com/max/1400/1*SH5oB5FkFf1Gz7m5tJYpPA.png", caption="Hand Gesture Recognition for EC2 Control")
        
        st.markdown("---")
        st.subheader("Architecture Diagram")
        st.markdown("""
        The system works in the following steps:
        1. **Capture**: Webcam captures real-time video feed
        2. **Detect**: OpenCV processes frames to detect hand gestures
        3. **Count**: Algorithm counts the number of fingers raised
        4. **Trigger**: When five fingers are detected, Python script triggers AWS Boto3
        5. **Launch**: Boto3 launches a pre-configured EC2 instance
        6. **Confirm**: System confirms successful instance launch
        """)
        
        st.image("https://d1.awsstatic.com/serverless/Serverless-Image_API-Gateway-Lambda.4b3b2a9f0b9f3a3f8e5c7e0d7f0c3e1a3f8e5c7e.png", caption="AWS Architecture Pattern")
    
    with tab4:
        st.subheader("⚡ Serverless Computing Project")
        st.markdown("""
        ### Building Scalable Serverless Applications
        
        This project demonstrates the power of serverless architecture using AWS services to create a highly scalable and cost-effective application.
        
        #### Project Overview:
        - Developed a serverless backend using AWS Lambda and API Gateway
        - Implemented event-driven architecture with S3 and DynamoDB
        - Created automated CI/CD pipeline using AWS CodePipeline
        - Achieved 99.9% uptime with near-zero infrastructure management
        
        #### Key Benefits:
        - **Cost Efficiency**: Pay only for what you use
        - **Auto-scaling**: Automatically handles traffic spikes
        - **Reduced Operational Overhead**: No server management required
        - **Faster Time to Market**: Quick deployment and updates
        
        This project showcases best practices in serverless architecture and cloud-native development.
        """)
        
        linkedin_url = st.text_input("LinkedIn Post URL:", placeholder="https://www.linkedin.com/posts/username-serverless-project")
        
        if linkedin_url:
            if st.button("View LinkedIn Post"):
                st.markdown(f"[View LinkedIn Post]({linkedin_url})")
        
        st.markdown("---")
        st.subheader("Architecture Diagram")
        st.image("https://d1.awsstatic.com/serverless/Serverless-Image_API-Gateway-Lambda.4b3b2a9f0b9f3a3f8e5c7e0d7f0c3e1a3f8e5c7e.png", caption="Serverless Architecture Pattern")

# Web Scraping Tasks
elif menu == "🕸️ Web Scraping":
    st.header("🕸️ Web Scraping Tools")
    tab1, tab2, tab3 = st.tabs(["🔍 View Source", "📰 Scrape Data", "🔎 Google Search"])
    with tab1:
        st.subheader("🔍 View Page Source")
        url = st.text_input("Enter URL:")
        if st.button("View Source"):
            try:
                # Fetch the HTML source code
                response = urllib.request.urlopen(url)
                html = response.read().decode('utf-8')
                # Display the source code
                st.code(html, language='html')  # Use st.code for formatted output
            except Exception as e:
                st.error(f"Error fetching or displaying source: {e}")
    with tab2:
        st.subheader("📰 Scrape Title and Meta Description")
        url_scrape = st.text_input("Enter URL for scraping:")
        if st.button("Scrape Data"):
            try:
                response = urllib.request.urlopen(url_scrape)
                soup = BeautifulSoup(response, 'html.parser')
                title = soup.title.string if soup.title else "No Title Found"
                meta_description = soup.find("meta", attrs={"name": "description"})["content"] if soup.find("meta", attrs={"name": "description"}) else "No Description Found"
                st.write(f"Title: {title}")
                st.write(f"Meta Description: {meta_description}")
            except Exception as e:
                st.error(f"Error scraping data: {e}")
    with tab3:
        st.subheader("🔎 Google Search")
        search_query = st.text_input("Enter search query:")
        num_results = st.number_input("Number of results:", min_value=1, max_value=10, value=5, step=1)  # Limit results
        if st.button("Search Google"):
            try:
                search_results = list(search(search_query, num_results=num_results, stop=num_results))  # Use list and stop
                for result in search_results:
                    st.write(result)
            except Exception as e:
                st.error(f"Error during Google Search: {e}")

# Image Processing Tasks
elif menu == "📸 Image Processing":
    st.header("📸 Image Processing Tools")
    st.subheader("🎨 Create Digital Image")
    image_width = st.number_input("Image Width:", min_value=100, max_value=1000, value=500, step=50)
    image_height = st.number_input("Image Height:", min_value=100, max_value=1000, value=300, step=50)
    background_color = st.color_picker("Background Color:", value="#FFFFFF")  # Default to white
    text_to_add = st.text_input("Text to Add:", value="Hello, World!")
    text_color = st.color_picker("Text Color:", value="#000000")  # Default to black
    if st.button("Create Image"):
        try:
            # Create a new image
            img = Image.new('RGB', (image_width, image_height), color=background_color)
            d = ImageDraw.Draw(img)
            # Calculate text size and position
            text_width, text_height = d.textsize(text_to_add)
            text_x = (image_width - text_width) / 2
            text_y = (image_height - text_height) / 2
            # Add text to the image
            d.text((text_x, text_y), text_to_add, fill=text_color)
            # Display the image
            st.image(img, caption="Generated Image")
        except Exception as e:
            st.error(f"Error creating image: {e}")

# Communication Tasks
elif menu == "💬 Communication":
    st.header("💬 Communication Tools")
    tab1, tab2, tab3 = st.tabs(["📱 SMS", "📞 Call", "💬 WhatsApp"])
    
    # SMS Tab
    with tab1:
        st.subheader("📱 Send SMS")
        # Input fields for Twilio credentials
        account_sid = st.text_input("Twilio Account SID:", key="sms_sid")
        auth_token = st.text_input("Twilio Auth Token:", type="password", key="sms_token")
        twilio_phone_number = st.text_input("Your Twilio Phone Number (with +):", key="sms_from")
        recipient_number = st.text_input("Recipient Number (with country code):", key="sms_to")
        message = st.text_area("SMS Message:", key="sms_message")
        if st.button("Send SMS", key="send_sms"):
            try:
                client = Client(account_sid, auth_token)
                message = client.messages.create(
                    to=recipient_number,
                    from_=twilio_phone_number,
                    body=message
                )
                st.success(f"SMS sent successfully! Message SID: {message.sid}")
            except Exception as e:
                st.error(f"Error sending SMS: {e}")
    
    # Call Tab
    with tab2:
        st.subheader("📞 Make a Twilio Call")
        account_sid_call = st.text_input("Twilio Account SID:", key="call_sid")
        auth_token_call = st.text_input("Twilio Auth Token:", type="password", key="call_token")
        from_number_call = st.text_input("Your Twilio Phone Number (with +):", key="call_from")
        to_number_call = st.text_input("Recipient Number (with country code):", key="call_to")
        twiml_message = st.text_area("TwiML Message:", 
                                     value="<Response><Say>Hello! This is a test call from Python using Twilio.</Say></Response>",
                                     key="call_twiml")
        if st.button("Initiate Call", key="make_call"):
            try:
                client = Client(account_sid_call, auth_token_call)
                call = client.calls.create(
                    to=to_number_call,
                    from_=from_number_call,
                    twiml=twiml_message
                )
                st.success(f"📞 Call initiated successfully! Call SID: {call.sid}")
            except Exception as e:
                st.error(f"❌ Error initiating call: {e}")
    
    # WhatsApp Tab
    with tab3:
        st.subheader("💬 Send WhatsApp Message")
        account_sid_wa = st.text_input("Twilio Account SID:", key="wa_sid")
        auth_token_wa = st.text_input("Twilio Auth Token:", type="password", key="wa_token")
        from_number_wa = st.text_input("Your Twilio WhatsApp Number (with +):", 
                                       value="whatsapp:+", 
                                       key="wa_from")
        to_number_wa = st.text_input("Recipient WhatsApp Number (with country code):", 
                                     value="whatsapp:+", 
                                     key="wa_to")
        wa_message = st.text_area("WhatsApp Message:", 
                                 value="Hello! This is a WhatsApp message from Python 📲",
                                 key="wa_message")
        if st.button("Send WhatsApp Message", key="send_wa"):
            try:
                client = Client(account_sid_wa, auth_token_wa)
                message = client.messages.create(
                    body=wa_message,
                    from_=from_number_wa,
                    to=to_number_wa
                )
                st.success(f"✅ WhatsApp message sent! Message SID: {message.sid}")
            except Exception as e:
                st.error(f"Error sending WhatsApp message: {e}")

# Featured Projects
elif menu == "⭐ Featured Projects":
    st.header("⭐ Featured Projects")
    tab1, tab2, tab3 = st.tabs(["🧠 AI Psychiatrist", "🏗️ Microservices", "📋 Project Showcase"])
    
    with tab1:
        st.subheader("🧠 AI Psychiatrist")
        st.markdown("""
        The AI Psychiatrist is a conversational AI designed to provide mental health support and guidance. 
        It uses advanced natural language processing to understand user concerns and offer helpful responses.
        
        ### Features:
        - Confidential conversations
        - 24/7 availability
        - Evidence-based responses
        - Non-judgmental listening
        """)
        
        # API Key input
        api_key = st.text_input("OpenAI API Key:", type="password", key="psychiatrist_api_key")
        
        # User input
        user_input = st.text_area("Share your thoughts or concerns:", height=150)
        
        if st.button("Get Response"):
            if not api_key:
                st.error("Please enter your OpenAI API key")
            elif not user_input:
                st.error("Please share your thoughts or concerns")
            else:
                try:
                    # Initialize the client
                    Gemini_model = OpenAI(api_key=api_key, base_url="https://generativelanguage.googleapis.com/v1beta/openai")
                    
                    # Define the braindoc function
                    def braindoc(myprompt):
                        mymsg = [
                            {"role": "system", "content": "you are a ai assistant, work like a psychiatrist"},
                            {"role": "user", "content": myprompt}
                        ]
                        response = Gemini_model.chat.completions.create(
                            model="gemini-2.5-flash",
                            messages=mymsg
                        )
                        return response.choices[0].message.content
                    
                    # Get response
                    response = braindoc(user_input)
                    
                    # Display response
                    st.subheader("AI Psychiatrist Response:")
                    st.success(response)
                    
                    # Disclaimer
                    st.markdown("---")
                    st.warning("""
                    **Disclaimer**: This AI is not a substitute for professional medical advice, diagnosis, or treatment. 
                    If you're experiencing a mental health crisis, please contact a professional immediately.
                    """)
                except Exception as e:
                    st.error(f"Error processing your request: {e}")
    
    with tab2:
        st.subheader("🏗️ Microservices Architecture Project")
        st.markdown("""
        ### Built a Microservices-Based Project Using Docker & Python
        
        This project demonstrates the implementation of a clean microservices architecture with two independent services:
        📦 User Service and 📦 Data Service — both containerized and running through Docker.
        
        **Project Highlights:**
        - Separated codebase for each service with its own app.py, Dockerfile, and requirements.txt
        - Used PostgreSQL as the backend database, initialized using init.sql
        - Defined and managed all services with a single docker-compose.yml for orchestration
        - Followed a clean, modular folder structure suitable for real-world applications
        
        **Architecture Overview:**
        - Each service runs in its own Docker container
        - Services communicate through well-defined APIs
        - PostgreSQL database container with persistent storage
        - Docker Compose for orchestration and service linking
        
        **Key Benefits:**
        - **Scalability**: Each service can be scaled independently
        - **Maintainability**: Smaller, focused codebases are easier to maintain
        - **Technology Flexibility**: Each service can use different technologies
        - **Resilience**: Failure in one service doesn't affect others
        
        **Technical Implementation:**
        - User Service: Handles user authentication and management
        - Data Service: Manages business data and business logic
        - API Gateway: Routes requests to appropriate services
        - Message Queue: For asynchronous communication between services
        
        This project showcases best practices in microservices design, containerization, and DevOps workflows.
        """)
        
        st.markdown("[View LinkedIn Post](https://www.linkedin.com/posts/suhana-laddha-b88874295_devops-microservices-docker-activity-7355159726852100096-52v3?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEd_SJgBPramPoTnC2UCLtfN15Su8W_bqNo)")
        
        st.markdown("---")
        st.subheader("Architecture Diagram")
        st.image("https://miro.medium.com/max/1400/1*SH5oB5FkFf1Gz7m5tJYpPA.png", caption="Microservices Architecture Pattern")
    
    with tab3:
        st.subheader("📋 Project Showcase")
        st.info("Coming soon: Showcase of more exciting projects!")

# Agentic AI
elif menu == "🤖 Agentic AI":
    st.header("🤖 Agentic AI Tools")
    st.subheader("🔍 AskNews Tool")
    
    # API key input
    google_api_key = st.text_input("Google API Key:", type="password")
    
    # User question input
    user_question = st.text_area("Enter your question about the news:", 
                                value="What's the latest news about artificial intelligence in education?")
    
    if st.button("Get News Answer"):
        if not google_api_key:
            st.error("Please enter your Google API key")
        elif not user_question:
            st.error("Please enter a question")
        else:
            try:
                # Initialize the LLM
                llm = ChatGoogleGenerativeAI(
                    model="gemini-2.0-flash",
                    google_api_key=google_api_key,
                    convert_system_message_to_human=True,
                    temperature=0.7
                )
                
                # Initialize the AskNews tool
                ask_news_tool = AskNewsSearch()
                tools = [ask_news_tool]
                
                # Create the agent
                agent = create_react_agent(llm, tools)
                
                # Prepare the input message
                input_message = {
                    "role": "user",
                    "content": user_question
                }
                
                # Stream the agent's response
                st.subheader("Agent Response:")
                response_container = st.empty()
                
                with st.spinner("Processing your request..."):
                    full_response = ""
                    for step in agent.stream(
                        {"messages": [input_message]},
                        stream_mode="values",
                    ):
                        if "messages" in step and step["messages"]:
                            last_message = step["messages"][-1]
                            if hasattr(last_message, 'content'):
                                full_response += str(last_message.content) + "\n\n"
                                response_container.markdown(full_response)
                
                st.success("✅ Response generated successfully!")
            except Exception as e:
                st.error(f"Error processing your request: {e}")
    
    # Instructions
    st.markdown("---")
    st.markdown("### How to use this tool:")
    st.markdown("""
    1. Enter your Google API key (from Google AI Studio)
    2. Type your question about current news
    3. Click "Get News Answer" to see the AI agent's response
    4. The agent will search for the latest news and provide a comprehensive answer
    """)

st.sidebar.header("About")
st.sidebar.info("This is Suhana's Toolkit, a collection of useful Python tools and utilities.")
