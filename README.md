# AAV ROS2 Development

## Overview
This repository serves as the bare bones setup for ROS2 Development.


## SETUP with GitHub Codespaces
1. Open this repository on GitHub.
2. To create the codespace for the first time (skip to step 3 if you've already created the codespace):
    1. Click the green "Code" button.
    2. Switch to the "Codespaces" tab.
    3. Click the "+" button to create a new codespace.
    4. A new tab will open with the codespace. It will take approximately five minutes to build the container and prepare the codespace.
    5. Once the codespace is ready, you will see the terminal in the bottom of the window, and you will be in the `/workspaces/{repo-name}` directory.
    6. If you are prompted to install the recommended extensions, click "Install All" to install the recommended extensions. If you are not prompted, you can install the recommended extensions by clicking the extensions icon on the left sidebar, searching for "@recommended" in the search bar, and clicking the cloud icon next to "Workspace Recommendations".
3. To open the codespace after it has been created:
    1. Click the green "Code" button.
    2. Switch to the "Codespaces" tab.
    3. Click on the codespace you want to open.
    4. Optional: If you would like to open the codespace in VS Code on your local machine, perform steps 1-2, click the three dots on the right side of the codespace and select "Open with Visual Studio Code".
4. Make sure you are in the following directory:
    ```bash
    cd /workspaces/{repo-name}
    ```
    Replace `{repo-name}` with the name of the repository you created the codespace from.
5. [Build the workspace.](#building-the-workspace)
6. After you have finished working, close the tab with the codespace or close the VS Code window if you opened the codespace in VS Code.
7. To stop the codespace:
    1. Go back to the repository on GitHub.
    2. Click the "Code" button.
    3. Switch to the "Codespaces" tab.
    4. Click the three dots on the right side of the codespace and select "Stop codespace".

## Desktop Viewer
If you're using GitHub Codespaces, to view the turtlesim GUI or RQT_GRAPH, perform the following:
1. Press Ctrl/Cmd + Shift + P to open the command palette.
2. Type ">Ports" and select "Ports: Focus on Ports View".
3. In the "Ports" view, right-click on `6080` in the first column and select "Open in Browser" to open the desktop in a new tab. Alternatively, select "Preview in Editor" to view the desktop in the codespace.
5. You may need to wait a few minutes for the desktop to load.
6. Once you see the "noVNC" logo, click the "Connect" button to open the desktop.
7. The turtlesim GUI or RQT_GRAPH will be visible in the desktop (if you've started the turtlesim node or RQT_GRAPH).