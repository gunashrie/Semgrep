import sqlite3
from html import escape
 
def unsafe_output(data):
    print(data)  # ❌ This should be flagged
 
def safe_output(data):
    print(escape(data))  # ✅ This should not be flagged
 
unsafe_output("<script>alert('XSS')</script>")
safe_output("<script>alert('XSS')</script>")
