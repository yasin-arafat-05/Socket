import streamlit as st
import socket

st.title("File Downloader Client")

filename = st.text_input("Enter filename to download:")

if st.button("Download"):
    if not filename:
        st.error("Please enter a filename.")
    else:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(('localhost', 9999))
            client.send(filename.encode())
            response = client.recv(1024)
            if response == b'OK':
                data = b''
                while True:
                    chunk = client.recv(1000)
                    if not chunk:
                        break
                    data += chunk
                st.download_button(
                    label="Click to Download File",
                    data=data,
                    file_name=f"downloaded_{filename}",
                    mime="application/octet-stream"
                )
                st.success(f"File '{filename}' downloaded successfully. Click the button above to save it.")
            else:
                st.error(response.decode())
            client.close()
        except ConnectionRefusedError:
            st.error("Could not connect to the server. Make sure the server is running on localhost:9999.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")