import win32api

# Get the current user's home directory
home_dir = win32api.GetUserHomeFolder()

# Execute a command
win32api.ShellExecute(0, "open", "notepad.exe", None, None, win32con.SW_SHOW)

# Terminate a process
win32api.TerminateProcess(process_handle, 0)

import win32com

# Get a COM object
obj = win32com.GetObject("Excel.Application")

# Create a new COM object
obj = win32com.CreateObject("Excel.Application")

import win32con

# Show a window
win32gui.ShowWindow(window_handle, win32con.SW_SHOW)

# Hide a window
win32gui.ShowWindow(window_handle, win32con.SW_HIDE)

import win32gui

# Create a new window
window_handle = win32gui.CreateWindow(
    "Button", "Button", win32con.WS_OVERLAPPEDWINDOW,
    0, 0, 200, 50, 0, 0, 0, None
)

# Destroy a window
win32gui.DestroyWindow(window_handle)

# Get the text of a window
text = win32gui.GetWindowText(window_handle)

import win32process

# Create a new process
process_handle, thread_id, process_id, thread_handle = win32process.CreateProcess(
    None, "notepad.exe", None, None, 0,
    win32con.CREATE_NEW_CONSOLE, None, None,
    win32process.STARTUPINFO()
)

# Terminate a process
win32process.TerminateProcess(process_handle, 0)

# Get information about a process's memory usage
mem_info = win32process.GetProcessMemoryInfo(process_handle)

import win32security

# Look up the SID for a user account
sid, domain, type = win32security.LookupAccountName("", "Administrator")

# Add an ACE to an ACL
acl = win32security.ACL()
win32security.AddAce(acl, win32security.ACL_REVISION, 0, sid, win32con.GENERIC_ALL)
