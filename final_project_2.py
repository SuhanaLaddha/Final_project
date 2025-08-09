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
from PIL import Image
import psutil
import paramiko  # Import paramiko for SSH

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
    "💬 Communication"
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
    "💬 Communication"
].index(st.session_state.menu))

st.session_state.menu = menu  # Update session state after selection

st.markdown("---")

# Dashboard Home
if menu == "🏠 Dashboard Home":
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Available Tools", "16", delta="4")
    with col2:
        st.metric("Commands Run", "0", delta="0")
    with col3:
        st.metric("Success Rate", "100%", delta="0%")
    with col4:
        st.metric("Uptime", "100%", delta="0%")

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

# Python Tasks
elif menu == "🐍 Python Tasks":
    st.header("🐍 Python Development Tools")

    tab1, tab2, tab3, tab4 = st.tabs(["🔢 Calculator", "📦 Packages", "🎲 Random Gen", "📊 Data Tools"])

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

    with tab3:
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

    with tab4:
        st.subheader("📊 Quick Data Analysis")

        # Sample data generator
        if st.button("📈 Generate Sample Dataset"):
            data = {
                'ID': range(1, 11),
                'Name': [f'Item_{i}' for i in range(1, 11)],
                'Value': [random.randint(10, 1000) for _ in range(10)],
                'Category': [random.choice(['A', 'B', 'C']) for _ in range(10)]
            }
            df = pd.DataFrame(data)
            st.dataframe(df, use_container_width=True)
            st.bar_chart(df[['Value']])

# Linux Tasks
elif menu == "🐧 Linux Tasks":
    st.header("🐧 Linux System Administration")

    tab1, tab2, tab3, tab4 = st.tabs(["📂 File System", "💾 System Info", "🔍 Process Monitor", "📝 File Operations"])

    with tab1:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📍 Current Location")
            if st.button("Check PWD"):
                result = execute_command("pwd")
                st.code(result)

        with col2:
            st.subheader("📁 Directory Listing")
            if st.button("List Files (ls -la)"):
                result = execute_command("ls -la")
                st.code(result)

    with tab2:
        col1, col2 = st.columns(2)

        with col1:
            if st.button("💾 Disk Usage"):
                result = execute_command("df -h")
                st.code(result)

        with col2:
            if st.button("🖥️ Memory Usage"):
                result = execute_command("free -h")
                st.code(result)

        if st.button("🔧 System Information"):
            result = execute_command("uname -a")
            st.code(result)

    with tab3:
        if st.button("⚡ Running Processes"):
            result = execute_command("ps aux | head -20")
            st.code(result)

        process_name = st.text_input("Search for process:")
        if st.button("🔍 Search Process") and process_name:
            result = execute_command(f"ps aux | grep {process_name}")
            st.code(result)

    with tab4:
        file_name = st.text_input("Enter filename to read:")
        if st.button("📖 Read File") and file_name:
            content = safe_file_read(file_name)
            st.code(content)

# Docker Tasks
elif menu == "🐳 Docker Tasks":
    st.header("🐳 Docker Container Management")

    tab1, tab2, tab3, tab4 = st.tabs(["⚙️ Configuration", "📊 Overview", "🚀 Launch", "🛑 Control"])

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

# JavaScript Tasks
elif menu == "⚡ JavaScript Tasks":
    st.header("⚡ JavaScript & Web APIs")

    st.info("💡 These are examples of JavaScript functionality that would work in a browser environment")

    tab1, tab2, tab3 = st.tabs(["📱 Web APIs", "🎨 DOM Manipulation", "📡 AJAX Examples"])

    with tab1:
        st.subheader("📸 Media Capture API")
        st.code("""
// Capture user camera
navigator.mediaDevices.getUserMedia({
    video: true,
    audio: true
})
.then(stream => {
    video.srcObject = stream;
})
.catch(err => console.error('Error:', err));
        """, language="javascript")

        st.subheader("🌍 Geolocation API")
        st.code("""
// Get user location
navigator.geolocation.getCurrentPosition(
    position => {
        console.log('Latitude:', position.coords.latitude);
        console.log('Longitude:', position.coords.longitude);
    },
    error => console.error('Error:', error)
);
        """, language="javascript")

    with tab2:
        st.subheader("🎨 DOM Manipulation Examples")
        st.code("""
// Create dynamic elements
const button = document.createElement('button');
button.textContent = 'Click me!';
button.addEventListener('click', () => {
    alert('Button clicked!');
});
document.body.appendChild(button);

// Style manipulation
button.style.backgroundColor = '#4CAF50';
button.style.color = 'white';
button.style.padding = '10px 20px';
        """, language="javascript")

    with tab3:
        st.subheader("📡 Fetch API Examples")
        st.code("""
// GET request
fetch('https://api.example.com/data')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));

// POST request
fetch('https://api.example.com/users', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        name: 'John Doe',
        email: 'john@example.com'
    })
});
        """, language="javascript")

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

    tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "🔍 Resources", "📝 Describe", "⚙️ Management"])

    with tab1:
        col1, col2 = st.columns(2)

        with col1:
            if st.button("🏢 Cluster Info"):
                result = execute_command("kubectl cluster-info")
                st.code(result)

        with col2:
            if st.button("📦 All Pods"):
                result = execute_command("kubectl get pods --all-namespaces")
                st.code(result)

    with tab2:
        col1, col2 = st.columns(2)

        with col1:
            if st.button("🔧 Services"):
                result = execute_command("kubectl get services")
                st.code(result)

        with col2:
            if st.button("📱 Deployments"):
                result = execute_command("kubectl get deployments")
                st.code(result)

        if st.button("📊 Nodes"):
            result = execute_command("kubectl get nodes")
            st.code(result)

    with tab3:
        resource_type = st.selectbox("Resource Type:", ["pod", "service", "deployment", "node"])
        resource_name = st.text_input("Resource Name:")

        if st.button("🔍 Describe Resource") and resource_name:
            result = execute_command(f"kubectl describe {resource_type} {resource_name}")
            st.code(result)

    with tab4:
        st.subheader("⚙️ Resource Management")

        yaml_content = st.text_area("YAML Configuration:", height=200)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Apply Config") and yaml_content:
                # In a real implementation, you'd save this to a temp file
                st.success("Configuration would be applied!")
                st.code("kubectl apply -f config.yaml")

        with col2:
            delete_resource = st.text_input("Delete Resource (type/name):")
            if st.button("🗑️ Delete") and delete_resource:
                result = execute_command(f"kubectl delete {delete_resource}")
                st.code(result)

# ML Tasks
elif menu == "🤖 ML Tasks":
    st.header("🤖 Machine Learning & AI Tools")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠 Predictions", "🧠 NLP Models", "📊 Data Analysis", "📈 Visualization", "🧮 Statistics"])

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
            <            <small>Generated by Suhana's Toolkit at {format_timestamp()}</small>
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
    st.info("Jenkins integration is coming soon! Stay tuned.")

# AWS Tasks
elif menu == "☁️ AWS Tasks":
    st.header("☁️ AWS Cloud Services")
    st.info("AWS integration is coming soon! Stay tuned.")

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

    # Send SMS
    st.subheader("📱 Send SMS")
    # Input fields for Twilio credentials
    account_sid = st.text_input("Twilio Account SID:")
    auth_token = st.text_input("Twilio Auth Token:", type="password")  # Mask the token
    twilio_phone_number = st.text_input("Your Twilio Phone Number (with +):")  # Add input for Twilio phone number
    recipient_number = st.text_input("Recipient Number (with country code):")
    message = st.text_area("SMS Message:")

    if st.button("Send SMS"):
        try:
            # Your code to send SMS goes here (using Twilio)
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                to=recipient_number,
                from_=twilio_phone_number,  # Use the input Twilio phone number
                body=message
            )
            st.success(f"SMS sent successfully! Message SID: {message.sid}")

        except Exception as e:
            st.error(f"Error sending SMS: {e}")

# Featured Projects
elif menu == "⭐ Featured Projects":
    st.header("⭐ Featured Projects")
    st.info("Coming soon: Showcase of exciting projects!")

st.sidebar.header("About")
st.sidebar.info("This is Suhana's Toolkit, a collection of useful Python tools and utilities.")